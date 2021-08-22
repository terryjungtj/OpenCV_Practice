# Warp Perspective

import cv2
import numpy as np
print("Package Imported")

img = cv2.imread("Resources/card.jpeg")      

width, height = 850,530                                                 # define the size of the card 

pts1 = np.float32([[129, 316], [716, 72], [312, 649], [917, 382]])      # define the four corners as a coordinate
pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])      # define the four corresponding coordinates (top left, top right, bottom left, bottom right)
matrix = cv2.getPerspectiveTransform(pts1, pts2)                        # obtain the transformation matrix
imgOutput = cv2.warpPerspective(img, matrix, (width, height))           # obtain the warped image based on the matrix


cv2.imshow("Image", img)
cv2.imshow("Warped Image", imgOutput)
cv2.waitKey(0)