import cv2
import sys
import numpy as np
from encoding import decode_qr
import time


def scan(webcam,scan_var):
    
    try:
        webcam.open()
        while scan_var["running"]:
            img = webcam.read()
            cv2.imwrite("qr_code.png",img);
            data,return_status =decode_qr(img)
            
            if return_status:
                scan_var["running"] = False
                break;
            else:
                continue;
            time.sleep(0.1)
        webcam.close()
    except Exception as e:
        print(f"Error occurred while scanning: {e}")    

def scan_upload(img_bytes):
    np_array = np.frombuffer(img_bytes, np.uint8)

    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return decode_qr(img)   

