# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:57:53 2019

Codigo para corregir distorción de la camara. Distorciones estilo FISHEYE

@author: BraianSoullier
"""

import cv2
import glob
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt
import scipy.sparse as sparse

#ruta = r"C:/Users/BraianSoullier/Desktop/TAMIUSOULLIER/FAUBA_190904/Code/imgOrig.png"
ruta = "fauba_01.png"
imgOrig = cv2.imread(ruta)
pars = np.load('usbCamPars.npy',allow_pickle=True).item()


#%% Corrigo distorción de imagen con parametros de la camara sacados en del script "calibracion.py"
imgEdit = cv2.undistort(imgOrig,pars['cameraMatrix'],pars['distCoeffs'])
						
plt.figure()
plt.imshow(imgOrig[:,:,::-1])
plt.figure()
plt.imshow(imgEdit[:,:,::-1])

plt.imsave('/home/braso/Documentos/TAMIU/TAMIUSOULLIER/SCRIPS/ClasVerde/fauba_edit.jpg',imgEdit[:,:,::-1])
plt.imsave('/home/braso/Documentos/TAMIU/TAMIUSOULLIER/SCRIPS/ClasVerde/fauba_edit.jpg',imgEdit[:,:,::-1])
