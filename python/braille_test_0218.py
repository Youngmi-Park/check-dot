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
num={1:1, 3:2, 9:3, 25:4, 17:5, 11:6, 27:7, 19:8, 10:9, 26:0}
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

#코드 리스트
full_code=[60, 9, 33, 9, 52, 1, 32, 1, 50, 43, 7, 0, 63, 43, 48, 59, 7,
           32, 40, 59, 8, 63, 8, 1, 4, 8, 2, 8, 18, 52, 17, 13, 2, 1, 61, 28, 23,
           15, 36, 39, 23, 54, 39, 23, 2, 1, 14, 3, 4, 17, 2, 1, 1, 37, 43, 38, 43, 1, 1,
           56, 14]
# 63이 약자인 경우
# [60, 9, 36, 9, 52, 1, 32, 1, 50, 43, 1, 37, 7, 0, 63, 43] = [3, '-', 3, 'a', 'A', '가', '그리고', '사', ' ', '옹', '가']
# 63이 온표인 경우
# [60, 9, 36, 9, 52, 1, 32, 1, 50, 43, 1, 37, 7, 0, 63, 26] = [3, '-', 3, 'a', 'A', '가', '그리고', '사', ' ', 'ㅎ']

#출력 리스트
trans_code=[]
i=0
fortis=False
nofortis=False

#온표검사
yesfull=0
if (full_code.count(63)):
     j=full_code.index(63)
     # 인덱스 에러 방지
     if (j+1 >= len(full_code)):
          pass
     elif (full_code[j+1] in con):
          yesfull=j


while (i < len(full_code)):
     #'ㅅ, ㅈ, ㅊ, ㅆ, ㅉ' 다음 약자 '영'이면 '엉' 변환 검사
     if (full_code[i] in [32, 40, 48]):
          # 인덱스 에러 방지
          if (i+1 >= len(full_code)):
               pass
          #ㅅ,ㅈ,ㅊ
          elif(full_code[i+1] == 59):
               result = hgtk.letter.compose(con[full_code[i]], 'ㅓ', 'ㅇ')
               trans_code.append(result)
               i+=2
               continue
          #ㅆ
          elif (full_code[i+1]==32):
               # 인덱스 에러 방지
               if (i+2 >= len(full_code)):
                    pass
               elif (full_code[i+2] == 59):
                    result = hgtk.letter.compose(fortis_con[full_code[i+1]], 'ㅓ', 'ㅇ')
                    trans_code.append(result)
                    i+=3
                    continue
          #ㅉ
          elif (full_code[i+1]==40):
               # 인덱스 에러 방지
               if (i+2 >= len(full_code)):
                    pass
               elif (full_code[i+2] == 59):
                    result = hgtk.letter.compose(fortis_con[full_code[i + 1]], 'ㅓ', 'ㅇ')
                    trans_code.append(result)
                    i+=3
                    continue

     # 1. 숫자시작
     if (full_code[i] in num_sign):
          while True:
               i+=1
               #숫자
               if (full_code[i] in num):
                    trans_code.append(num[full_code[i]])
               #빈칸
               elif (full_code[i] in blank):
                    trans_code.append(blank[full_code[i]])
                    i+=1
                    break
               #특수문자
               elif (full_code[i] in pun):
                    if (full_code[i] in [12, 18]):
                         # 인덱스 에러 방지
                         if (i+1 >= len(full_code)):
                              break
                         elif (full_code[i+1] in [12, 18]):
                              trans_code.append(pun[full_code[i]])
                              i+=1
                    else:
                         trans_code.append(pun[full_code[i]])
               #붙임표 36점
               elif(full_code[i] in attach_sign):
                    i+=1
                    break
               #기타
               else:
                    break

     # 2. 영어시작
     elif (full_code[i] == 52):
          while True:
               i+=1
               #영어
               if (full_code[i] in eng):
                   trans_code.append(eng[full_code[i]])
               #대문자표
               elif (full_code[i] in eng_cap):
                    i+=1
                    trans_code.append(eng2[full_code[i]])
               #영어끝
               elif (full_code[i] ==50):
                    i+=1
                    break
               #기타
               else:
                    break

     # 3. 된소리(=ㅅ초성, nofortis로 검사)
     elif (full_code[i] == 32 and nofortis == False):
          #인덱스 에러 방지
          if (i+1 >= len(full_code)):
               nofortis=True
               continue
          #초성
          if (full_code[i+1] in con):
               fortis=True
               i+=1
          #기타(ㅅ초성 포함)
          else:
               nofortis=True
               continue

     # 4. 초성
     elif (full_code[i] in con):
          #ㅅ초성으로 된소리에서 쫓겨남(초기화)
          if (nofortis):
               nofortis=False
          #직전에 된소리가 찍혔던 경우(초기화, 된초성처리)
          if (fortis):
               fortis=False
               word1=fortis_con[full_code[i]]
          #그냥 초성이 들어온 경우
          else:
               word1=con[full_code[i]]
          # 인덱스 에러 방지(초성으로 종료시)
          if (i+1 >= len(full_code)):
               result = hgtk.letter.compose(word1, 'ㅏ')
               trans_code.append(result)
               i+=1
          #초성2
          elif (full_code[i+1] in con):
               result = hgtk.letter.compose(word1, 'ㅏ')
               trans_code.append(result)
               i+=1
          #약자
          elif (full_code[i+1] in abb):
               split=hgtk.letter.decompose(abb[full_code[i+1]])
               result = hgtk.letter.compose(word1, split[1], split[2])
               trans_code.append(result)
               i+=2
          #종성1
          elif (full_code[i+1] in con_last):
               #ㄱ종성
               if (full_code[i+1] == 1):
                    #인덱스 에러 방지(ㄱ종성으로 종료시)
                    if (i + 2 >= len(full_code)):
                         result=hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i+1]])
                         trans_code.append(result)
                         i+=2
                    #약어검사
                    elif (full_code[i+2] in conjun):
                         result=hgtk.letter.compose(word1, 'ㅏ')
                         trans_code.append(result)
                         trans_code.append(conjun[full_code[i+2]])
                         i+=3
                    #종성2(ㄲ, ㄳ)
                    elif (full_code[i+2] == 1):
                         result=hgtk.letter.compose(word1, 'ㅏ', fortis_last[full_code[i+2]])
                         trans_code.append(result)
                         i+=3
                    elif (full_code[i+2] == 4):
                         result=hgtk.letter.compose(word1, 'ㅏ', 'ㄳ')
                         trans_code.append(result)
                         i+=3
                    #기타
                    else:
                         result=hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i+1]])
                         trans_code.append(result)
                         i+=2
               #ㄱ외 종성
               else:
                    # 인덱스 에러 방지(종성으로 종료시)
                    if (i + 2 >= len(full_code)):
                         result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                         trans_code.append(result)
                         i += 2
                    #겹받침 ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ, ㄸ, ㅃ, ㅉ
                    #(ㄴ, ㄹ, ㅂ 시작)
                    elif (full_code[i+1] in [18, 2, 3]):
                         #ㄴ겹받침(ㄵ, ㄶ)
                         if (full_code[i+1] == 18):
                              if (full_code[i+2] == 5):
                                   result=hgtk.letter.compose(word1, 'ㅏ', 'ㄵ')
                                   trans_code.append(result)
                                   i += 3
                              elif (full_code[i+2] == 52):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㄶ')
                                   trans_code.append(result)
                                   i += 3
                              else:
                                   result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i+1]])
                                   trans_code.append(result)
                                   i+=2
                         #ㄹ겹받침(ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ)
                         elif (full_code[i + 1] == 2):
                              if (full_code[i + 2] == 1):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㄺ')
                                   trans_code.append(result)
                                   i += 3
                              elif (full_code[i+2] == 34):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㄻ')
                                   trans_code.append(result)
                                   i += 3
                              elif (full_code[i+2] == 3):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㄼ')
                                   trans_code.append(result)
                                   i += 3
                              elif (full_code[i+2] == 4):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㄽ')
                                   trans_code.append(result)
                                   i += 3
                              elif (full_code[i+2] == 38):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㄾ')
                                   trans_code.append(result)
                                   i += 3
                              elif (full_code[i+2] == 50):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㄿ')
                                   trans_code.append(result)
                                   i += 3
                              elif (full_code[i+2] == 52):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㅀ')
                                   trans_code.append(result)
                                   i += 3
                              else:
                                   result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                                   trans_code.append(result)
                                   i += 2
                         #ㅂ겹받침(ㅃ, ㅄ)
                         elif (full_code[i + 1] == 3):
                              if (full_code[i+2] == 4):
                                   result = hgtk.letter.compose(word1, 'ㅏ', 'ㅄ')
                                   trans_code.append(result)
                                   i += 3
                              else:
                                   result = hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i + 1]])
                                   trans_code.append(result)
                                   i += 2
                    #기타
                    else:
                         result=hgtk.letter.compose(word1, 'ㅏ', con_last[full_code[i+1]])
                         trans_code.append(result)
                         i+=2
          #중성
          elif (full_code[i + 1] in vow):
               #인덱스 에러 방지(중성으로 종료시)
               if (i+2 >= len(full_code)):
                    result=hgtk.letter.compose(word1, vow[full_code[i+1]])
                    trans_code.append(result)
                    i+=2
               #종성1
               elif (full_code[i+2] in con_last):
                    #인덱스 에러 방지(종성으로 종료시)
                    if (i+3 >= len(full_code)):
                         result=hgtk.letter.compose(word1, vow[full_code[i+1]], con_last[full_code[i+2]])
                         trans_code.append(result)
                         i+=3
                    #종성2(ㄲ, ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ)
                    elif (full_code[i+2] in [1, 18, 2, 3]):
                         if (full_code[i+2] == 1):
                              #ㄱ종성(ㄲ, ㄳ)
                              if (full_code[i + 3] == 1):
                                   result = hgtk.letter.compose(word1, vow[full_code[i+1]], fortis_last[full_code[i + 3]])
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i + 3] == 4):
                                   result = hgtk.letter.compose(word1, vow[full_code[i+1]], 'ㄳ')
                                   trans_code.append(result)
                                   i += 4
                              # 기타
                              else:
                                   result = hgtk.letter.compose(word1, vow[full_code[i+1]], con_last[full_code[i + 2]])
                                   trans_code.append(result)
                                   i += 3
                         elif (full_code[i+2] == 18):
                              #ㄴ종성(ㄵ, ㄶ)
                              if (full_code[i+3]==5):
                                   result= hgtk.letter.compose(word1, vow[full_code[i+1]], 'ㄵ')
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i+3]==52):
                                   result= hgtk.letter.compose(word1, vow[full_code[i+1]], 'ㄶ')
                                   trans_code.append(result)
                                   i += 4
                              # 기타
                              else:
                                   result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                                   trans_code.append(result)
                                   i += 3
                         elif (full_code[i + 2] == 2):
                              #ㄹ종성(ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ)
                              if (full_code[i+3] == 1):
                                   result= hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄺ')
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i+3] == 34):
                                   result= hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄻ')
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i+3] == 3):
                                   result= hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄼ')
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i+3] == 4):
                                   result= hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄽ')
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i+3] == 38):
                                   result= hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄾ')
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i+3] == 50):
                                   result= hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㄿ')
                                   trans_code.append(result)
                                   i += 4
                              elif (full_code[i+3] == 52):
                                   result= hgtk.letter.compose(word1, vow[full_code[i + 1]], 'ㅀ')
                                   trans_code.append(result)
                                   i += 4
                              # 기타
                              else:
                                   result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                                   trans_code.append(result)
                                   i += 3
                         elif (full_code[i + 2] == 3):
                              #ㅂ종성(ㅄ)
                              if (full_code[i+3]==4):
                                   result= hgtk.letter.compose(word1, vow[full_code[i+1]], 'ㅄ')
                                   trans_code.append(result)
                                   i += 4
                              # 기타
                              else:
                                   result = hgtk.letter.compose(word1, vow[full_code[i + 1]], con_last[full_code[i + 2]])
                                   trans_code.append(result)
                                   i += 3
                    #기타
                    else:
                         result=hgtk.letter.compose(word1, vow[full_code[i+1]], con_last[full_code[i+2]])
                         trans_code.append(result)
                         i+=3

               #붙임표
               elif (full_code[i+2] in attach_sign):
                    if (full_code[i+1] in [39, 13, 28, 15]):
                         result = hgtk.letter.compose(word1, vow[full_code[i+1]])
                         trans_code.append(result)
                         trans_code.append("애")
                         i += 3
                    else:
                         result=hgtk.letter.compose(word1, vow[full_code[i+1]])
                         trans_code.append(result)
                         trans_code.append("예")
                         i+=3
               #기타
               else:
                    result=hgtk.letter.compose(word1, vow[full_code[i+1]])
                    trans_code.append(result)
                    i+=2

          #기타
          else:
               i+=1

     # 5. 중성
     elif (full_code[i] in vow):
          # 인덱스 에러 방지(중성으로 종료시)
          if (i + 1 >= len(full_code)):
               result = hgtk.letter.compose('ㅇ', vow[full_code[i]])
               trans_code.append(result)
               i += 1
               continue
          #중성2(ㅟ, ㅒ, ㅙ, ㅞ)
          elif (full_code[i] in [13, 28, 39, 15]):
               if(full_code[i+1] ==23):
                    if(full_code[i]==13):
                         word2="ㅟ"
                         i+=1
                    elif(full_code[i]==28):
                         word2="ㅒ"
                         i+=1
                    elif(full_code[i]==39):
                         word2="ㅙ"
                         i+=1
                    elif(full_code[i]==15):
                         word2="ㅞ"
                         i+=1
               else:
                    word2=vow[full_code[i]]
          else:
               word2=vow[full_code[i]]
          #인덱스 에러 방지(이중모음 종료시)
          if (i+1 >= len(full_code)):
               result=hgtk.letter.compose("ㅇ", word2)
               trans_code.append(result)
               i+=1
          #종성1
          elif (full_code[i+1] in con_last):
               #인덱스 에러 방지(종성1로 종료시)
               if (i+2 >= len(full_code)):
                    result=hgtk.letter.compose("ㅇ", word2, con_last[full_code[i+1]])
                    trans_code.append(result)
                    i+=2
               # 종성2(ㄲ, ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ)
               elif (full_code[i + 1] in [1, 18, 2, 3]):
                    if(full_code[i+1]==1):
                         #ㄱ종성(ㄲ, ㄳ)
                         if (full_code[i+2] == 1):
                              result=hgtk.letter.compose("ㅇ", word2, fortis_last[full_code[i+2]])
                              trans_code.append(result)
                              i+=3
                         elif (full_code[i+2]==4):
                              result = hgtk.letter.compose("ㅇ", word2, 'ㄳ')
                              trans_code.append(result)
                              i += 3
                         #기타
                         else:
                              result = hgtk.letter.compose("ㅇ", word2, con_last[full_code[i+1]])
                              i+=2
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
               #기타
               else:
                    result=hgtk.letter.compose("ㅇ", word2, con_last[full_code[i+1]])
                    trans_code.append(result)
                    i+=2

          # 붙임표
          elif (full_code[i + 1] in attach_sign):
               if (full_code[i] in [39, 13, 28, 15]):
                    result = hgtk.letter.compose("ㅇ", vow[full_code[i]])
                    trans_code.append(result)
                    trans_code.append("애")
                    i+=2
               else:
                    result = hgtk.letter.compose("ㅇ", vow[full_code[i]])
                    trans_code.append(result)
                    trans_code.append("예")
                    i += 2

          #기타
          else:
               result=hgtk.letter.compose("ㅇ", word2)
               trans_code.append(result)
               i+=1

     # 6. 약자
     elif (full_code[i] in abb and i != yesfull):
          trans_code.append(abb[full_code[i]])
          i+=1

     # 7. 예외약자(가,사)
     elif (full_code[i] in abb_exc):
          #인덱스 에러 방지(예외약자로 종료시)
          if (i+1 >= len(full_code)):
               trans_code.append(abb_exc[full_code[i]])
               i+=1
          #종성1
          elif (full_code[i+1] in con_last):
               #인덱스 에러 방지(종성으로 종료시)
               if (i+2 >= len(full_code)):
                    split=hgtk.letter.decompose(abb_exc[full_code[i]])
                    result=hgtk.letter.compose(split[0], split[1], con_last[full_code[i+1]])
                    trans_code.append(result)
                    i+=2
               # 종성2(ㄲ, ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ)
               elif (full_code[i+1] in [1, 18, 2, 3]):
                    if (full_code[i + 1] == 1):
                         # ㄱ종성(ㄲ, ㄳ)
                         if (full_code[i + 2] == 1):
                              split = hgtk.letter.decompose(abb_exc[full_code[i]])
                              result = hgtk.letter.compose(split[0],split[1], fortis_last[full_code[i + 2]])
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
                              result = hgtk.letter.compose(split[0], split[1], con_last[full_code[i+1]])
                              trans_code.append(result)
                              i += 2
                    elif (full_code[i+1]==18):
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
                    elif(full_code[i+1]==2):
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
                    elif(full_code[i+1]==3):
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
               #기타
               else:
                    split = hgtk.letter.decompose(abb_exc[full_code[i]])
                    result=hgtk.letter.compose(split[0], split[1], con_last[full_code[i+1]])
                    trans_code.append(result)
                    i+=2
          #기타
          else:
               trans_code.append(abb_exc[full_code[i]])
               i+=1

     # 8. 특수문자(-)
     elif (full_code[i] == 36):
          trans_code.append(pun[full_code[i]])
          i+=1

     # 9. 온표
     elif (full_code[i] in full_sign and yesfull):
          # 인덱스 에러 방지
          if (i + 1 >= len(full_code)):
               i+=1
          elif (full_code[i+1] in con):
               trans_code.append(con[full_code[i+1]])
               i+=2
          else:
               i+=1
     
     # 10. 약어
     elif (full_code[i] == 1):
          #인덱스 에러 방지(단지 종성 ㄱ으로 종료시)
          if (i + 1 >= len(full_code)):
               i+=1
          elif(full_code[i+1] in conjun):
               trans_code.append(conjun[full_code[i+1]])
               i+=2
          else:
               i+=1

     # 11. 빈칸
     elif (full_code[i] in blank):
          trans_code.append(blank[full_code[i]])
          i+=1

     # 12. 것(56+14)
     elif (full_code[i] in thing):
          #인덱스 에러 방지(단지 56으로 종료시)
          if (i+1 >= len(full_code)):
               i+=1
          elif (full_code[i+1] == 14):
               trans_code.append(thing[full_code[i]])
               i+=2
          else:
               i+=1
     # 종료
     else:
          break

print(trans_code)

#result=hgtk.letter.compose(con[9], vow[28], con_last[34])
#print(result*3)
#result=hgtk.letter.compose(con[9], vow[28])
#print(result)
#result=hgtk.letter.compose(con[9], vow[35], 'ㄺ')
#print(result)
