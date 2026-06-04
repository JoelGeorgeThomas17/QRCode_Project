import cv2;
from ScanQR import scan
from ScanQR import scan_upload
from encoding import encode
from fastapi import FastAPI
from threading import Thread
from Camera_init import Webcam
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
import base64
from io import BytesIO
class URL(BaseModel):
    url:str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
webcam = Webcam(0, 1920, 1080)




@app.post("/upload")



async def upload(file: UploadFile = File()):
    img = await file.read()
    data,result = scan_upload(img)
    return{
        "data":data
    };
@app.post("/encode")
async def encode_url(url: URL):
    try:
        encode(url.url)
        img = Image.fromarray(cv2.imread("qr_code_encoded.png"))
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return {"image": img_str}
    except ValueError as ve:
        return {"error": str(ve)}
@app.get("/scan")
def main():
    
    Thread(target=scan(webcam),daemon=True).start()
   
    return {"message": "QR code scanning started"}
if __name__ == "__main__":
    main()