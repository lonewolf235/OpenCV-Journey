import cv2
import time
##This code for streaming video from webcam using Opencv
cam=cv2.VideoCapture(0)
time.sleep(1)
while True:
    _,img=cam.read()
    cv2.imshow("camerafeed",img)
    key = cv2.waitKey(1) & 0xFF
    if(key==ord("q")):
        break
cam.release()
cv2.destroyAllWindows()