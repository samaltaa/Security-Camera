import cv2
import time
import datetime


# define a video capture object
cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detection = False 
detection_stopped_time = None
time_started = False
SECONDS_TO_RECORD_AFTER_FACE_DETECTED = 5

# define frame size 
frame_size = (int(cap.get(3)), int(cap.get(4)))
#define the codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")


while(True):

    #capture the video frame by frame 
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor =1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    # this entire block of code takes care of beginning recoding once
    # face is detected, if face is undetected for 5+ seconds, recording stops
    if len(faces) > 0:
            if detection:
                 time_started = False
            else:
                 detection = True
                 current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                 out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
                 print("Started Recording")
    elif detection:
         if time_started:
              if time.time() - detection_stopped_time > SECONDS_TO_RECORD_AFTER_FACE_DETECTED:
                   detection = False
                   time_started = False
                   out.release()
                   print("Recording Stopped")
         else:
            time_started = True
            detection_stopped_time = time.time()
    if detection:
        out.write(frame)

    # draw a rectangle around the faces detected 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    #display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the quitting button 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
# after the loop release the cap object 
cap.release()
# destroy all the windows
cv2.destroyAllWindows()