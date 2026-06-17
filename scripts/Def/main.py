import cv2
import time
from threading import Thread, Lock
from ScanQR import scan, scan_upload
from encoding import encode
from Camera_init import Webcam
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import base64
class URL(BaseModel):
    url: str
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state = {
    "running": False,
    "latest_frame": None
}
frame_lock = Lock()

def camera_loop():
    global state
    print("[CAMERA] Inside background thread. Opening camera index 0...")
    
    # Using default backend initialization
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[CAMERA] CRITICAL: Device index 0 could not be opened.")
        state["running"] = False
        return

    print("[CAMERA] Hardware hook secured. Capturing frames...")
    while state["running"]:
        ret, frame = cap.read()
        if ret and frame is not None:
            with frame_lock:
                state["latest_frame"] = frame.copy()
        else:
            time.sleep(0.01)
            
    cap.release()
    print("[CAMERA] Hardware released cleanly.")

@app.get("/start")
def start_scan():
    global state
    print("[HTTP] /start route hit.")
    
    if not state["running"]:
        state["running"] = True
        worker = Thread(target=scan, args=(Webcam(0), state), daemon=True)
        worker.start()
        print("[HTTP] Background thread spawned.")
        
    return {"status": "success", "message": "Camera activation triggered."}

@app.get("/stop")
def stop_scan():
    global state
    print("[HTTP] /stop route hit.")
    state["running"] = False
    with frame_lock:
        state["latest_frame"] = None
    return {"status": "success", "message": "Stopped."}

def generate_video_stream():
    global state
    while state["running"]:
        frame = None
        with frame_lock:
            if state["latest_frame"] is not None:
                frame = state["latest_frame"].copy()
        
        if frame is None:
            time.sleep(0.03)
            continue

        success, buffer = cv2.imencode(".jpg", frame)
        if not success:
            continue

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")
        time.sleep(0.03)

@app.get("/video")
def video_feed():
    return StreamingResponse(
        generate_video_stream(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
@app.post("/encode")
def encode_qr(url_link: URL):
    text = url_link.url
    encode(text)
    with open("qr_code_encoded.png","rb") as image_file:
        img_bs64 = base64.b64encode(image_file.read()).decode('utf-8')
    return {"qr_code": img_bs64}
