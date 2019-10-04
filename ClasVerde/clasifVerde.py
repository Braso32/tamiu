# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:04:08 2019

@author: BraianSoullier
"""


import cv2
import glob
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt

# ruta = r"C:\Users\BraianSoullier\Desktop\TAMIUSOULLIER\SCRIPS\ClasVerde\imgEdit.jpg"
ruta = "fauba_edit.jpg"
imgT = cv2.imread(ruta)

# %% Color verde en RGB

ch1,ch2,ch3=imgT.T
imgNew=(2*np.int32(ch2)-np.int32(ch1)-np.int32(ch3))
imgNew=imgNew


plt.figure()
plt.title('Imagen intensidad verde')
plt.imshow(imgNew.T)

plt.figure()
plt.title('Imagen en RGB')
plt.imshow(imgT[:,:,::-1])
#%% Seleccionar donde hay cultivo CRECIDO

plt.figure()
plt.imshow(imgNew.T)
print('esquina 1:\t',end=' ')
y1,x1=np.array(np.round(plt.ginput()[0]),dtype=np.int32)
print('esquina 1:\t',end=' ')
y2,x2=np.array(np.round(plt.ginput()[0]),dtype=np.int32)

recorte=imgNew.T[x1:x2,y1:y2]

recorte = np.uint8(255*(recorte-recorte.min()) / (recorte.max()-recorte.min()))
plt.figure()
plt.imshow(recorte)

#%% Una vez recortado busco Bordes CRECIDO


clahe = cv2.createCLAHE(clipLimit=3,tileGridSize=(35,60))
recorteN =clahe.apply(recorte)
plt.imshow(np.hstack([recorte,recorteN]))
#plt.hist(recorte.reshape(-1),50)
#RET,imgB=cv2.threshold(recorteN,130,255,0)
RET,imgB=cv2.threshold(recorteN,0,255,cv2.THRESH_OTSU)
#kernel=cv2.getStructuringElement(	cv2.MORPH_ELLIPSE,(16,16))
#imgB=cv2.morphologyEx(imgB,cv2.MORPH_OPEN,kernel)
imgB=cv2.morphologyEx(imgB,cv2.MORPH_ERODE,np.ones([4,4],dtype=np.uint8))
imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.fillPoly(imgB,cnt,255)
cv2.drawContours(imgB,cnt,-1,(127,0,0))
plt.figure()
plt.imshow(imgB)

#%%
res=[]

for i in cnt:
	rect=cv2.minAreaRect(i)
	res.append([*rect[0], *rect[1], rect[2]])
	box = cv2.boxPoints(rect) # cv2.boxPoints(rect) for OpenCV 3.x
	box = np.int0(box)
	cv2.fillPoly(imgB,[box],255)
	#cv2.drawContours(imgB,[box],0,(0,0,255),2)]



plt.figure()
plt.imshow(imgB)


# %%
res = np.array(res)

alfa = res.T[-1]
width = res.T[2]
height= res.T[3]
plt.figure('alpha_v_Width')
plt.scatter(alfa,width,alpha=0.4)
plt.figure('height_v_width')
plt.scatter(height,width,alpha=0.4)

# plt.figure('alpha')
# plt.hist(alfa,50)
# plt.figure('w')
# plt.hist(width,50)
# plt.figure('h')
# plt.hist(height,50)
#%%
plt.figure('ar')
ar = width / height
ar = np.array([1/a if a>1 else a for a in ar  ])

plt.hist(ar,50)

#%%


# #%% Seleccionar donde hay cultivo en CRECIMIENTO

# plt.figure()
# plt.imshow(imgT)
# print('esquina 1:\t',end=' ')
# y1,x1=np.array(np.round(plt.ginput()[0]),dtype=np.int32)
# print('esquina 1:\t',end=' ')
# y2,x2=np.array(np.round(plt.ginput()[0]),dtype=np.int32)

# recorte=imgT[x1:x2,y1:y2]

# plt.figure()
# plt.imshow(recorte)

# #%% Una vez recortado busco Bordes EN CRECIMIENTO

# imgB=cv2.cvtColor(recorte,cv2.COLOR_RGB2GRAY)
# RET,imgB=cv2.threshold(imgB,95,255,0)

# imgB=cv2.morphologyEx(imgB,cv2.MORPH_OPEN,np.ones([10,10],dtype=np.uint8))
# #imgB=cv2.morphologyEx(imgB,cv2.MORPH_ERODE,np.ones([2,2],dtype=np.uint8))
# imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(imgB,cnt,-1,(127,0,0))
# x,y,ancho,alto=cv2.boundingRect(cnt[0])
# _,[altoR,anchoR], _=cv2.minAreaRect(cnt[0])

# plt.figure()
# plt.imshow(imgB)
