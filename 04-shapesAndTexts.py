# Shapes and Texts

import cv2
import numpy as np
print("Package Imported")

img = np.zeros((512, 512, 3), np.uint8)             # matrix of 0 (black)
# img[:] = 255, 0, 0                                 # change all the pixels in the matrix to blue   

cv2.line(img, (0,0), (300,300), (0,255,0), 3)                           # draw a line (image, starting point, ending point(user defined), colour, thickness)
# cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)         # draw a line (image, starting point, ending point, colour, thickness)
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 3)                      # draw a rectangle (image, starting point, ending point(user defined), colour, thickness)
# cv2.rectangle(img, (0,0), (250,350), (0,0,255), cv2.FILLED)             # draw a rectangle (image, starting point, ending point(user defined), colour, filled)
cv2.circle(img, (400, 50), 30, (255, 0, 0), 3)                          # draw a circle (image, centre point, radius(user defined), colour, thickness)
cv2.putText(img, "OPENCV", (300,100), cv2.FONT_ITALIC, 1, (0,250,0), 1) # insert text (image, text, position, font, scale, colour, thickness)

cv2.imshow("Image", img)
cv2.waitKey(0)