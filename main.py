import cv2
import time
import datetime


# define a video capture object
cap = cv2.VideoCapture(0)

# load Haar cascade classifiers for boths face and eyes
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#open text file for writing
output_file = open("eye_movements.txt", "w")

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

    #detect eyes to track their movement
    for (x,y,w,h) in faces:
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         eyes = eyeCascade.detectMultiScale(roi_gray)
         for (ex,ey,ew,eh) in eyes:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
              #calculate the eye gaze direction
              eye_roi_gray = roi_gray[ey:ey+eh, ex:ex+ew]
              eye_roi_color = roi_color[ey:ey+eh, ex:ex+ew]
              _, eye_thresh = cv2.threshold(eye_roi_gray, 50, 255, cv2.THRESH_BINARY_INV)
              contours, _ = cv2.findContours(eye_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
              if len(contours) > 0:
                   pupil = max(contours, key=cv2.contourArea)
                   x1, y1, w1, h1 = cv2.boundingRect(pupil)
                   center = (int(x1 + w1/2), int(y1 + h1/2))
                   cv2.circle(eye_roi_color, center, 3, (255, 0, 0), -1)

                   #determine & record eye movement direction and store in txt file
                   if center[0] < ew / 3:
                        direction = "left"
                   elif center[0] > 2 * ew / 3:
                        direction = "right"
                   elif center[1] < eh / 3:
                        direction = "up"
                   elif center[1] > 2 * eh / 3:
                        direction = "down"
                   else:
                        direction = "center"

                    # record eye movement direction and store it in txt file
                   output_file.write(f"the eyes of the person in the room moved {direction}\n")
                    

    # draw a rectangle around the faces detected 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    #display the resulting frame
    cv2.imshow('Security Cam', frame)

    # the 'q' button is set as the quitting button 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
#close output file
output_file.close()
# after the loop release the cap object 
cap.release()
# destroy all the windows
cv2.destroyAllWindows()