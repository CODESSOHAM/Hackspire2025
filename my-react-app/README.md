# Samraksana - Video Surveillance System

A modern web-based surveillance system built with React and Flask, featuring real-time camera monitoring and suspicious activity detection.

## Features

- Multi-camera grid view
- Single camera detailed view
- Suspicious activity detection
- Real-time alerts
- Camera frame capture
- Gesture detection

## Tech Stack

### Frontend
- React 19
- Vite
- React Router DOM
- Modern CSS with Neo Brutalism design

### Backend
- Flask
- OpenCV
- NumPy
- Flask-CORS

## Prerequisites

- Node.js (v20.19+ or v22.12+)
- Python 3.12+
- pip
- Webcam (for testing)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd my-react-app
```

2. Install frontend dependencies:
```bash
npm install
```

3. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

## Development

1. Start the Flask backend:
```bash
cd backend
python app.py
```
The backend will run on http://localhost:5000

2. In a new terminal, start the frontend development server:
```bash
npm run dev
```
The frontend will run on http://localhost:5173

## Production

1. Build the frontend:
```bash
npm run build
```

2. Start the production server:
```bash
cd backend
python app.py
```
The application will be available at http://localhost:5000

## Accessing from Other Devices

To access the application from other devices on the same network:
1. Find your computer's IP address
2. Access the application at `http://<your-computer-ip>:5000`

Note: Make sure your firewall allows connections on port 5000.

## Project Structure

```
my-react-app/
├── src/                    # Frontend source code
│   ├── components/         # React components
│   ├── pages/             # Page components
│   ├── styles/            # CSS styles
│   └── assets/            # Static assets
├── backend/               # Flask backend
│   ├── app.py            # Main Flask application
│   ├── requirements.txt   # Python dependencies
│   └── captured_frames/   # Stored camera frames
└── dist/                  # Built frontend files
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
