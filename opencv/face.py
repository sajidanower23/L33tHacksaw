import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('opencv-3.2.0/data/haarcascades_cuda/haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier('opencv-3.2.0/data/haarcascades_cuda/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

num = 0

while(True):

    ret, img = cap.read()
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            num += 1
            print(num)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25)
            )

        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
            
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()
