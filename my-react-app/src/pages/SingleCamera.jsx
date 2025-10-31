import React, { useEffect, useRef, useState } from "react";
import "../styles/SingleCamera.css";

function SingleCamera() {
  const videoRef = useRef(null);
  const [alert, setAlert] = useState(false);

  useEffect(() => {
    async function getCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        if (videoRef.current) videoRef.current.srcObject = stream;
      } catch (err) {
        console.error("Camera access denied:", err);
      }
    }
    getCamera();
  }, []);

  // Simulated abnormal movement detection (randomized demo)
  useEffect(() => {
    const interval = setInterval(() => {
      if (Math.random() > 0.85) {
        setAlert(true);
        setTimeout(() => {
          document.body.style.backgroundColor = "black";
          alert("⚠️ Abnormal movement detected! System locked.");
          window.location.reload();
        }, 1000);
      }
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="single-camera-page">
      <h1>Live Camera Feed</h1>
      <video ref={videoRef} autoPlay playsInline className="camera-feed" />
      <div className="gesture-section">
        <h2>Gesture & Movement Detection</h2>
        <p>
          {alert
            ? "⚠️ Abnormal movement detected!"
            : "Monitoring for gestures and creepy movements..."}
        </p>
      </div>
    </div>
  );
}

export default SingleCamera;
