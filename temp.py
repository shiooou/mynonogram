# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2
import os

def read_images(images):
    array_of_images = []
    for filename in os.listdir(r'./'+images):
        img = cv2.imread(images + '/' + filename)
        if img is not None:
            array_of_images.append(img)
        else:
            print("Cannot read file {}".format(images + '/' + filename))
        
    return array_of_images

if __name__ == "__main__":
    
    array_of_images = read_images('images')
    
    for image in array_of_images:
        image = cv2.resize(image, (15,15),interpolation=cv2.INTER_AREA)
        new_image = np.zeros((15, 15, 3))
        
        for row in range(15):
            for column in range(15):
                if np.average(image[row][column],weights=[1,0,0]) >122:
                    #加權平均
                    new_image[row][column] = [255, 255, 255]
                else:
                    new_image[row][column] = [0, 0, 0]
      
   
        #cv2.imshow('original', image)
        #cv2.waitKey(0)
        #cv2.imshow('new',new_image)
        #cv2.waitKey(0)
    #cv2.destroyAllWindows()
        
