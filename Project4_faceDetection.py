# Face Detection

widthImg = 640
heightImg = 480

minArea = 500
count = 0

import cv2
import time
import numpy as np
print("Package Imported")

# imagePath = 'Resources/IU.jpg'
videoPath = 'Resources/High Kick.mp4'
# videoPath = 'Resources/DashCam Owners.mp4'
cascadePath = 'Resources/haarcascades/haarcascade_frontalface_default.xml'

# Read Video
# cap = cv2.VideoCapture(videoPath)

# Read Webcam
cap = cv2.VideoCapture(0)           # 0 is default webcam
cap.set(3,640)                      # id no.3 = width
cap.set(4,480)                      # id no.4 = height
cap.set(10,100)                     # id no.10 = brightness

faceCascade = cv2.CascadeClassifier(cascadePath)



while True:

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)       #find the faces (image, scale factor, minimum neighbours)

    for (x, y, w, h) in faces:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x+w,y+h), (255,0,0), 2)     # draw a rectangle on the image
            cv2.putText(img, "Face", (x, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            imgRegionOfInterest = img[y:y+h, x:x+w]
            cv2.imshow("Region of Interest", imgRegionOfInterest)



    cv2.imshow("Output", img)
    # time.sleep(0.05)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/Face_" + str(count) + ".jpg", imgRegionOfInterest)
        
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150,265), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
      

