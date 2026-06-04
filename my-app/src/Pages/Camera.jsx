export default function Camera(){
    const startCamera = async () =>{
        try{
            const response = await fetch("http://127.0.0.1:8000/scan");
            const data = await response.json();
            console.log(data);
            alert("Camera started, Show the Code");
        }
        catch(error){
            console.error("Error starting camera.",error);
        };
    }
    return(
        <div>
            <h1>QR-Detector</h1>
            <button onClick={startCamera}>Start Scanning </button>
            <br></br>
            <img src = "http://127.0.0.1:8000/scan" alt = "Live Feed"></img>
        </div>
    )
}