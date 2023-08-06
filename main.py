import cv2
import sys

# cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# define a video capture object
vid = cv2.VideoCapture(0)




while(True):

    #capture the video frame by frame 
    ret, frame = vid.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor =1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # draw a rectangle around the faces detected 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    #display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the quitting button 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# after the loop release the cap object 
vid.release()
# destroy all the windows
cv2.destroyAllWindows()