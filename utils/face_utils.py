import datetime
import cv2

def detect_faces(face_cascade, gray_frame):
    return face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

def save_face_image(frame, face_index):
    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    image_path =f"./Images/face_{current_time}_{face_index}.jpg"
    cv2.imwrite(image_path, frame)
    print(f"Intruder Face Captured at: {current_time}")