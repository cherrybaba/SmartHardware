#!/bin/python
import cv2
cam = cv2.VideoCapture(0)
x=0
y=0
r=0
preX=0
preY=0
preZ=0
flag=0
while (True):# 打开摄像头
    #global x,y,flag
    ret , frame = cam.read() # 获取摄像头数据
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # 色彩变换
    blur = cv2.blur(grey,(5,5)) # 过滤噪声
    circles = cv2.HoughCircles(blur,method=cv2.HOUGH_GRADIENT,dp=1,minDist=200, param1=100,param2=33,minRadius=30,maxRadius=175)# 识别圆形
    if circles is not None: # 识别到圆形
        for j in circles [:]: # 画出识别的结果
            tmpX=x 
            tmpY=y
            tmpR=r
            distance=(x-j[0][0])*(x-j[0][0])+(y-j[0][1])*(y-j[0][1])
            deltaR=abs(r-j[0][2])
            x=j[0][0]
            y=j[0][1]
            r=j[0][2]
            for i in j[:]:
                if flag==0:
                    flag=1
                    x=i[0]
                    y=i[1]
                    r=i[2]
                    break
                if (tmpX-i[0])*(tmpX-i[0])+(tmpY-i[1])*(tmpY-i[1])+abs(tmpR-i[2])<distance+deltaR:
                    distance=(tmpX-i[0])*(tmpX-i[0])+(tmpY-i[1])*(tmpY-i[1])
                    deltaR=abs(tmpR-i[2])
                    x=i[0]
                    y=i[1]
                    r=i[2]
            
            cv2.circle(frame,(x,y),r,(0,255,0),2)
            cv2.circle(frame,(x,y),2,(0,0,255),3)
            cv2.imshow('Detected',frame) # 显示识别图像
            if cv2.waitKey(1) == ord("q"):
                    break
cv2.destroyAllWindows() # 关闭窗口
cam.release() # 释放摄像头