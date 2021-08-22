# Contour and Shape Detection

import cv2
import numpy as np
print("Package Imported")

def empty(a):
    pass

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

# gets the contours of a shape
def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)       # (image, retreival method(retreives the extreme outer contours), request for all the contours)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        
        if area>500:                                                                            # simple threshold to avoid noise
            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)                                 # draw a contour (imgae, contour, contour index, colour, thickness)
            perim = cv2.arcLength(cnt, True)                                                    # gets the lengths of the contour (to determine the no of corners)
            print(perim)
            approx = cv2.approxPolyDP(cnt, 0.02*perim, True)                                    # approximate the numer of corners (contours, resolution, whether the shape is closed or open)
            print(len(approx))

            objCor = len(approx)                                                                # create object corner 
            x, y, w, h = cv2.boundingRect(approx)                                               # create a bounding box around the object
            
            # Shape classifications
            if objCor == 3: 
                objectType = "Triangle"
            elif objCor == 4:                                                                   # Since both the square and rectangles have 4 corners, the aspect ratio is calculated to differentiate the two
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio<1.05: 
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"
            
            
            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0), 2)                           # draw a rectangle on the image
            cv2.putText(imgContour, objectType, (x+(w//2)-10,y+(h//2)-10), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,0,0), 2)

path = 'Resources/shapes.png'

img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(img, 50, 50)  
getContours(imgCanny)
 
imgBlank = np.zeros_like(img)           # create a blank image

imgStack = stackImages(0.8, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
cv2.imshow("Stacked Images", imgStack)
cv2.waitKey(0)
