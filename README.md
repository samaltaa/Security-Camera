

---

# Security Camera

**A Python-based security camera system that detects and tracks faces and eye movements, saves video recordings, and captures images of detected faces.**

## Features

- Real-time face and eye detection using Haar cascade classifiers.
- Tracks eye movements and logs directions in a text file.
- Records video when a face is detected and stops recording after no detection for a configurable duration.
- Saves images of detected faces with timestamps.
- Encoded file support for monitored individuals.

## Requirements

- Python 3.x
- OpenCV
- Pickle

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/samaltaa/Security-Camera.git
   cd Security-Camera
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python
   ```

3. Ensure the following files are in the project directory:
   - `haarcascade_frontalface_default.xml`
   - `haarcascade_eye.xml`
   - `EncodeFile.p`

## Usage

1. Run the script:
   ```bash
   python security_camera.py
   ```

2. Press `q` to exit the application.

## Directory Structure

- **Images/**: Stores images of detected faces.
- **Videos/**: Stores recorded video clips.
- **eye_movements.txt**: Logs detected eye movement directions.

## Future Updates

- Refactor code to reduce redundancy.
- Add additional functionalities like multi-camera support.

## License

This project is licensed under the MIT License.

---
