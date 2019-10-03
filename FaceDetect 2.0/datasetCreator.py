import numpy as np
import cv2
import sqlite3
face_cascade = cv2.CascadeClassifier('//home//xander999//Desktop//haar-cascade-files-master//haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)
def inputorUpdate(id,name,age,gender):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM PEOPLE WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    isrec=0
    for row in cursor:
        isrec=1
    if(isrec==1):
        cmd="UPDATE PEOPLE SET NAME="+str(name)+", AGE="+str(age)+", GENDER="+str(gender)+" WHERE ID="+str(id)
    else:
        cmd="INSERT INTO PEOPLE(ID,NAME,AGE,GENDER) VALUES("+str(id)+","+str(name)+","+str(age)+","+str(gender)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    
id=input('enter user id :')
name=input('enter user name:')
age=input('enter user age :')
gender=input('enter user gender :')

inputorUpdate(id,name,age,gender)
sampleNum=0
while(True):
    tf, frame=cam.read()
    #cv2.imshow('SingleFrame',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1
        print(sampleNum)
        cv2.imwrite("dataset//User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h, x:x+w])
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('AnotherFrame',frame)
    key=cv2.waitKey(1)
    if key==27:
        break
    elif key==ord('x'):
        print('You have been printing X')
cam.release()
cv2.destroyAllWindows()






