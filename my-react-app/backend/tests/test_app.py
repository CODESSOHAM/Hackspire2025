"""
Test module for the Flask application.
"""
import pytest
from app import create_app
from app.camera import CameraManager

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

def test_get_all_cameras(client):
    """Test getting all cameras"""
    response = client.get("/api/cameras")
    assert response.status_code == 200
    data = response.get_json()
    assert "cameras" in data
    assert len(data["cameras"]) == 9

def test_get_camera_status(client):
    """Test getting specific camera status"""
    response = client.get("/api/camera/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "status" in data
    assert "suspicious_activity" in data

def test_trigger_alert(client):
    """Test triggering an alert"""
    response = client.post("/api/camera/1/alert")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "timestamp" in data

def test_system_status(client):
    """Test getting system status"""
    response = client.get("/api/system/status")
    assert response.status_code == 200
    data = response.get_json()
    assert "total_cameras" in data
    assert "active_cameras" in data
    assert "alerts_active" in data
    assert "system_status" in data