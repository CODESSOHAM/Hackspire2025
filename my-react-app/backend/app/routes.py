"""
Routes module for handling all API endpoints.
"""
from flask import Blueprint, jsonify, request, send_from_directory
from datetime import datetime
import os
from .camera import CameraManager

# Initialize the camera manager
camera_manager = CameraManager()

# Create blueprint for API routes
api = Blueprint('api', __name__)

@api.route('/cameras', methods=['GET'])
def get_all_cameras():
    """Get status of all cameras"""
    return jsonify({"cameras": camera_manager.get_all_cameras()})

@api.route('/camera/<int:camera_id>', methods=['GET'])
def get_camera_status(camera_id):
    """Get status of a specific camera"""
    camera = camera_manager.get_camera(camera_id)
    if camera is None:
        return jsonify({"error": "Camera not found"}), 404
    return jsonify(camera)

@api.route('/camera/<int:camera_id>/alert', methods=['POST'])
def trigger_alert(camera_id):
    """Trigger an alert for a specific camera"""
    timestamp = camera_manager.trigger_alert(camera_id)
    if timestamp is None:
        return jsonify({"error": "Camera not found"}), 404
    return jsonify({
        "message": f"Alert triggered for camera {camera_id}",
        "timestamp": timestamp
    })

@api.route('/camera/<int:camera_id>/reset', methods=['POST'])
def reset_alert(camera_id):
    """Reset alert status for a specific camera"""
    if not camera_manager.reset_alert(camera_id):
        return jsonify({"error": "Camera not found"}), 404
    return jsonify({
        "message": f"Alert reset for camera {camera_id}"
    })

@api.route('/camera/<int:camera_id>/frame', methods=['POST'])
def save_frame(camera_id):
    """Save a captured frame from a specific camera"""
    if 'frame' not in request.files:
        return jsonify({"error": "No frame provided"}), 400
    
    frame = request.files['frame']
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"camera_{camera_id}_{timestamp}.jpg"
    frame_path = os.path.join('captured_frames', filename)
    
    frame.save(frame_path)
    
    return jsonify({
        "message": "Frame saved successfully",
        "filename": filename
    })

@api.route('/system/status', methods=['GET'])
def get_system_status():
    """Get overall system status"""
    return jsonify(camera_manager.get_system_status())