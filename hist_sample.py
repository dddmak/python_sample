#!/usr/bin/env python

#author:makino
#date:20181108

import cv2
import numpy as np
import glob
import subprocess
import sys
import os
import time
import datetime
from matplotlib import pyplot as plt

path_back =  '/home/sanlab/catkin_ws/src/rd_tomato/src/image/test.png'
path_check = '/home/sanlab/catkin_ws/src/rd_tomato/src/image/video/check'
path_src = '/home/sanlab/catkin_ws/src/rd_tomato/src'
img_back = cv2.imread(path_back)
hsv = cv2.cvtColor(img_back,cv2.COLOR_BGR2HSV)
color = ('r','g','b')
for i,col in enumerate(color):
    histr = cv2.calcHist([hsv],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    #print(histr[90])
plt.show()

