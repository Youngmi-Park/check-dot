import pandas as pd
from sklearn.cluster import DBSCAN
import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

img_color=cv.imread(r"C:\test\4musil.jpg")
dst=img_color.copy()
cv.imshow("origin", img_color)
cv.waitKey(0)

#@@@@@@@@더 좋은 검출 위해 라플라시안과 경계값 변경!
laplacian = cv.Laplacian(img_color, cv.CV_8U)

img_gray2=cv.cvtColor(laplacian, cv.COLOR_BGR2GRAY)
ret2, img_binary2=cv.threshold(img_gray2, 130, 255, cv.THRESH_BINARY)
img_binary2 = cv.bitwise_not(img_binary2)    # 이미지 반전
contours2, hierarchy2=cv.findContours(img_binary2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours2:
    cv.drawContours(img_color, [cnt], 0, (0, 0, 0), 2)

cv.imshow("result", img_color)
cv.waitKey(0)
x=np.array(contours2)

contours22=np.vstack(contours2).squeeze()

#print(contours22)
height=img_color.shape[0]
width=img_color.shape[1]
channels=img_color.shape[2]
radius=((height/8)+(width/8))/2
df=pd.DataFrame(contours22)
model=DBSCAN(eps=radius, min_samples=3)
model.fit(df)
y_predict=model.fit_predict(df)
print(y_predict)

df[2]=y_predict
#print(df)

df=df[df[2]!=-1]
del df[2]
print(df)
tuples = [tuple(x) for x in df.values]
#print(tuples)
for cnt in tuples:
    cv.circle(img_color, cnt, 0, (255, 255, 0), 2)

cv.imshow("result2", img_color)
cv.waitKey(0)

height = img_color.shape[0]
width = img_color.shape[1]
channels = img_color.shape[2]

# 검출된 컨투어를 빈 이미지에 매핑 후 저장
layer1 = np.zeros((height, width, channels))
layer1[:] = (255, 255, 255)
for cnt in tuples:
    cv.circle(layer1, cnt, 0, (0, 0, 0), 2)
res = layer1[:]
cv.imwrite(r"C:\test\white.jpg", res)


#클러스터된 점자로 image trim
#trim 후 영역 검출 위해 5%씩 여백을 남김
xsize=int((np.amax(tuples, axis=0)[0]-np.amin(tuples, axis=0)[0])*0.05)
ysize=int((np.amax(tuples, axis=0)[1]-np.amin(tuples, axis=0)[1])*0.05)
area_avg=int((xsize+ysize)/2)
#trim 계산 값
xmin=int(np.amin(tuples, axis=0)[0]-area_avg if np.amin(tuples, axis=0)[0]-area_avg>0 else 1)
xmax=int(np.amax(tuples, axis=0)[0]+area_avg if np.amax(tuples, axis=0)[0]+area_avg<img_color.shape[1] else img_color.shape[1])
ymin=int(np.amin(tuples, axis=0)[1]-area_avg if np.amin(tuples, axis=0)[1]-area_avg>0 else 1)
ymax=int(np.amax(tuples, axis=0)[1]+area_avg if np.amax(tuples, axis=0)[1]+area_avg<img_color.shape[0] else img_color.shape[0])
print(xmin)
print(xmax)
print(ymin)
print(ymax)
#print(np.amin(tuples, axis=0))     #print(np.amax(tuples, axis=0))

dst=dst[ymin:ymax, xmin:xmax]

cv.imshow("result3", dst)
cv.imwrite(r"C:\test\crop.jpg", dst)
cv.waitKey(0)
