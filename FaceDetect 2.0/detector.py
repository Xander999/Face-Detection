import numpy as np
import cv2
import sqlite3
import cv2.face
face_cascade = cv2.CascadeClassifier('//home//xander999//Desktop//haar-cascade-files-master//haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)
rec=cv2.face.createLBPHFaceRecognizer()
rec.load('recognizer//trainingdata.yml')
id=0

def getProfile(id):
    conn=sqlite3.connect('FaceBase.db')
    cmd="SELECT * FROM PEOPLE WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

while(True):
    tf, frame=cam.read()
    #cv2.imshow('SingleFrame',frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        id=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            cv2.putText(frame,str(profile[1]),(x,y+h+30),cv2.FONT_HERSHEY_PLAIN,1,255)
            cv2.putText(frame,str(profile[2]),(x,y+h+60),cv2.FONT_HERSHEY_PLAIN,1,255)
            cv2.putText(frame,str(profile[3]),(x,y+h+90),cv2.FONT_HERSHEY_PLAIN,1,255)
          
    cv2.imshow('Scanning...',frame)
    key=cv2.waitKey(1)
    if key==27:
        break
    elif key==ord('x'):
        print('You have been printing X')
cam.release()
cv2.destroyAllWindows()






