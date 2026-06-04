import tkinter as tk
from tkinter import ttk
import cv2
from Camera_init import Webcam
camera = Webcam(0);
from ScanQR import scan
root = ttk.Tk()
root.title("My First GUI")
root.geometry("300x150")

label = ttk.Label(root, text="Tkinter works!")
label.pack(pady=20)
style = ttk.Style()

print(style.theme_names())   # shows available themes
style.theme_use("vista")      # try: clam, alt, default, classic

ttk.Button(root, text="Styled Button").pack(padx=20, pady=20)

button = ttk.Button(root, text="Close", command=root.destroy)
button.pack()
button2 = ttk.Button(root, text="Scan QR", command= lambda:scan(camera))
button2.pack()
root.mainloop()