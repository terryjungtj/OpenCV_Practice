# Virtual Paint

import cv2
import time
import numpy as np
print("Package Imported")

# Read Video
# cap = cv2.VideoCapture("Resources/BluePen.mp4")

# Read Webcam
cap = cv2.VideoCapture(0)           # 0 is default webcam
cap.set(3,640)                      # id no.3 = width
cap.set(4,480)                      # id no.4 = height
cap.set(10,100)                     # id no.10 = brightness

myColours = [[108,128,62,124,255,255]]

myColourValues = [[255,0,0], [0,255,0], [0,0,255]]      #Blue, Gree, Red

myPoints = []   # x, y, colourId

def findColour(img, myColours, myColourValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)            # convert the coloured image to a HSV image
    colourSelect = 0

    newPoints = []
    for colour in myColours:
        # Create a Mask Image
        lower = np.array(colour[0:3])                   # create lower limit
        upper = np.array(colour[3:6])                   # create upper limit
        mask = cv2.inRange(imgHSV,lower,upper)                  # create a mask image (image, lower limit, upper limit)
        x,y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColourValues[colourSelect], cv2.FILLED)
        
        if x!=0 and y!=0:
            newPoints.append([x,y,colourSelect])

        colourSelect += 1
        cv2.imshow(str(colour[0]), mask)
    return newPoints


# gets the contours of a shape
def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)       # (image, retreival method(retreives the extreme outer contours), request for all the contours)
    x,y,w,h = 0,0,0,0 # initial values
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:                                                                            # simple threshold to avoid noise
            cv2.drawContours(imgResult, cnt, -1, (0,255,0), 3)                                 # draw a contour (imgae, contour, contour index, colour, thickness)
            perim = cv2.arcLength(cnt, True)                                                    # gets the lengths of the contour (to determine the no of corners)
            approx = cv2.approxPolyDP(cnt, 0.02*perim, True)                                    # approximate the numer of corners (contours, resolution, whether the shape is closed or open)                                                             # create object corner 
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y        # return the mid point horizontally and the peak vertically

def drawOnCanvas(myPoints, myColourValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColourValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColour(img, myColours, myColourValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColourValues)

    cv2.imshow("Video", imgResult)
    # time.sleep(0.05)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

