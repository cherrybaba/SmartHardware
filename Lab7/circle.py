import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([180, 255, 46]))
    
    circles = cv2.HoughCircles(mask, method=cv2.HOUGH_GRADIENT, dp=1, minDist=200, param1=100, param2=33, minRadius=0)
    
    if circles is not None:
    #在多个圆中确定中心的一个圆
        s = a = cnt = 0
        for i in circles[0, :]:
            s+=i[0]
            cnt+=1
        d = 100
        s/=cnt
        cnt=0
        for i in circles[0, :]:
            if abs(s - i[0])<d:
                d=abs(s-i[0])
                a=cnt
            cnt+=1
        cnt = 0
        for i in circles[0, :]:
            if cnt==a:
                cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(frame, (i[0], i[1]), 2, (0, 255, 0), 3)
            cnt+=1
    cv2.imshow('Detected', frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllwindows()
cam.release()
