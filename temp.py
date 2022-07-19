# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2
import os

x
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
        cv2.imshow("filename",image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
        