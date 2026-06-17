import { useState } from "react"
import { useNavigate } from "react-router-dom"

export default function Create() {
    const [img, setImg] = useState(null);
    const [urlText, setUrlText] = useState(""); // Track input securely
    const navigate = useNavigate();

    const send = async () => {
        if (!urlText.trim()) {
            alert("Please enter a URL first!");
            return;
        }

        try {
            const res = await fetch("http://127.0.0.1:8000/encode", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ url: urlText }) // Sends the exact state string
            });

            const data = await res.json();
            
            if (data.qr_code) {
                setImg(data.qr_code); 
            } else if (data.error) {
                console.error("Backend Error:", data.error);
            }
        } catch (error) {
            console.error("Network error connecting to backend:", error);
        }
    };

    return (
        <div>
            <div className="button-container"></div>
            {img && (
                <img
                    src={`data:image/png;base64,${img}`}
                    alt="QR Code"
                />
            )}
            <br />
            
            {/* Bound value and onChange handler directly to React state */}
            <input 
                type="text" 
                placeholder="Enter URL" 
                value={urlText}
                onChange={(e) => setUrlText(e.target.value)}
                style={{ width: "490px", height: "40px", borderRadius: "16px" }} 
            />
            <br /><br />
            <button onClick={send}> Generate QR Code </button>
            <br />
            <button onClick={() => navigate("/")}>Exit</button>
        </div>
    );
}