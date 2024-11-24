# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:03:21 2024

@author: ocamp
"""
import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    cv2.imshow("image", img)
    cv2.waitkey(1)