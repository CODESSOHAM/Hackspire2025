import React, { useState } from "react";
import "../styles/CameraGrid.css";
import CameraBox from "../components/CameraBox";
import AlertBox from "../components/AlertBox";

function CameraGrid() {
  const [alertCamera, setAlertCamera] = useState(null);

  const triggerAlert = (cameraNumber) => {
    setAlertCamera(cameraNumber);
    setTimeout(() => setAlertCamera(null), 4000);
  };

  return (
    <div className="grid-page">
      <h1>All Camera Feeds</h1>
      <div className="camera-grid">
        {Array.from({ length: 9 }).map((_, i) => (
          <CameraBox
            key={i}
            number={i + 1}
            onAlert={() => triggerAlert(i + 1)}
          />
        ))}
      </div>
      <div className="detection-section">
        <h2>Suspicious Activity Detection</h2>
        {alertCamera ? (
          <AlertBox camera={alertCamera} />
        ) : (
          <p>No suspicious activity detected yet.</p>
        )}
      </div>
    </div>
  );
}

export default CameraGrid;
