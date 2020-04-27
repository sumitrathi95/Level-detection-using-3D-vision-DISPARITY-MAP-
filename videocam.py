import cv2
import numpy as np
from imutils.video import VideoStream
import time

webcam1 = cv2.VideoCapture(0)
time.sleep(2.0)

while(1):
    a, gray1 = webcam1.read()
    #gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    cv2.imshow('LiveWebFeed',a)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
