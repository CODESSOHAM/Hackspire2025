import React from "react";
import "../styles/CameraGrid.css";

function CameraBox({ number, onAlert }) {
  return (
    <div className="camera-box">
      <div className="camera-label">Camera {number}</div>
      <div className="camera-placeholder">
        <p>Feed unavailable</p>
      </div>
      <button className="alert-btn" onClick={onAlert}>
        Simulate Suspicious Activity
      </button>
    </div>
  );
}

export default CameraBox;
