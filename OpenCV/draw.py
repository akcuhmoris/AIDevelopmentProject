import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')
import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#1. paint the image a certain color

blank[:] = 0,255,0
cv.imshow('Green',blank)

cv.waitKey(0)