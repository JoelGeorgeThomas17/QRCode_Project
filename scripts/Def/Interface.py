import cv2
import threading
import time
from PIL import Image
import customtkinter as ctk

# Import your existing functional logic safely
from scripts.Def.encoding import encode, decode_qr

# Configure the visual style of your application window
ctk.set_appearance_mode("dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class QRApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sleek QR Studio")
        self.geometry("900x550")
        self.resizable(False, False)

        # Thread state controls
        self.camera_running = False
        self.cap = None

        # --- GRID LAYOUT SETUP ---
        self.grid_columnconfigure(0, weight=1, minsize=450)
        self.grid_columnconfigure(1, weight=1, minsize=450)
        self.grid_rowconfigure(0, weight=1)

        # ================= LEFT SIDE: SCANNER =================
        self.left_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#1e293b")
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.scanner_title = ctk.CTkLabel(self.left_frame, text="📷 Live QR Scanner", font=("Helvetica", 20, "bold"))
        self.scanner_title.pack(pady=15)

        # Video stream box placeholder
        self.video_label = ctk.CTkLabel(self.left_frame, text="Camera Offline", fg_color="#0f172a", width=400, height=300, corner_radius=10)
        self.video_label.pack(padx=20, pady=10)

        # Live Decoded Result output display
        self.result_label = ctk.CTkLabel(self.left_frame, text="Result: Waiting for scan...", font=("Helvetica", 13, "italic"), text_color="#94a3b8")
        self.result_label.pack(pady=10)

        self.scan_btn = ctk.CTkButton(self.left_frame, text="Start Scanner", font=("Helvetica", 14, "bold"), command=self.toggle_scanner, height=40)
        self.scan_btn.pack(pady=15)

        # ================= RIGHT SIDE: ENCODER =================
        self.right_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#1e293b")
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.encoder_title = ctk.CTkLabel(self.right_frame, text="✨ Generate QR Code", font=("Helvetica", 20, "bold"))
        self.encoder_title.pack(pady=15)

        self.url_input = ctk.CTkEntry(self.right_frame, placeholder_text="Paste your URL here (e.g., https://...)", width=350, height=40)
        self.url_input.pack(pady=15)

        self.gen_btn = ctk.CTkButton(self.right_frame, text="Generate & Save", font=("Helvetica", 14, "bold"), fg_color="#10b981", hover_color="#059669", command=self.generate_code, height=40)
        self.gen_btn.pack(pady=10)

        # Feedback text status for encoder activity
        self.status_label = ctk.CTkLabel(self.right_frame, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Standard clean window close routine
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # --- QR GENERATOR FUNCTION ---
    def generate_code(self):
        text = self.url_input.get().strip()
        if not text:
            self.status_label.configure(text="⚠️ Please enter a URL first!", text_color="#ef4444")
            return
        
        try:
            # Runs your encoding backend tool logic directly
            encode(text)
            self.status_label.configure(text="✅ QR Saved successfully as 'qr_code_encoded.png'!", text_color="#10b981")
        except Exception as e:
            self.status_label.configure(text=f"❌ Error: {str(e)}", text_color="#ef4444")

    # --- QR SCANNER CAM LOOP CONTROLLER ---
    def toggle_scanner(self):
        if not self.camera_running:
            self.camera_running = True
            self.scan_btn.configure(text="Stop Scanner", fg_color="#ef4444", hover_color="#dc2626")
            self.result_label.configure(text="Searching for QR code Matrix...", text_color="#38bdf8")
            
            # Start OpenCV thread so window loop never freezes
            self.cap = cv2.VideoCapture(0)
            threading.Thread(target=self.video_stream_loop, daemon=True).start()
        else:
            self.stop_camera_logic()

    def stop_camera_logic(self):
        self.camera_running = False
        self.scan_btn.configure(text="Start Scanner", fg_color="#3b82f6", hover_color="#2563eb")
        if self.cap:
            self.cap.release()
        self.video_label.configure(text="Camera Offline", image=None)

    def video_stream_loop(self):
        while self.camera_running:
            ret, frame = self.cap.read()
            if ret:
                # 1. Run your existing custom decode function against the current hardware image frame
                data, success = decode_qr(frame)
                
                if success and data:
                    self.result_label.configure(text=f"🎉 Found: {data}", text_color="#10b981")
                    # Stop loop instantly on successful read match
                    self.after(0, self.stop_camera_logic)
                    break

                # 2. Convert OpenCV visual matrix format (BGR) to Tkinter friendly image (RGB)
                cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_img = Image.fromarray(cv2_img)
                
                # Resize keeping aspect scale clean within framework container limits
                ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(400, 300))
                
                # Update UI elements safely inside window render schedule
                self.video_label.configure(image=ctk_img)
            
            time.sleep(0.01) # Keep execution light on CPU cycles

    def on_closing(self):
        self.camera_running = False
        if self.cap:
            self.cap.release()
        self.destroy()

if __name__ == "__main__":
    app = QRApp()
    app.mainloop()