import cv2
import face_recognition
import os
import numpy as np

path="Avatar"
images = []
classNames = []
myList =os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f"{path}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

#step encoding
def Mahoa(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR được chuyển đổi sang RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnow = Mahoa(images)

#start webcam
def FaceID(namelist):
    checkFace = 0
    mytest = 0
    cap = cv2.VideoCapture(0)
    
    while not checkFace:
        ret, frame= cap.read()
        framS = cv2.resize(frame,(0,0),None,fx=0.5,fy=0.5)
        framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        framS = cv2.flip(framS, 1)
        frame = cv2.resize(frame, (0, 0), None, fx=1.5, fy=1.5)
        facecurFrame = face_recognition.face_locations(framS)
        encodecurFrame = face_recognition.face_encodings(framS)

        for encodeFace, faceLoc in zip(encodecurFrame,facecurFrame):
            faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
            matchIndex = np.argmin(faceDis)

            if faceDis[matchIndex] < 0.30:
                checkFace = 1
                mytest = 1
                myID = namelist[matchIndex]
                break

        cv2.putText(frame, 'Press q to exit', (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('FaceID', frame)

        if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
            break


    cap.release()
    cv2.destroyAllWindows()
    if (mytest):
        realId = myID[0] + myID[1] + myID[2]
        return realId
    else:
        return 0

