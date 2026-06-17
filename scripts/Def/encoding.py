import cv2
try:
    import qrcode
except Exception as e:
    raise ImportError("The 'qrcode' package is required but could not be imported. Install it with: pip install qrcode[pil]") from e
import webbrowser as web
def encode(url):
    if(url.startswith('http') or url.startswith('https') or url.startswith('www')):

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr_code_encoded.png")
    else:
        raise ValueError("Invalid URL. Please provide a valid URL starting with http, https, or www.")
    
    

def decode_qr(img):
    return_status = False
    # Use OpenCV to load the image instead of PIL to avoid PIL import issues
    
    detector = cv2.QRCodeDetector();
    if img is None:
        print("No image found.")
        return None,return_status
    data, bbox, _ = detector.detectAndDecode(img);
    if data:
        print("Decoded data:", data)
        
    else:
       return None,return_status;
    if (data.startswith('http') or data.startswith('https') or data.startswith('www')):
      web.open(data)  
      return_status = True
    return data,return_status