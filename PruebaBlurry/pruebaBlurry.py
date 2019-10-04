# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

#%%
imgSB=cv2.imread(r"imagenSinBlurry.jpg", cv2.IMREAD_GRAYSCALE)
imgCB=cv2.imread(r"imagenConBlurry.jpg",cv2.IMREAD_GRAYSCALE)
imgSB = imgSB.T[:,::-1]

# imR=np.reshape(imgSB,-1)
# imgNew=[]
# imgNew.append(imR[len(imR)-1])

# for i in range (1,len(imR)):
#     imgNew.append(imR[len(imR)-i])

# imgSB=np.reshape(imgNew,(1336,2880),-1)

#imgCB = cv2.GaussianBlur(imgSB,(39,39),15)


sep = np.zeros([20,2880])

f = plt.figure()
plt.subplot(1,2,1)
plt.imshow(np.vstack([imgSB, sep, imgCB]),"gray")

import scipy.fftpack as fft

fft1 = np.abs(fft.fftshift( fft.fft2(imgSB)))
fft2 = np.abs(fft.fftshift( fft.fft2(imgCB)))


m = 14000
plt.subplot(1,2,2)
plt.imshow(np.vstack([fft1>m,sep, fft2>m]))


cv2.Laplacian(imgCB,cv2.CV_64F).var()
cv2.Laplacian(imgCB,cv2.CV_64F).var()