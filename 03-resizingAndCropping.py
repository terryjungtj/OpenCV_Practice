# Resizing and Cropping

import cv2
import numpy as np
print("Package Imported")

# Resize Image
# img = cv2.imread("Resources/IU.jpg")
# print(img.shape)                        # get image size (height, width, BGR)
# imgResize = cv2.resize(img, (500, 500))
# print(imgResize.shape)     

# cv2.imshow("Image", img)
# cv2.imshow("Resized Image", imgResize)
# cv2.waitKey(0)


# Crop Image
img = cv2.imread("Resources/IU.jpg")
print(img.shape)                        # get image size (height, width, BGR)
imgCropped = img[0:500, 200:500]        # index and extract the matrix (height, width)

cv2.imshow("Image", img)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)