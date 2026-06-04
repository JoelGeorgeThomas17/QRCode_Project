import { useNavigate } from "react-router-dom"

export default function Scan(){
    const navigate = useNavigate();
    return(
        <div>
        <h1>"Scan Page"</h1>
        <button onClick={() => navigate("/upload")}>Upload QR Code</button>
        <br></br>
        <button onClick={() => navigate("/camera")}>Scan</button>
        </div>
    )
}