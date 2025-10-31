"""
Initialize Flask application and register blueprints.
"""
from flask import Flask, send_from_directory
from flask_cors import CORS
import os

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__, static_folder='../../dist')
    CORS(app)  # Enable CORS for all routes

    # Ensure the captured_frames directory exists
    if not os.path.exists('captured_frames'):
        os.makedirs('captured_frames')

    # Register blueprints
    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    # Serve React App
    @app.route('/')
    def serve():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>')
    def serve_static(path):
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')

    return app