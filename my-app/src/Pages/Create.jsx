import {useState} from "react"
export default function Create() {
    const [img, setImg] = useState(null);
     const send = async () => {
        let text = document.getElementById("URL").value;

        const res = await fetch("http://127.0.0.1:8000/encode", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: text })
        });

        const data = await res.json();
        setImg(data.image); // adjust based on backend response
    };

    return(
        <div>
        <h1>Create Page</h1>
        <br></br>
        <br></br>
        {img && (
                <img
                    src={`data:image/png;base64,${img}`}
                    alt="QR Code"
                />
            )}
        <br></br>
        
        <input type="text" id="URL" placeholder="Enter URL"/> 
        <button onClick={send}> Generate QR Code </button>
        
         

        </div>

    )
}

