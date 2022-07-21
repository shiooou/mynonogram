#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:16:55 2022

@author: shiooooou
"""

import cv2
import numpy as np
img = cv2.imread('images/Unknown2.jpeg')
img = cv2.resize(img, (15,15),interpolation=cv2.INTER_AREA)
new_img = np.zeros((15, 15, 3))
bwlist = np.zeros((15,15))

for row in range(15):
    for column in range(15):
        if np.average(img[row][column],weights=(2,1,1))>122:
            #加權平均
            new_img[row][column] = [255, 255, 255]
            bwlist[row][column] = 1
        else:
            new_img[row][column] = [0, 0, 0]
            bwlist[row][column] = 0
print(bwlist)            
            
#直的
r = 0 
for row in range(15):
    if bwlist[row][8] == 1:
        r += 1
        if row == 14 :
            print(r)
    elif r == 0 :
        print('',end='')
    else:
        print(r,end='')
        r = 0
 


#cv2.imshow('img',img)
#cv2.waitKey(0)

