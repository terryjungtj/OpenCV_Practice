# Basic Filters

import cv2
import numpy as np
print("Package Imported")

# Show Image
img = cv2.imread("Resources/IU.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 # convert to grayscale
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)                    # blur an image
imgCanny = cv2.Canny(img, 100, 100)                             # convert to binary image with edges 
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)       # dialate the edges
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)       # erode the edges

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
