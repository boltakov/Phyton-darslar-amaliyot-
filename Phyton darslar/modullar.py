# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:06:21 2026

@author: Bo'ltakov Diyor
"""
#MODULLAR

#math modulidan foydalanib:
#Foydalanuvchidan son qabul qiling
#Shu sonning kvadrat ildizi chiqaring
import math

def kvadrat(son):
    return math.sqrt(son)
#print(kvadrat(16))
'''
#random modulidan foydalanib lotereya o'yini yarating:
#1 dan 100 gacha tasodifiy son generatsiya qilinsin
#Foydalanuvchi son kiriting
#To'g'ri topsa — "Tabriklaymiz!", topalmasa — "Yutqazdingiz!" chiqsin
import random as r

def oyin(num1, num2, son_top):
    number = r.randint(num1, num2)  # bir marta generatsiya
    if son_top == number:            # ✅ shu sonni tekshir
        print("Tabriklaymiz!")
    else:
        print("Yutqazdingiz!")
    return number

son_top = int(input("1 dan 10 gacha son kiriting: "))
print(f"To'g'ri son: {oyin(1, 10, son_top)}")

import hisobla as h

print(h.yigindi(3, 5, 6, 7, 1))

print(h.kopaytma(1, 2, 3, 4))

print(h.ortacha(2, 3, 4, 5, 2))
'''
from datetime import datetime

def yosh_hisobla(tugilgan_yil):
    hozirgi_yil = datetime.now().year
    yosh = hozirgi_yil - tugilgan_yil
    return yosh

def chiroyli_sana():
    hozir = datetime.now()
    return hozir.strftime("%Y-yil, %d-%B, %A")

tugilgan_yil = int(input("Tug'ilgan yilingiz: "))

print(f"Yoshingiz: {yosh_hisobla(tugilgan_yil)}")
print(f"Bugun: {chiroyli_sana()}")

















