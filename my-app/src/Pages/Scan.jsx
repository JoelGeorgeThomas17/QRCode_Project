import { useNavigate } from "react-router-dom"

export default function Scan(){
    const navigate = useNavigate();
    return(
        <>
        <div className="button-container">
        </div>
        <br></br>
        <div>
        <h1></h1>
        <button onClick={() => navigate("/upload")}>Upload QR Code</button>
        <br />
        <button onClick={() => navigate("/camera")}>Scan</button>
         <br />
        <button onClick={() =>navigate("/")}>Exit</button>
        </div>
        </>
    )
}