# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:47:55 2026

@author: Bo'ltakov Diyor
"""

#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi 
#har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Nodir', 'Baxtiyor', 'Maruf', 'Abdukarim', 'Yusuf']
for a in ismlar:
    print(f"Assalomu alaykum {a}, Salomatmisiz? Ahvollariz yaxshimi?")
    
#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi"
#degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)        
print("Kod", len(ismlar), "marta takrorlandi.")    

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar
#bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(10,100,2))
for s in sonlar:
    print(f"{s}soninig kubi {s**3}ga teng.\n")

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va
#kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring
kinolar = []
print("Eng sevimli 5ta kinoingizni kiriting.")   
for b in range(5):
    kinolar.append(input(f"{b+1}-kinoni kitiring\n>>>"))
print(kinolar)    

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) 
#so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab 
#ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
dostlarim = []
son = int(input("Bugun nechta odam bilan suhbatlashdingiz\n>>>"))
for r in range(son):
    dostlarim.append(input(f"{r+1}-do'stingizni ismini kiriting.\n>>>"))
    
print(dostlarim)    

    

    
    
    
    
    
    
    