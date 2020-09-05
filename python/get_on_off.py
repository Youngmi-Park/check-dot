"""
[braille image process]
원본 이미지

=>밝기 조절
제일 검출이 잘 되는 값: 220

=>이진화
경계값: 150

=>영역 검출
if 성능: 조절후>전 then 조절후 선택
else: 조절전 선택

=>점자 이미지 저장
"""

import cv2 as cv
import numpy as np
import math

img_color=cv.imread(r"C:\test\crop.jpg")

#원본 이미지 rgb값 split하여
#r레이어 g레이어 b레이어의 모든 픽셀의 평균 계산
b, g, r=cv.split(img_color)

bavg=math.ceil(np.mean(b))
gavg=math.ceil(np.mean(g))
ravg=math.ceil(np.mean(r))

#그 세 개의 값으로 rgb레이어의 평균 계산
avg=[bavg, gavg, ravg]
avg=math.ceil(np.mean(avg))
print(avg)

#rgb레이어의 평균 값과 220와의 차이 계산
diff=220-avg

get_img=img_color.copy()
get_img2=get_img.copy()

height=get_img.shape[0]
width=get_img.shape[1]
channels=get_img.shape[2]

#각 레이어에 차이값만큼 밝기 조절
#(만약 220보다 평균적으로 밝은 이미지라면 밝기 감소,
#220보다 평균적으로 어두운 이미지라면 밝기 증가)
for y in range(height):
    for x in range(width):
        for c in range(channels):
            get_img2[y, x, c]=np.clip(get_img[y, x, c]+diff, 0, 255)

cv.imshow("origin", img_color)
cv.waitKey(0)

cv.imshow("get", get_img2)
cv.waitKey(0)

#이미지를 흑백으로 변환
img_gray=cv.cvtColor(get_img2, cv.COLOR_BGR2GRAY)
img_gray2=cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
#경계값을 150으로 이미지 이진화
ret, img_binary=cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
ret2, img_binary2=cv.threshold(img_gray2, 150, 255, cv.THRESH_BINARY)

img_binary = cv.bitwise_not(img_binary)    # 이미지 반전
img_binary2 = cv.bitwise_not(img_binary2)    # 이미지 반전

#컨투어 검출 작업하여 리스트 저장
contours, hierarchy=cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2=cv.findContours(img_binary2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#컨투어된 개수를 비교하여 성능 비교 후 선택
if len(contours)>len(contours2):
    for cnt in contours:
        cv.drawContours(get_img2, [cnt], 0, (0, 0, 0), 2)

    cv.imshow("result", get_img2)
    cv.waitKey(0)

    height = img_color.shape[0]
    width = img_color.shape[1]
    channels = img_color.shape[2]

    # 검출된 컨투어를 빈 이미지에 매핑 후 저장
    layer1 = np.zeros((height, width, channels))
    layer1[:] = (255, 255, 255)
    for cnt in contours:
        cv.drawContours(layer1, [cnt], 0, (0, 0, 0), 2)
    res = layer1[:]
    cv.imwrite(r"C:\test\white.jpg", res)
else:
    for cnt in contours2:
        cv.drawContours(img_color, [cnt], 0, (0, 0, 0), 2)

    cv.imshow("result", img_color)
    cv.waitKey(0)

    height = img_color.shape[0]
    width = img_color.shape[1]
    channels = img_color.shape[2]

    # 검출된 컨투어를 빈 이미지에 매핑 후 저장
    layer1 = np.zeros((height, width, channels))
    layer1[:] = (255, 255, 255)
    for cnt in contours2:
        cv.drawContours(layer1, [cnt], 0, (0, 0, 0), 2)
    res = layer1[:]
    cv.imwrite(r"C:\test\white.jpg", res)


#220이구나
#219
#217
#218
