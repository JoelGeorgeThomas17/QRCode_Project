import {BrowserRouter, Routes , Route} from "react-router-dom"
import Scan from './Pages/Scan'   
import Create from "./Pages/Create"
import HomePage  from './Pages/HomePage'
import Upload from "./Pages/Upload"
import Camera from "./Pages/Camera"
import './App.css'

function App() {
  
  return (
    <BrowserRouter>
       <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/scan" element={<Scan />} />
        <Route path="/create" element={<Create />} />
        <Route path="/upload" element={<Upload />}/>
        <Route path="/camera" element={<Camera />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
