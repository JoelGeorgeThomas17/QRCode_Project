# QR Code Detection and Validation System

A full-stack QR code detection application built with **React**, **FastAPI**, **OpenCV**, and **Python**. The system captures live camera frames, detects and decodes QR codes in real time, and displays results through a web-based interface.

---

## Overview

This project provides a real-time QR code scanning solution by combining a React frontend with a FastAPI backend. The backend continuously captures frames from a connected camera, processes them using OpenCV and QR decoding libraries, and streams the results to the frontend.

The application is designed for scenarios such as:

- Attendance tracking
- Inventory management
- Asset identification
- Access control systems
- QR-based authentication workflows

---

## Features

- Real-time camera feed streaming
- QR code detection and decoding
- FastAPI REST API backend
- React-based user interface
- Live scan result updates
- Modular and scalable architecture
- Easy deployment and configuration

---

## Technology Stack

### Frontend

- React
- Vite
- JavaScript
- HTML5
- CSS

### Backend

- Python 3.x
- FastAPI
- Uvicorn
- OpenCV
- NumPy

---

## Project Structure

```text
project-root/
│
├── backend/
│   ├── Camera_init.py
│   ├── encoding.py
│   ├── Interface.py
│   ├── ScanQR.py
│   ├── main.py
│   └── ...
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   ├── main.jsx
│   │   ├── Pages/
|   │   │   ├── Camera.jsx
|   │   │   ├── Create.jsx
|   │   │   ├── HomePage.jsx
|   │   │   ├── Scan.jsx
|   │   │   ├── Upload.jsx 
│   ├── package.json
│   └── ...
│
├── README.md
├── Requirements.txt
└── .gitignore
|__
```

---

## System Architecture

```text
+------------------+
|      Camera      |
+--------+---------+
         |
         v
+------------------+
|     OpenCV       |
| Frame Capture    |
+--------+---------+
         |
         v
+------------------+
|  QR Detection    |
|    & Decoding    |
+--------+---------+
         |
         v
+------------------+
|     FastAPI      |
|     Backend      |
+--------+---------+
         |
         v
+------------------+
|      React       |
|     Frontend     |
+------------------+
```

---

## Application Workflow

1. The user opens the React application.
2. The frontend requests a live video stream from the FastAPI backend.
3. The backend continuously captures frames from the system camera.
4. Each frame is processed for QR code detection.
5. When a QR code is found, the encoded data is extracted.
6. The decoded information is returned to the frontend.
7. The frontend displays the scanned QR code information in real time.

---

## Prerequisites

Before running the application, ensure the following are installed:

- Python 3.9+
- Node.js 18+
- npm
- Git
- Webcam or external camera

Verify installations:

```bash
python --version
node --version
npm --version
git --version
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-system.git
cd qr-code-system
```

---

## Backend Setup

### Create Virtual Environment

#### Windows

```bash
python -m venv venv_name
.\venv_name\Scripts\activate
```
---

### Install Dependencies

```bash
pip install -r Requirements.txt
```

Example `requirements.txt`:

```text
fastapi
uvicorn
opencv-python
pyzbar
numpy
python-multipart
```

---

### Run Backend Server

```bash
python -m uvicorn main:app --reload
```

Backend server:

```text
http://localhost:8000
```
---

## Frontend Setup

Install dependencies:

```bash
npm install
```

Start development server: From project root

```bash
cd my-app
npm run dev
```

Frontend server:

```text
http://localhost:5173
```

---

## API Endpoints

### Health Check

```http
GET /
```

Example Response:

```json
{
  "status": "running"
}
```

---

### Video Stream

```http
GET /video
```

Returns a live MJPEG camera stream.

---

### QR Detection

```http
GET /detect
```

Example Response:

```json
{
  "detected": true,
  "data": "https://example.com"
}
```

---

## Example Frontend Usage

```jsx
function CameraFeed() {
  return (
    <img
      src="http://localhost:8000/video"
      alt="Live Camera Feed"
      width="700"
    />
  );
}

export default CameraFeed;
```

---

## Configuration

### Enable CORS

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Troubleshooting

### Camera Does Not Open

Check if another application is currently using the camera:

- Zoom
- Microsoft Teams
- Discord
- Google Meet

Test camera availability:

```python
import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())
```

---

### Frontend Cannot Display Video

Verify:

- Backend server is running.
- Endpoint `/video` is accessible.
- CORS is configured correctly.
- Camera permissions are granted.

---

### QR Codes Are Not Detected

Check:

- QR code is clearly visible.
- Lighting conditions are sufficient.
- Camera focus is correct.
- QR decoder library is installed correctly.

---

## Future Improvements

- WebSocket-based communication
- WebRTC video streaming
- Multiple camera support
- User authentication and authorization
- Scan history storage
- Database integration
- Docker containerization
- Cloud deployment
- QR code generation module

---

## Security Considerations

- Restrict CORS origins in production.
- Validate all incoming requests.
- Use HTTPS for deployed environments.
- Secure API endpoints with authentication.
- Store sensitive scan data securely.

---

## License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
```

---

## Authors



Full-Stack Developer

Built using React, FastAPI, OpenCV, and Python.

---

## Acknowledgements

- FastAPI
- React
- OpenCV
- Uvicorn
- PyZBar
- Python Community

---

