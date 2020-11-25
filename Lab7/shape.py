#!/bin/python
import cv2
cam = cv2.VideoCapture(0)
while (True):# 打开摄像头
    ret , frame = cam.read() # 获取摄像头数据
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # 色彩变换
    blur = cv2.blur(grey,(5,5)) # 过滤噪声
    circles = cv2.HoughCircles(blur,method=cv2.HOUGH_GRADIENT,dp=1,minDist=200, param1=100,param2=33,minRadius=30,maxRadius=175)# 识别圆形
    if circles is not None: # 识别到圆形
        for i in circles [:]: # 画出识别的结果
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            cv2.imshow('Detected',frame) # 显示识别图像
            if cv2.waitKey(1) == ord("q"):
                break
cv2.destroyAllWindows() # 关闭窗口
cam.release() # 释放摄像头