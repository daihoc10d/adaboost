import numpy as np
import cv2
face_cascade =cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_eye.xml")
img = cv2.imread('ABC.jpg')
img2 = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.5, 5)
for (x,y,w,h) in faces:
    img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img2[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3)
    for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('ABC',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()