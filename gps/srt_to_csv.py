#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:11:31 2019

@author: ulises
"""




import pandas as pd
import numpy as np
import glob
from time import time


def srt2csv(path = '/home/braso/Documentos/TAMIU/TAMIUSOULLIER/SCRIPS/gps/str'):
	'''convierte los srt dentro del path en csv'''
	a0 = time()
	srtFiles=glob.glob(path+'**/*.SRT')
	for thisSubtFile in srtFiles:
	
		fil= open(thisSubtFile)
		subt=fil.read().split('\n\n')
	
		df_subt = pd.DataFrame(columns = ['frameNumber','dateTime','lat','lon'])
		for i in range(len(subt)):
			l 			= subt[i].split('[')
			if l[0] != '':
				l0sp 		= l[0].split('\n')
				
				datetime 	= ','.join(l0sp[-2].split(',')[:-1])
				frNum 		= np.int32(l0sp[2].split(':')[1].split(',')[0])
				la 			= l[-2].replace(']','').replace(' ','').split(':')[-1]
				lo 			= l[-1].replace(']','').replace(' ','').split(':')[-1].replace('</font>','')
				df_subt = df_subt.append({'frameNumber':frNum,
								 'dateTime':pd.to_datetime(datetime),
								 'lat':np.float(la),
								 'lon':np.float(lo)},ignore_index=True)
		print('tiempo parcial')
		df_subt.to_csv(thisSubtFile.split('.SRT')[0]+'.csv')
	
	a1 = time()
	
	print('esto tardo: ', a1-a0,' segundos en correr sobre ',len(srtFiles),' subtitulos')
