import { useNavigate } from "react-router-dom"
import blueLogo from "../assets/blue_logo.png"

export default function HomePage() {
    const navigate = useNavigate()
    return(
<div><h1></h1>
      <img src={blueLogo} alt="QR Code" />
      <br></br>
      <button onClick={() => navigate("/scan")} >Scan QR code</button>
      <br></br>
      <button onClick={() => navigate("/create")}>Create QR code</button>
      </div>
        )
      }
