import cv2


# define a video capture object
cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recording = False 
frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

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
    if len(faces) > 0:
            recording = True

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