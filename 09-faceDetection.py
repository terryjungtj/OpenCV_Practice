# Face Detection

import cv2
import numpy as np
print("Package Imported")

cascadePath = 'Resources/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)

imagePath = 'Resources/IU.jpg'
img = cv2.imread(imagePath)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)       #find the faces (image, scale factor, minimum neighbours)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w,y+h), (255,0,0), 2)     # draw a rectangle on the image

cv2.imshow("Image", img)
cv2.waitKey(0)
