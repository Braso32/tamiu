#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:45:26 2019

@author: braso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%

path="/home/braso/Documentos/TAMIU/TAMIUSOULLIER/SCRIPS/FloodAlgorim"
#file= "/campoCortado.jpg"
#file= "/frame4.jpg"
file="/indexGreen.jpg"
#file="/santiago.jpg"

img=cv2.imread(path+file, cv2.IMREAD_GRAYSCALE)
#recorte=cv2.imread(path+file)
plt.figure()
plt.imshow(img)
#
#recorte = np.uint8(255*(recorte-recorte.min()) / (recorte.max()-recorte.min()))
#
#clahe = cv2.createCLAHE(clipLimit=3,tileGridSize=(35,60))
#recorteN =clahe.apply(recorte)
#plt.imshow(np.hstack([recorte,recorteN]))


ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_OTSU)

plt.figure('Campo de cultivo')
plt.imshow(thresh,'gray')

## noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

# sure background area
sure_bg = cv2.dilate(thresh,kernel,iterations=0)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

img=cv2.imread(path+file)

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

plt.figure()
plt.imshow(img)

plt.figure()
plt.imshow(markers)
