import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import CameraGrid from "./pages/CameraGrid";
import SingleCamera from "./pages/SingleCamera";
import "./index.css";

function App() {
  return (
    <Router>
      <nav className="navbar">
        <h2>Surveillance System</h2>
        <div>
          <Link to="/">Grid View</Link>
          <Link to="/single">Single Camera</Link>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<CameraGrid />} />
        <Route path="/single" element={<SingleCamera />} />
      </Routes>
    </Router>
  );
}

export default App;
