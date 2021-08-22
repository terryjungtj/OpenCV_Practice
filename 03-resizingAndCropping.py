# Resizing and Cropping

import cv2
import numpy as np
print("Package Imported")

# Functions
# Resize Image
def resizeImage():
    img = cv2.imread("OpenCV_Practice/Resources/IU.jpg")    # change directory accordingly
    print(img.shape)                                        # get image size (height, width, BGR)
    imgResize = cv2.resize(img, (500, 500))
    print(imgResize.shape)     

    cv2.imshow("Image", img)
    cv2.imshow("Resized Image", imgResize)
    cv2.waitKey(0)


# Crop Image
def cropImage():
    img = cv2.imread("OpenCV_Practice/Resources/IU.jpg")    # change directory accordingly
    print(img.shape)                                        # get image size (height, width, BGR)
    imgCropped = img[0:500, 200:500]                        # index and extract the matrix (height, width)

    cv2.imshow("Image", img)
    cv2.imshow("Cropped Image", imgCropped)
    cv2.waitKey(0)


# Main
if __name__ == '__main__':
    options = {0: resizeImage,            # store the functions in an array
               1: cropImage}

    options[1]()                        # change the index number to call the desired function