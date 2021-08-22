# Read Images/Videos/Webcam

import cv2
print("Package Imported")


# Functions
# Read Image
def readImage():
    img = cv2.imread("OpenCV_Practice/Resources/IU.jpg")    # change directory accordingly

    cv2.imshow("Output", img)
    cv2.waitKey(0)

# Read Video
def readVideo():
    cap = cv2.VideoCapture("Resources/PowerSupply.mp4")     # change directory accordingly
    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Read Webcam
def readWebcam():
    cap = cv2.VideoCapture(0)           # 0 is default webcam
    cap.set(3,640)                      # id no.3 = width
    cap.set(4,480)                      # id no.4 = height
    cap.set(10,100)                     # id no.10 = brightness

    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Main
if __name__ == '__main__':
    options = {0: readImage,            # store the functions in an array
               1: readVideo,
               2: readWebcam,}

    options[0]()                        # change the index number to call the desired function