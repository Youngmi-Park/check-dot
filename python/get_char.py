#-*-coding: utf-8

#글자수 검출 코드

import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt
import unicodedata

#글자수 저장 리스트
dot_result=[]

img_color=cv.imread(r"C:\test\crop.jpg")

cv.imshow("origin", img_color)
cv.waitKey(0)
y_tri=int(img_color.shape[0]*0.67)
x_tri=int(img_color.shape[1]/y_tri)
print(y_tri)
print(x_tri)

for i in range(x_tri-1):
    i=img_color.copy()
    dot_result.append(i)

size=int(img_color.shape[1]/len(dot_result))
print(size)

xmin=0
xmax=size

for i in range(len(dot_result)):
    dot_result[i]=img_color[0:img_color.shape[0], xmin:xmax]
    if xmax>img_color.shape[1]:
        xmax=img_color.shape[1]
    xmin=xmax
    xmax=xmin+size+1

for i in range(len(dot_result)):
    cv.imshow("word", dot_result[i])
    cv.waitKey(0)
