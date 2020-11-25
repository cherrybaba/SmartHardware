import numpy as np
import cv2
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # 转换颜色空间
    image_mask = cv2.inRange(hsv, np.array([0, 43, 46]), np.array([34, 255, 255]))# 计算输出图像
    output = cv2.bitwise_and(frame, frame, mask=image_mask)
    ret,thresh=cv2.threshold(image_mask,127,255,0)
    im,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #找到事物轮廓
    
    if len(contours)!=0:
        cv2.drawContours(output,contours,-1,255,3) #画出所有事物轮廓
        c=max(contours,key=cv2.contourArea) #选取最大的轮廓为手部轮廓
        x,y,w,h=cv2.boundingRect(c) #确定手部轮廓的起始坐标、长宽
        cv2.circle(output,(x+w/2,y+h/2),2,(0,255,0),3) #在手部中心点画圆标记
    cv2.imshow('Original', frame)
    cv2.imshow('Output', output)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllwindows()
cam.release()
