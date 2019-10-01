import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('//home//xander999//Desktop//haar-cascade-files-master//haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('recognizer//trainingdata.yml')
id=0

while(True):
    tf, frame=cam.read()
    #cv2.imshow('SingleFrame',frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        id=rec.predict(gray[y:y+h,x:x+w])
        print(id)
        cv2.putText(frame,str(id),(x,y+h),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,255)
    cv2.imshow('Scanning...',frame)
    key=cv2.waitKey(1)
    if key==27:
        break
    elif key==ord('x'):
        print('You have been printing X')
cam.release()
cv2.destroyAllWindows()






