import React from "react";
import "../styles/CameraGrid.css";

function AlertBox({ camera }) {
  return (
    <div className="alert-box">
      🚨 Suspicious activity detected on Camera {camera}!
    </div>
  );
}

export default AlertBox;
