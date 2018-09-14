# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 23:27:38 2018

@author: Avis_King
"""

import numpy as np
import time
import cv2

cap = cv2.VideoCapture(0) #since 1st webcam is recording its 0
print("Press q or ctrl+c to quit")

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()