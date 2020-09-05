#-*- coding:utf-8 -*-

# braille 점자
braille={0:' ', 1:'⠁', 2:'⠂', 3:'⠃', 4:'⠄', 5:'⠅', 6:'⠆', 7:'⠇', 8:'⠈', 9:'⠉', 10:'⠊',
         11:'⠋', 12:'⠌', 13:'⠍', 14:'⠎', 15:'⠏', 16:'⠐', 17:'⠑', 18:'⠒', 19:'⠓', 20:'⠔',
         21:'⠕', 22:'⠖', 23:'⠗', 24:'⠘', 25:'⠙', 26:'⠚', 27:'⠛', 28:'⠜', 29:'⠝', 30:'⠞',
         31:'⠟', 32:'⠠', 33:'⠡', 34:'⠢', 35:'⠣', 36:'⠤', 37:'⠥', 38:'⠦', 39:'⠧', 40:'⠨',
         41:'⠩', 42:'⠪', 43:'⠫', 44:'⠬', 45:'⠭', 46:'⠮', 47:'⠯', 48:'⠰', 49:'⠱', 50:'⠲',
         51:'⠳', 52:'⠴', 53:'⠵', 54:'⠶', 55:'⠷', 56:'⠸', 57:'⠹', 58:'⠺', 59:'⠻', 60:'⠼',
         61:'⠽', 62:'⠾', 63:'⠿'}
# vow 중성(Vowel)
vow={35:'ㅏ', 28:'ㅑ', 14:'ㅓ', 49:'ㅕ', 37:'ㅗ', 44:'ㅛ', 13:'ㅜ', 41:'ㅠ', 42:'ㅡ', 21:'ㅣ', 58:'ㅢ', 29:'ㅔ', 23:'ㅐ',
     12:'ㅖ', 39:'ㅘ', 15:'ㅝ', 61:'ㅚ'}
# con 초성(Consonant)
con={8:'ㄱ', 9:'ㄴ', 10:'ㄷ', 16:'ㄹ', 17:'ㅁ', 24:'ㅂ', 32:'ㅅ', 40:'ㅈ', 48:'ㅊ', 11:'ㅋ', 19:'ㅌ', 25:'ㅍ', 26:'ㅎ'}
# con_abb 초성 약자
con_abb={9:'나', 10:'다', 17:'마', 24:'바', 40:'자', 11:'카', 19:'타', 25:'파',  26:'하'}
# con_last 종성(last Consonant)
con_last={1:'ㄱ', 18:'ㄴ', 20:'ㄷ', 2:'ㄹ', 34:'ㅁ', 3:'ㅂ', 4:'ㅅ', 54:'ㅇ', 5:'ㅈ', 6:'ㅊ', 22:'ㅋ', 38:'ㅌ', 50:'ㅍ', 52:'ㅎ', 12:'ㅆ'}
# abb 약자(Abbreviation)
abb={57:'억', 62:'언', 30:'얼', 33:'연',  51:'열', 59:'영', 45:'옥', 55:'온', 63:'옹', 27:'운', 47:'울', 53:'은', 31:'인', 46:'을'}
# abb_exc 예외약자(가,사)
abb_exc={43:'가', 7:'사'}
# conjun 약어(접속사 conjunction)
conjun={14: '그래서', 9:'그러나', 18:'그러면', 34:'그러므로', 29:'그런데', 37:'그리고'}
# fortis_sign 된소리표
fortis_sign={32:'fortis'}
# fortis_con 된소리 초성(Fortis)
fortis_con={8:'ㄲ', 10:'ㄸ', 24:'ㅃ', 32:'ㅆ', 40:'ㅉ'}
# fortis_last 된소리 종성(Fortis)
fortis_last={1: 'ㄲ'}
# num_sign 수표
num_sign={60:'num_sign'}
# num 숫자(Number)
num={1:'1', 3:'2', 9:'3', 25:'4', 17:'5', 11:'6', 27:'7', 19:'8', 10:'9', 26:'0'}
# pun 문장부호(Punctuation)
pun={36:'-', 34:'+', 33:'*', 20:'-', 12:'/', 18:'='}
# {50:'.', 38:'?', 22:'!', 16:','} /는 12+12, =는 18+18
# eng_sign 영어 시작/끝 표기
eng_sign={52:'eng_start', 50:'eng_end'}
# eng_cap 영어대문자표
eng_cap={32:'capital'}
# eng 영어(English)
eng={1:'a', 3:'b', 9:'c', 25:'d', 17:'e', 11:'f', 27:'g', 19:'h', 10:'i', 26:'j', 5:'k', 7:'l', 13:'m', 29:'n',
     21:'o', 15:'p', 31:'q', 23:'r', 14:'s', 30:'t', 37:'u', 39:'v', 58:'w', 45:'x', 61:'y', 53:'z'}
eng2={1:'A', 3:'B', 9:'C', 25:'D', 17:'E', 11:'F', 27:'G', 19:'H', 10:'I', 26:'J', 5:'K', 7:'L', 13:'M', 29:'N',
     21:'O', 15:'P', 31:'Q', 23:'R', 14:'S', 30:'T', 37:'U', 39:'V', 58:'W', 45:'X', 61:'Y', 53:'Z'}
#겹받침 ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ
# attach_sign 36붙임표
attach_sign={36:'attach'}
# full_sign 온표(종성자체)
full_sign={63:'full'}
# blank 빈칸
blank={0:' '}
# thing 것(56+14)
thing={56:'것'}

import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt
import unicodedata
import pandas as pd
from sklearn.cluster import DBSCAN
from requests import get  # to make GET request
import requests

import os
import sys
import urllib.request
import hgtk

#서버에서 이미지를 얻을 때까지 반복
#서버에 이미지가 생기면 php에서 이미지 이름 제공받아 while 탈출
while True:
    #print("file search....")
    url = 'http://localhost/file_print.php'
    r = requests.post(url)
    name = r.text
    if name:
        #print("file got it!")
        break

#서버에서 받은 이미지 이름으로 파일 다운로드
url = "http://localhost/img/"+name
#print(url)

temp = urllib.request.urlopen(url)
oriImage = np.asarray(bytearray(temp.read()), dtype="uint8")

#다운로드 후 서버의 이미지 삭제
del_img='http://localhost/delimg.php'
r2 = requests.post(del_img)
#다운받은 이미지 opencv로 처리


#----------트리밍----------#
#img_color=원본 이미지
img_color=cv.imdecode(oriImage, cv.IMREAD_COLOR)

#속도 문제로 image resize
height = int(img_color.shape[0]*0.3)
width = int(img_color.shape[1]*0.3)
img_color=cv.resize(img_color, dsize=(width, height), interpolation=cv.INTER_AREA)
#################
#원본 이미지 rgb값 split하여
#r레이어 g레이어 b레이어의 모든 픽셀의 평균 계산
b, g, r=cv.split(img_color)

bavg=math.ceil(np.mean(b))
gavg=math.ceil(np.mean(g))
ravg=math.ceil(np.mean(r))

#그 세 개의 값으로 rgb레이어의 평균 계산
avg=[bavg, gavg, ravg]
avg=math.ceil(np.mean(avg))
#print(avg)

#rgb레이어의 평균 값과 130와의 차이 계산
diff=130-avg

get_img=img_color.copy()
get_img2=get_img.copy()

height=get_img.shape[0]
width=get_img.shape[1]
channels=get_img.shape[2]

#각 레이어에 차이값만큼 밝기 조절
#(만약 130보다 평균적으로 밝은 이미지라면 밝기 감소,
#220보다 평균적으로 어두운 이미지라면 밝기 증가)
for y in range(height):
    for x in range(width):
        for c in range(channels):
            get_img2[y, x, c]=np.clip(get_img[y, x, c]+diff, 0, 255)
img_color=get_img2.copy()
####################
#점자는 빛이 위에서 아래로, 그림자가 밑으로 지는 경우가 많으므로 sobely가 유리
sobely=cv.Sobel(img_color, cv.CV_8U, 0, 1, ksize=3)
img_gray2=cv.cvtColor(sobely, cv.COLOR_BGR2GRAY)

ret2, img_binary2=cv.threshold(img_gray2, 140, 255, cv.THRESH_BINARY)
img_binary2 = cv.bitwise_not(img_binary2)    # 이미지 반전
#cv.imshow("g", img_binary2)
#cv.waitKey(0)
contours2, hierarchy2=cv.findContours(img_binary2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours2:
    cv.drawContours(img_color, [cnt], 0, (0, 0, 0), 1)

#cv.imshow("gg", img_color)
#cv.waitKey(0)
x=np.array(contours2)

contours22=np.vstack(contours2).squeeze()

height=img_color.shape[0]
width=img_color.shape[1]
channels=img_color.shape[2]
radius=((height/8)+(width/8))/2
df=pd.DataFrame(contours22)
model=DBSCAN(eps=radius, min_samples=3)
model.fit(df)
y_predict=model.fit_predict(df)

df[2]=y_predict

df=df[df[2]!=-1]
del df[2]

tuples = [tuple(x) for x in df.values]
'''
for cnt in tuples:
    cv.line(img_color, cnt, cnt, (255, 255, 0), 1)
'''
height = img_color.shape[0]
width = img_color.shape[1]
channels = img_color.shape[2]

# 검출된 컨투어를 빈 이미지에 매핑 후 저장
layer1 = np.zeros((height, width, channels))
layer1[:] = (255, 255, 255)
for cnt in tuples:
    cv.circle(layer1, cnt, 0, (0, 0, 0), 3)
res = layer1[:]

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

res=res[ymin:ymax, xmin:xmax]
cv.imwrite(r"C:\test\white.jpg", res)

#----------글자수 슬라이싱----------#
#글자수 저장 리스트
dot_result=[]

img_slice=res.copy()

y_tri=int(img_slice.shape[0]*0.67)
x_tri=int(img_slice.shape[1]/y_tri)

count=[]
for x in range(x_tri):
    count.append(x)

size=int(img_slice.shape[1]/len(count))
xmin=0
xmax=size
i2=0
j2 = img_slice.copy()

while True:
    dot_result.append(j2)
    if xmin>=img_slice.shape[1]:
        xmin=xmin-size
    if xmax>=img_slice.shape[1]:
        xmax = img_slice.shape[1]
        xmin=xmax-size
        dot_result[i2] = img_slice[0:img_slice.shape[0], xmin:xmax]
        i2 += 1
        break
    dot_result[i2] = img_slice[0:img_slice.shape[0], xmin:xmax]
    xmin=xmax+1
    xmax=xmin+size+1
    i2+=1

#----------코드 인식----------#
full_code=[]

for nums in range(i2):
     one_code=[]
     code_img=[]
     img_copy=img_slice.copy()
     #6칸 이미지 생성
     for k in range(6):
          code_img.append(img_copy)

     y_tri=int(dot_result[nums].shape[0]/3)
     x_tri=int(dot_result[nums].shape[1]/2)

     code_img[0]=dot_result[nums][0:y_tri, 0:x_tri]
     code_img[1]=dot_result[nums][y_tri:y_tri+y_tri+1, 0:x_tri]
     code_img[2]=dot_result[nums][y_tri+y_tri+1:dot_result[0].shape[0], 0:x_tri]
     code_img[3]=dot_result[nums][0:y_tri, x_tri:dot_result[0].shape[1]]
     code_img[4]=dot_result[nums][y_tri:y_tri+y_tri+1, x_tri:dot_result[0].shape[1]]
     code_img[5]=dot_result[nums][y_tri+y_tri+1:dot_result[0].shape[0], x_tri:dot_result[0].shape[1]]

     #cv.imshow("result", dot_result[nums])
     #cv.waitKey(0)

     #이미지 rgb값 split하여
     #r레이어 g레이어 b레이어의 모든 픽셀의 평균 계산
     b0, g0, r0=cv.split(code_img[0])
     b1, g1, r1=cv.split(code_img[1])
     b2, g2, r2=cv.split(code_img[2])
     b3, g3, r3=cv.split(code_img[3])
     b4, g4, r4=cv.split(code_img[4])
     b5, g5, r5=cv.split(code_img[5])

     bavg0=math.ceil(np.mean(b0))
     gavg0=math.ceil(np.mean(g0))
     ravg0=math.ceil(np.mean(r0))

     bavg1=math.ceil(np.mean(b1))
     gavg1=math.ceil(np.mean(g1))
     ravg1=math.ceil(np.mean(r1))

     bavg2=math.ceil(np.mean(b2))
     gavg2=math.ceil(np.mean(g2))
     ravg2=math.ceil(np.mean(r2))

     bavg3=math.ceil(np.mean(b3))
     gavg3=math.ceil(np.mean(g3))
     ravg3=math.ceil(np.mean(r3))

     bavg4=math.ceil(np.mean(b4))
     gavg4=math.ceil(np.mean(g4))
     ravg4=math.ceil(np.mean(r4))

     bavg5=math.ceil(np.mean(b5))
     gavg5=math.ceil(np.mean(g5))
     ravg5=math.ceil(np.mean(r5))

     #그 세 개의 값으로 rgb레이어의 평균 계산
     avg0=[bavg0, gavg0, ravg0]
     avg1=[bavg1, gavg1, ravg1]
     avg2=[bavg2, gavg2, ravg2]
     avg3=[bavg3, gavg3, ravg3]
     avg4=[bavg4, gavg4, ravg4]
     avg5=[bavg5, gavg5, ravg5]

     avg0=math.ceil(np.mean(avg0))
     avg1=math.ceil(np.mean(avg1))
     avg2=math.ceil(np.mean(avg2))
     avg3=math.ceil(np.mean(avg3))
     avg4=math.ceil(np.mean(avg4))
     avg5=math.ceil(np.mean(avg5))
     #이미지들 실험하면서 민감도 차차 수정해나가기@@@@@@
     if avg0<230:
         one_code.append(1)
     else:
         one_code.append(0)

     if avg1<230:
         one_code.append(1)
     else:
         one_code.append(0)

     if avg2<230:
         one_code.append(1)
     else:
         one_code.append(0)

     if avg3<230:
         one_code.append(1)
     else:
         one_code.append(0)

     if avg4<230:
         one_code.append(1)
     else:
         one_code.append(0)

     if avg5<230:
         one_code.append(1)
     else:
         one_code.append(0)

     #print(one_code)

     decimal=(one_code[0]*1)+(one_code[1]*2)+(one_code[2]*4)+(one_code[3]*8)+(one_code[4]*16)+(one_code[5]*32)
     full_code.append(decimal)

braille_list=[]
for code in full_code:
    braille_list.append(braille[code])
braille_result = "".join(braille_list)
print(braille_result)

# 출력 리스트
trans_code = []
i=0
j=0
fortis = False
nofortis = False

# 온표검사
yesfull = 0
if (full_code.count(63)):
    j = full_code.index(63)
    # 인덱스 에러 방지
    if (j + 1 >= len(full_code)):
        pass
    elif (full_code[j + 1] in con):
        yesfull=True

#----------번역시작----------#
while (i < len(full_code)):
    # 'ㅅ, ㅈ, ㅊ, ㅆ, ㅉ' 다음 약자 '영'이면 '엉' 변환 검사
    if (full_code[i] in [32, 40, 48]):
        # 인덱스 에러 방지
        if (i + 1 >= len(full_code)):
            pass
        # ㅅ,ㅈ,ㅊ
        elif (full_code[i + 1] == 59):
            result = hgtk.letter.compose(con[full_code[i]], 'ㅓ', 'ㅇ')
            trans_code.append(result)
            i += 2
            continue
        # ㅆ
        elif (full_code[i + 1] == 32):
            # 인덱스 에러 방지
            if (i + 2 >= len(full_code)):
                pass
            elif (full_code[i + 2] == 59):
                result = hgtk.letter.compose(fortis_con[full_code[i + 1]], 'ㅓ', 'ㅇ')
                trans_code.append(result)
                i += 3
                continue
        # ㅉ
        elif (full_code[i + 1] == 40):
            # 인덱스 에러 방지
            if (i + 2 >= len(full_code)):
                pass
            elif (full_code[i + 2] == 59):
                result = hgtk.letter.compose(fortis_con[full_code[i + 1]], 'ㅓ', 'ㅇ')
                trans_code.append(result)
                i += 3
                continue

    # 1. 숫자시작
    if (full_code[i] in num_sign):
        while True:
            if (i + 1 >= len(full_code)):
                i += 1
                break
            i += 1
            # 숫자
            if (full_code[i] in num):
                trans_code.append(num[full_code[i]])
            # 빈칸
            elif (full_code[i] in blank):
                trans_code.append(blank[full_code[i]])
                i += 1
                break
            # 특수문자
            elif (full_code[i] in pun):
                if (full_code[i] in [12, 18]):
                    # 인덱스 에러 방지
                    if (i + 1 >= len(full_code)):
                        i += 1
                        break
                    elif (full_code[i + 1] in [12, 18]):
                        trans_code.append(pun[full_code[i]])
                        i += 1
                else:
                    trans_code.append(pun[full_code[i]])
            # 붙임표 36점
            elif (full_code[i] in attach_sign):
                i += 1
                break
            # 기타
            else:
                break

    # 2. 영어시작
    elif (full_code[i] == 52):
        while True:
            if (i + 1 >= len(full_code)):
                i += 1
                break
            i += 1
            # 영어
            if (full_code[i] in eng):
                trans_code.append(eng[full_code[i]])
            # 대문자표
            elif (full_code[i] in eng_cap):
                if (i + 1 >= len(full_code)):
                    i += 1
                    break
                elif (full_code[i + 1] in eng):
                    i += 1
                    trans_code.append(eng2[full_code[i]])
            # 영어끝
            elif (full_code[i] == 50):
                i += 1
                break
            # 빈칸
            elif (full_code[i] in blank):
                trans_code.append(blank[full_code[i]])
            # 기타
            else:
                break

    # 3. 된소리(=ㅅ초성, nofortis로 검사)
    elif (full_code[i] == 32 and nofortis == False):
        # 인덱스 에러 방지
        if (i + 1 >= len(full_code)):
            nofortis = True
            continue
        # 초성
        if (full_code[i + 1] in fortis_con):
            fortis = True
            i += 1
        # 기타(ㅅ초성 포함)
        else:
            nofortis = True
            continue

    # 4. 초성
    elif (full_code[i] in con):
        # ㅅ초성으로 된소리에서 쫓겨남(초기화)
        if (nofortis):
            nofortis = False
        # 직전에 된소리가 찍혔던 경우(초기화, 된초성처리)
        if (fortis):
            fortis = False
            word1 = fortis_con[full_code[i]]
        # 그냥 초성이 들어온 경우
        else:
            word1 = con[full_code[i]]
        # 인덱스 에러 방지(초성으로 종료시)
        if (i + 1 >= len(full_code)):
            result = hgtk.letter.compose(word1, 'ㅏ')
            trans_code.append(result)
            i += 1
        # 초성2
        elif (full_code[i + 1] in con):
            result = hgtk.letter.compose(word1, 'ㅏ')
            trans_code.append(result)
            i += 1
        # 약자
        elif (full_code[i + 1] in abb):
            split = hgtk.letter.decompose(abb[full_code[i + 1]])
            result = hgtk.letter.compose(word1, split[1], split[2])
            trans_code.append(result)
            i += 2
        # 중성
        elif (full_code[i + 1] in vow):
            # 인덱스 에러 방지(중성으로 종료시)
            if (i + 2 >= len(full_code)):
                result = hgtk.letter.compose(word1, vow[full_code[i + 1]])
                trans_code.append(result)
                i += 2
            # 종성1
            elif (full_code[i + 2] in con_last):
                # 인덱스 에러 방지(종성으로 종료시)
                if (i + 3 >= len(full_code)):
                    result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                    trans_code.append(result)
                    i += 3
                # 종성2(ㄲ, ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ)
                elif (full_code[i + 2] in [1, 18, 2, 3]):
                    if (full_code[i + 2] == 1):
                        # ㄱ종성(ㄲ, ㄳ)
                        if (full_code[i + 3] == 1):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], fortis_last[full_code[i + 3]])
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 4):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄳ')
                            trans_code.append(result)
                            i += 4
                        # 기타
                        else:
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                            trans_code.append(result)
                            i += 3
                    elif (full_code[i + 2] == 18):
                        # ㄴ종성(ㄵ, ㄶ)
                        if (full_code[i + 3] == 5):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄵ')
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 52):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄶ')
                            trans_code.append(result)
                            i += 4
                        # 기타
                        else:
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                            trans_code.append(result)
                            i += 3
                    elif (full_code[i + 2] == 2):
                        # ㄹ종성(ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ)
                        if (full_code[i + 3] == 1):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄺ')
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 34):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄻ')
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 3):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄼ')
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 4):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄽ')
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 38):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄾ')
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 50):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄿ')
                            trans_code.append(result)
                            i += 4
                        elif (full_code[i + 3] == 52):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㅀ')
                            trans_code.append(result)
                            i += 4
                        # 기타
                        else:
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                            trans_code.append(result)
                            i += 3
                    elif (full_code[i + 2] == 3):
                        # ㅂ종성(ㅄ)
                        if (full_code[i + 3] == 4):
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㅄ')
                            trans_code.append(result)
                            i += 4
                        # 기타
                        else:
                            result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                            trans_code.append(result)
                            i += 3
                # 기타
                else:
                    result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                    trans_code.append(result)
                    i += 3

            # 붙임표
            elif (full_code[i + 2] in attach_sign):
                if (full_code[i + 1] in [39, 13, 28, 15]):
                    result = hgtk.letter.compose(word1, vow[full_code[i + 1]])
                    trans_code.append(result)
                    trans_code.append("애")
                    i += 3
                else:
                    result = hgtk.letter.compose(word1, vow[full_code[i + 1]])
                    trans_code.append(result)
                    trans_code.append("예")
                    i += 3
            # 기타
            else:
                result = hgtk.letter.compose(word1, vow[full_code[i + 1]])
                trans_code.append(result)
                i += 2
        # 종성1
        elif (full_code[i + 1] in con_last):
            # ㄱ종성
            if (full_code[i + 1] == 1):
                # 인덱스 에러 방지(ㄱ종성으로 종료시)
                if (i + 2 >= len(full_code)):
                    result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                    trans_code.append(result)
                    i += 2
                # 약어검사
                elif (full_code[i + 2] in conjun):
                    result = hgtk.letter.compose(word1, 'ㅏ')
                    trans_code.append(result)
                    trans_code.append(conjun[full_code[i + 2]])
                    i += 3
                # 종성2(ㄲ, ㄳ)
                elif (full_code[i + 2] == 1):
                    result = hgtk.letter.compose(word1, 'ㅏ', fortis_last[full_code[i + 2]])
                    trans_code.append(result)
                    i += 3
                elif (full_code[i + 2] == 4):
                    result = hgtk.letter.compose(word1, 'ㅏ', 'ㄳ')
                    trans_code.append(result)
                    i += 3
                # 기타
                else:
                    result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                    trans_code.append(result)
                    i += 2
            # ㄱ외 종성
            else:
                # 인덱스 에러 방지(종성으로 종료시)
                if (i + 2 >= len(full_code)):
                    result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                    trans_code.append(result)
                    i += 2
                # 겹받침 ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ, ㄸ, ㅃ, ㅉ
                # (ㄴ, ㄹ, ㅂ 시작)
                elif (full_code[i + 1] in [18, 2, 3]):
                    # ㄴ겹받침(ㄵ, ㄶ)
                    if (full_code[i + 1] == 18):
                        if (full_code[i + 2] == 5):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄵ')
                            trans_code.append(result)
                            i += 3
                        elif (full_code[i + 2] == 52):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄶ')
                            trans_code.append(result)
                            i += 3
                        else:
                            result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                            trans_code.append(result)
                            i += 2
                    # ㄹ겹받침(ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ)
                    elif (full_code[i + 1] == 2):
                        if (full_code[i + 2] == 1):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄺ')
                            trans_code.append(result)
                            i += 3
                        elif (full_code[i + 2] == 34):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄻ')
                            trans_code.append(result)
                            i += 3
                        elif (full_code[i + 2] == 3):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄼ')
                            trans_code.append(result)
                            i += 3
                        elif (full_code[i + 2] == 4):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄽ')
                            trans_code.append(result)
                            i += 3
                        elif (full_code[i + 2] == 38):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄾ')
                            trans_code.append(result)
                            i += 3
                        elif (full_code[i + 2] == 50):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㄿ')
                            trans_code.append(result)
                            i += 3
                        elif (full_code[i + 2] == 52):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㅀ')
                            trans_code.append(result)
                            i += 3
                        else:
                            result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                            trans_code.append(result)
                            i += 2
                    # ㅂ겹받침(ㅃ, ㅄ)
                    elif (full_code[i + 1] == 3):
                        if (full_code[i + 2] == 4):
                            result = hgtk.letter.compose(word1, 'ㅏ', 'ㅄ')
                            trans_code.append(result)
                            i += 3
                        else:
                            result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                            trans_code.append(result)
                            i += 2
                # 기타
                else:
                    result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                    trans_code.append(result)
                    i += 2


        # 기타
        else:
            i += 1

    # 5. 중성
    elif (full_code[i] in vow):
        # 인덱스 에러 방지(중성으로 종료시)
        if (i + 1 >= len(full_code)):
            result = hgtk.letter.compose('ㅇ', vow[full_code[i]])
            trans_code.append(result)
            i += 1
            continue
        # 중성2(ㅟ, ㅒ, ㅙ, ㅞ)
        elif (full_code[i] in [13, 28, 39, 15]):
            if (full_code[i + 1] == 23):
                if (full_code[i] == 13):
                    word2 = "ㅟ"
                    i += 1
                elif (full_code[i] == 28):
                    word2 = "ㅒ"
                    i += 1
                elif (full_code[i] == 39):
                    word2 = "ㅙ"
                    i += 1
                elif (full_code[i] == 15):
                    word2 = "ㅞ"
                    i += 1
            else:
                word2 = vow[full_code[i]]
        else:
            word2 = vow[full_code[i]]
        # 인덱스 에러 방지(이중모음 종료시)
        if (i + 1 >= len(full_code)):
            result = hgtk.letter.compose("ㅇ", word2)
            trans_code.append(result)
            i += 1
        # 종성1
        elif (full_code[i + 1] in con_last):
            # 인덱스 에러 방지(종성1로 종료시)
            if (i + 2 >= len(full_code)):
                result = hgtk.letter.compose("ㅇ", word2, con_last[full_code[i + 1]])
                trans_code.append(result)
                i += 2
            # 종성2(ㄲ, ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ)
            elif (full_code[i + 1] in [1, 18, 2, 3]):
                if (full_code[i + 1] == 1):
                    # ㄱ종성(ㄲ, ㄳ)
                    if (full_code[i + 2] == 1):
                        result = hgtk.letter.compose("ㅇ", word2, fortis_last[full_code[i + 2]])
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 4):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄳ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        result = hgtk.letter.compose("ㅇ", word2, con_last[full_code[i + 1]])
                        i += 2
                elif (full_code[i + 1] == 18):
                    # ㄴ종성(ㄵ, ㄶ)
                    if (full_code[i + 2] == 5):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄵ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 52):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄶ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        result = hgtk.letter.compose("ㅇ", word2, con_last[full_code[i + 1]])
                        trans_code.append(result)
                        i += 2
                elif (full_code[i + 1] == 2):
                    # ㄹ종성(ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ)
                    if (full_code[i + 2] == 1):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄺ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 34):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄻ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 3):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄼ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 4):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄽ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 38):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄾ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 50):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㄿ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 52):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㅀ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        result = hgtk.letter.compose("ㅇ", word2, con_last[full_code[i + 1]])
                        trans_code.append(result)
                        i += 2
                elif (full_code[i + 1] == 3):
                    # ㅂ종성(ㅄ)
                    if (full_code[i + 2] == 4):
                        result = hgtk.letter.compose("ㅇ", word2, 'ㅄ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        result = hgtk.letter.compose("ㅇ", word2, con_last[full_code[i + 1]])
                        trans_code.append(result)
                        i += 2
            # 기타
            else:
                result = hgtk.letter.compose("ㅇ", word2, con_last[full_code[i + 1]])
                trans_code.append(result)
                i += 2

        # 붙임표
        elif (full_code[i + 1] in attach_sign):
            if (full_code[i] in [39, 13, 28, 15]):
                result = hgtk.letter.compose("ㅇ", vow[full_code[i]])
                trans_code.append(result)
                trans_code.append("애")
                i += 2
            else:
                result = hgtk.letter.compose("ㅇ", vow[full_code[i]])
                trans_code.append(result)
                trans_code.append("예")
                i += 2

        # 기타
        else:
            result = hgtk.letter.compose("ㅇ", word2)
            trans_code.append(result)
            i += 1

    # 6. 약자
    elif (full_code[i] in abb and not yesfull):
        trans_code.append(abb[full_code[i]])
        i += 1

    # 7. 예외약자(가,사)
    elif (full_code[i] in abb_exc):
        # 인덱스 에러 방지(예외약자로 종료시)
        if (i + 1 >= len(full_code)):
            trans_code.append(abb_exc[full_code[i]])
            i += 1
        # 종성1
        elif (full_code[i + 1] in con_last):
            # 인덱스 에러 방지(종성으로 종료시)
            if (i + 2 >= len(full_code)):
                split = hgtk.letter.decompose(abb_exc[full_code[i]])
                result = hgtk.letter.compose(split[0], split[1], con_last[full_code[i + 1]])
                trans_code.append(result)
                i += 2
            # 종성2(ㄲ, ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ)
            elif (full_code[i + 1] in [1, 18, 2, 3]):
                if (full_code[i + 1] == 1):
                    # ㄱ종성(ㄲ, ㄳ)
                    if (full_code[i + 2] == 1):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], fortis_last[full_code[i + 2]])
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 4):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄳ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], con_last[full_code[i + 1]])
                        trans_code.append(result)
                        i += 2
                elif (full_code[i + 1] == 18):
                    # ㄴ종성(ㄵ, ㄶ)
                    if (full_code[i + 2] == 5):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄵ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 52):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄶ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], con_last[full_code[i + 1]])
                        trans_code.append(result)
                        i += 2
                elif (full_code[i + 1] == 2):
                    # ㄹ종성(ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ)
                    if (full_code[i + 2] == 1):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄺ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 34):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄻ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 3):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄼ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 4):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄽ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 38):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄾ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 50):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㄿ')
                        trans_code.append(result)
                        i += 3
                    elif (full_code[i + 2] == 52):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㅀ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], con_last[full_code[i + 1]])
                        trans_code.append(result)
                        i += 2
                elif (full_code[i + 1] == 3):
                    # ㅂ종성(ㅄ)
                    if (full_code[i + 2] == 4):
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], 'ㅄ')
                        trans_code.append(result)
                        i += 3
                    # 기타
                    else:
                        split = hgtk.letter.decompose(abb_exc[full_code[i]])
                        result = hgtk.letter.compose(split[0], split[1], con_last[full_code[i + 1]])
                        trans_code.append(result)
                        i += 2
            # 기타
            else:
                split = hgtk.letter.decompose(abb_exc[full_code[i]])
                result = hgtk.letter.compose(split[0], split[1], con_last[full_code[i + 1]])
                trans_code.append(result)
                i += 2
        # 기타
        else:
            trans_code.append(abb_exc[full_code[i]])
            i += 1

    # 8. 특수문자(-)
    elif (full_code[i] == 36):
        trans_code.append(pun[full_code[i]])
        i += 1

    # 9. 온표
    elif (full_code[i] in full_sign and yesfull):
        # 인덱스 에러 방지
        if (i + 1 >= len(full_code)):
            i += 1
        elif (full_code[i + 1] in con):
            trans_code.append(con[full_code[i + 1]])
            i += 2
        else:
            i += 1

    # 10. 약어
    elif (full_code[i] == 1):
        # 인덱스 에러 방지(단지 종성 ㄱ으로 종료시)
        if (i + 1 >= len(full_code)):
            i += 1
        elif (full_code[i + 1] in conjun):
            trans_code.append(conjun[full_code[i + 1]])
            i += 2
        else:
            i += 1

    # 11. 빈칸
    elif (full_code[i] in blank):
        trans_code.append(blank[full_code[i]])
        i += 1

    # 12. 것(56+14)
    elif (full_code[i] in thing):
        # 인덱스 에러 방지(단지 56으로 종료시)
        if (i + 1 >= len(full_code)):
            i += 1
        elif (full_code[i + 1] == 14):
            trans_code.append(thing[full_code[i]])
            i += 2
        else:
            i += 1
    # 종료
    else:
        break

result_code = "".join(trans_code)
print(result_code)
'''
n=0
if len(full_code)>1:
    while n<len(full_code)-1:
        if n==0:
            img1f="C:/APM_Setup/htdocs/test/"+str(full_code[n])+".jpg"
            img2f = "C:/APM_Setup/htdocs/test/" + str(full_code[n + 1]) + ".jpg"
            img1 = cv.imread(img1f, 1)
            img2 = cv.imread(img2f, 1)
            addh = cv.hconcat([img1, img2])
            n += 1
        else:
            img2f="C:/APM_Setup/htdocs/test/"+str(full_code[n+1])+".jpg"
            img2=cv.imread(img2f,1)
            addh=cv.hconcat([addh,img2])
            n+=1
elif len(full_code)==1:
    img1f="C:/APM_Setup/htdocs/test/"+str(full_code[n])+".jpg"
    addh =cv.imread(img1f, 1)

#cv.imshow("result", addh)
#cv.waitKey(0)
cv.imwrite("C:/APM_Setup/htdocs/check_img/"+name, addh)
'''
