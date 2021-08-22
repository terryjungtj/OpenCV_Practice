# Document Scanner

widthImg = 720
heightImg = 1000

import cv2
import time
import numpy as np
print("Package Imported")



# Read Video
cap = cv2.VideoCapture("Resources/DocumentPortrait.mp4")

# Find the best technique to recognise the edges of the document
def preProcessing(img):
    kernel = np.ones((5,5))
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 # convert to grayscale
    imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)                    # blur an image
    imgCanny = cv2.Canny(img, 200, 200)                             # convert to binary image with edges 
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)       # dialate the edges
    imgEroded = cv2.erode(imgDialation, kernel, iterations=1)       # erode the edges
    return imgEroded


# gets the contours of a shape  
def getContours(img):
    biggestContour = np.array([])
    maxArea = 0

    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)       # (image, retreival method(retreives the extreme outer contours), request for all the contours)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>5000:                                                                            # simple threshold to avoid noise
            # cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)                                 # draw a contour (imgae, contour, contour index, colour, thickness)
            perim = cv2.arcLength(cnt, True)                                                    # gets the lengths of the contour (to determine the no of corners)
            # print(perim)
            approx = cv2.approxPolyDP(cnt, 0.02*perim, True)                                    # approximate the numer of corners (contours, resolution, whether the shape is closed or open)
            
            if area > maxArea and len(approx) == 4:
                biggestContour = approx
                maxArea = area

            # print(len(approx))
            # objCor = len(approx)                                                                # create object corner 
            # x, y, w, h = cv2.boundingRect(approx)   

    cv2.drawContours(imgContour, biggestContour, -1, (255, 0, 0), 20)
    return biggestContour

def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    print ("Current Points", myPoints)

    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    print ("Sum", add)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)

    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    print("New Points", myPointsNew)

    return myPointsNew


# gets warped perspective
def getWarp(img, biggestContour):
    biggestContour = reorder(biggestContour)
    pts1 = np.float32(biggestContour)                                                   # define the four corners as a coordinate
    pts2 = np.float32([[0,0], [widthImg,0], [0,heightImg], [widthImg, heightImg]])      # define the four corresponding coordinates (top left, top right, bottom left, bottom right)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)                                    # obtain the transformation matrix
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))                 # obtain the warped image based on the matrix

    imgCropped = imgOutput[20:imgOutput.shape[0]-20, 20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))

    return imgCropped


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


while True:
    success, img = cap.read()
    img = cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    
    biggestContour = getContours(imgThres)
    # print(biggestContour)
    if biggestContour.size != 0:
        imgWarped = getWarp(img, biggestContour)
        imgArray = ([img, imgThres], [imgContour, imgWarped])
    else:
        imgArray = ([img, imgThres], [img, img])
    
    imgStacked = stackImages(0.6, imgArray)
    cv2.imshow("Output", imgStacked)

    # time.sleep(0.05)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

