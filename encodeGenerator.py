import cv2
import face_recognition
import pickle
import os

# Path to the folder containing images
FolderPath = "Images"

# List image paths
PathList = os.listdir(FolderPath)
print(PathList)
imgList = []
monitoredIds = []

# Load images of monitored individuals
for path in PathList:
    imgList.append(cv2.imread(os.path.join(FolderPath, path)))
    monitoredIds.append(os.path.splitext(path)[0])
print(monitoredIds)

# Function
def findEncodings(images_list
):
    encode_list = []
    for img in images_list:
        # Switch BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Get the facial encodings
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    
    return encode_list

encodings = findEncodings(imgList)
print(encodings)