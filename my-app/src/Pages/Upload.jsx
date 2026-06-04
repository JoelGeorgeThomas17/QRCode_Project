import {useState} from 'react'
export default function Upload(){
    const [image, setImage] = useState(null);
    const handleChange = (e) => {
    const file = e.target.files[0];
    setImage(URL.createObjectURL(file));
  };
    const sendBackend = async () => {
          const fileInput = document.querySelector('input[type="file"]');

    const file = fileInput.files[0];

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

  console.log(data);};
    return (
        <div>
        <h1>"Upload Page"</h1>
        <input type = "file" onChange = {handleChange} />
        {image && <img src={image}  alt="Uploaded QR Code" width = "200" height = "200" />}
        <button onClick={sendBackend}>Use this QR Code</button>
        </div>
    )
}