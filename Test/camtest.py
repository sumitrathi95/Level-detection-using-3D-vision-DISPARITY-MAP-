import numpy as np
import cv2


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("output", img)

    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()
