# Security-Camera
# Security Camera



This is a Python-based project that utilizes the OpenCV library, Haar Cascade algorithm, time, and datetime libraries to create a system capable of detecting faces in a video frame, recording when a face is detected, and automatically uploading the recorded video once the face is out of frame for a specified duration.

## Features

- Real-time face detection using the Haar Cascade algorithm.
- Automatic recording of video when a face is detected.
- Video recording stops and uploads when face is out of frame for 5+ seconds.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samaltaa/face-detection-recording.git
   ```

2. Navigate to the project directory:

   ```bash
   cd face-detection-security-cam
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install opencv-python
   ```

## Usage

1. Run the `main.py` script to start the face detection and recording system:

   ```bash
   python main.py
   ```

2. The system will utilize your default camera to capture video frames. When a face is detected, the recording will start automatically.

3. Once the detected face is out of frame for 5 or more seconds, the recording will stop, and the video will be uploaded to the same directory using the `release()` method.

4. Press `q` to exit the system.

## Configuration

You can customize the following parameters in the `main.py` script:

- `OUT_FOLDER`: The folder where recorded videos will be saved.
- `VIDEO_WIDTH` and `VIDEO_HEIGHT`: The width and height of the recorded video frames.
- `FACE_CASCADE_XML`: The path to the Haar Cascade XML file for face detection.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project makes use of the OpenCV library: https://opencv.org/

Special thanks to the contributors and maintainers of this library.

## Disclaimer

This project is intended for educational and informational purposes only. The creators and contributors of this project are not responsible for any unauthorized or improper use of the system.
