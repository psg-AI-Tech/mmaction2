#!/usr/bin/env python3
import cv2

cap = cv2.VideoCapture("../demo/skeleton_demo.mp4")
flag, frame = cap.read()
while flag:
    cv2.imshow("frame",frame)
    key=cv2.waitKey(50)
    flag, frame = cap.read()
# cap.release()
