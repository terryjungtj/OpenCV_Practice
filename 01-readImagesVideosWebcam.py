# Read Images/Videos/Webcam

import cv2
print("Package Imported")

# # Read Image
# img = cv2.imread("Resources/IU.jpg")

# cv2.imshow("Output", img)
# cv2.waitKey(0)

# # Read Video
# cap = cv2.VideoCapture("Resources/PowerSupply.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Read Webcam
cap = cv2.VideoCapture(0)           # 0 is default webcam
cap.set(3,640)                      # id no.3 = width
cap.set(4,480)                      # id no.4 = height
cap.set(10,100)                     # id no.10 = brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break