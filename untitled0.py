#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:16:55 2022

@author: shiooooou
"""

import cv2
import numpy as np
img = cv2.imread('images/img2.jpg')
img = cv2.resize(img, (15,15),interpolation=cv2.INTER_AREA)
cv2.imshow('img',img)
cv2.waitKey(0)