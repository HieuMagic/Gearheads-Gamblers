import cv2
import time
from docx import Document
import Aready
# Capturing video from webcam:
cap = cv2.VideoCapture(0) # 0 is default webcam
path = "Avatar"
def TakePhotos(Id):
    currentFrame = 0
    count = 0
    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.resize(frame,(0,0), None, fx = 1.5, fy = 1.5)

        # Handles the mirroring of the current frame
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        framS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Saves image of the current frame in png file
        name = Id + str(currentFrame) + '.jpg'
        name = path + '/' + name
        cv2.imwrite(name, frame)

        # Display the resulting frame
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # To stop duplicate images
        currentFrame += 1
        time.sleep(0.01)
        count += 1
        if(count >= 3):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
