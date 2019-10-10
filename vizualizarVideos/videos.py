# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:46:10 2019

@author: BraianSoullier
"""

import cv2
import numpy as np

cap = cv2.VideoCapture("DJI_0182.mp4")

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
  
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()
