import { useNavigate } from "react-router-dom"

export default function HomePage() {
    const navigate = useNavigate()
    return(
<div><h1>QR-App</h1>
      <button onClick={() => navigate("/scan")} >Scan QR code</button>
      <br></br>
      <button onClick={() => navigate("/create")}>Create QR code</button>
      </div>
        )
      }
