import {useState} from "react";
import { useNavigate } from "react-router-dom";
export default function Camera(){
    const navigate = useNavigate();
    const [isStreaming,setIsStreaming] = useState(null)
   const startCamera = async () => {
    console.log("Start Scanning button clicked! Sending request to backend...");
    try {
        const response = await fetch("http://127.0.0.1:8000/start", {
            method: "GET",
            headers: {
                "Accept": "application/json",
            }
        });
        const result = await response.json();
        console.log("Backend responded with:", result);
        
        if (result.status === "success") {
            setIsStreaming(true);
        } else {
            alert("Backend error: " + result.message);
        }
    } catch (error) {
        console.error("CRITICAL FRONTEND ERROR: Failed to reach backend server.", error);
        alert("Could not reach the server. Is FastAPI running on port 8000?");
    }
};
    const stop = async () => {
        await fetch("http://127.0.0.1:8000/stop");
        setIsStreaming(false);
    };
    return(
        <div>
            <h1>QR-Detector</h1>
            <button onClick={startCamera}>Start Scanning </button>
            <br></br>
            <button onClick={stop}>Stop Scanning</button>
            <br></br>
            <button onClick={() =>navigate("/")}>Exit</button>
             <br></br>
            {isStreaming && (
                <img src={`http://127.0.0.1:8000/video`} width="600" height="480" alt="Live Feed" />
            )}
        </div>
    )
}