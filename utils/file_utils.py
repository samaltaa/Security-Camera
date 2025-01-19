import os
import pickle
import cv2

def initialize_directories():
    if not os.path.exists("Images"):
        os.makedirs("Images")
    if not os.path.exists("Videos"):
        os.makedirs("Videos")

def load_encodings(file_path):
    print("Loading Encoded File...")
    with open(file_path, "rb") as file:
        encodings = pickle.load(file)
    print("Encoded File Loaded, ready to monitor area....")
    return encodings

def initialize_video_writer(output_path, frame_size, codec):
    return cv2.VideoWriter(output_path, codec, 20, frame_size)


