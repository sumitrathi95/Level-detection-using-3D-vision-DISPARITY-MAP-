import numpy as np
import cv2
import math
import pyttsx

from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, img = cap.read()
    if img is None:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 120)
    lines = cv2.HoughLinesP(edges, 1, math.pi/1, 20, None, 2, 480);


    dot1 = (lines[0][0][0],lines[0][0][1])
    dot2 = (lines[0][0][2],lines[0][0][3])
    cv2.line(img, dot1, dot2, (255,0,0), 3)
    line1 =cv2.line(img,(0,40),(640,40),(255,255,255),4)
    line4 =cv2.line(img,(0,120),(640,120),(255,255,255),4)
    line2 =cv2.line(img,(0,240),(640,240),(255,255,255),4)
    line3 =cv2.line(img,(0,360),(640,360),(255,255,255),4)
    cv2.imshow("output", img)
    length = lines[0][0][1] - lines[0][0][3]

    if length >= 500 :
        engine = pyttsx.init()
        engine.setProperty('rate', 125)
        voices = engine.getProperty('voices')
        engine.say("Garbage filled 90 Percent")
        engine.runAndWait()
        client = TwilioRestClient(account_sid, auth_token)
        my_msg = ("Welcome \nSmart Garbage Collection System \nGarbage Level:50%", length)
        message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
        print('Garbag Filled 90')
            
    print (length)

    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()
