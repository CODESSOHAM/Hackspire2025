"""
Camera module for handling camera-related operations and state management.
"""
from datetime import datetime

class CameraManager:
    def __init__(self):
        self.camera_states = {
            f"camera_{i}": {
                "status": "active",
                "last_alert": None,
                "suspicious_activity": False
            } for i in range(1, 10)
        }
    
    def get_all_cameras(self):
        """Get status of all cameras"""
        return [
            {
                "id": i,
                "status": self.camera_states[f"camera_{i}"]["status"],
                "suspicious_activity": self.camera_states[f"camera_{i}"]["suspicious_activity"],
                "last_alert": self.camera_states[f"camera_{i}"]["last_alert"]
            }
            for i in range(1, 10)
        ]
    
    def get_camera(self, camera_id):
        """Get status of a specific camera"""
        camera_key = f"camera_{camera_id}"
        if camera_key not in self.camera_states:
            return None
        
        return {
            "id": camera_id,
            "status": self.camera_states[camera_key]["status"],
            "suspicious_activity": self.camera_states[camera_key]["suspicious_activity"],
            "last_alert": self.camera_states[camera_key]["last_alert"]
        }
    
    def trigger_alert(self, camera_id):
        """Trigger an alert for a specific camera"""
        camera_key = f"camera_{camera_id}"
        if camera_key not in self.camera_states:
            return None
        
        self.camera_states[camera_key]["suspicious_activity"] = True
        self.camera_states[camera_key]["last_alert"] = datetime.now().isoformat()
        return self.camera_states[camera_key]["last_alert"]
    
    def reset_alert(self, camera_id):
        """Reset alert status for a specific camera"""
        camera_key = f"camera_{camera_id}"
        if camera_key not in self.camera_states:
            return False
        
        self.camera_states[camera_key]["suspicious_activity"] = False
        return True
    
    def get_system_status(self):
        """Get overall system status"""
        active_cameras = sum(1 for cam in self.camera_states.values() if cam["status"] == "active")
        alerts_active = sum(1 for cam in self.camera_states.values() if cam["suspicious_activity"])
        
        return {
            "total_cameras": len(self.camera_states),
            "active_cameras": active_cameras,
            "alerts_active": alerts_active,
            "system_status": "operational"
        }