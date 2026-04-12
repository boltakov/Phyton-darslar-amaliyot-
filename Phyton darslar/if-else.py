# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:28:16 2026

@author: Bo'ltakov Diyor
"""

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat 
#tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga 
#chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
 
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
       
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
#"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini 
#konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" 
#matnini konsolga chiqaring.   
ism = input("Iltimos!, login kiriting\n>>>").lower()     
if ism == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {ism.title()}")
 
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga 
#teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.  
print("Istalgan 2ta son kiriting.")
a = int(input("1-sonni kiriting.\n>>>"))
b = int(input("2-sonni kiriting.\n>>>"))
if a == b:
    print('Sonlar teng ekan.')

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa
#konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni 
#chiqaring. 
son = int(input("Istalgan son kiriting.\n>>>"))
if son >= 0:
    print("Siz musbat son kiritdingiz")
else:
    print("Siz manfiy son kiritdingiz")
   
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning 
#ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
#"Musbat son kiriting" degan xabarni chiqaring.  
son1 = int(input("Istalgan son kiriting.\n>>>")) 
if son1 >= 0:
    print(son1**0.5)
else:
    print("Musbat son kiriting.")    

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft 
#son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan 
#xabarni chiqaring.
son2 = int(input("Iltimos juft son kiriting.\n>>>"))
if son2 % 2 == 0:
    print("Rahmat")
else:
    print("Iltimos juft son kiriting")   
 
#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini 
#quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm    
yosh = int(input("Yoshingiz nechada?\n>>>"))
if yosh <= 4 or yosh >= 60:
    print("Sizga kirish bepul.")
elif yosh <= 18:
    print("Siz uchun kirish 10000 so'm")
else:
    print("Sizga kirish 20000 so'm")    

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va
#ularning teng yoki katta/kichikligi haqida xabarni chiqaring

print("Istalgan 2ta son kiriting.")
son3 = float(input("1-sonni kiriting.\n>>>"))
son4 = float(input("2-sonni kiriting.\n>>>"))
if son3 > son4:
    print(f"{son3}, {son4} dan katta.")
elif son3 < son4:
    print(f"{son3}, {son4} dan kichik.")
else:
    print(f"{son3} va {son4} teng.")    

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni
#kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan 
#savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni,
#mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
#"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" 
#degan xabarlarni chiqaring.
mahsulotlar = ['non', 'kalbasa', 'nok', 'olma', 'shaftoli', 'gilos',
               'gilos', 'olcha', 'pomidor', 'bodiring']
print("5ta mahsulot kiriting.")
savat = []
for s in range(5):
    savat.append(input(f"{s+1}-mahsulotni kiriting.\n>>>").lower())

if savat:
    for  mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"{mahsulot.title()} do'konimizda bor.")
        else:
            print(f"{mahsulot.title()} do'konimizda yo'q.")
else:
    print("Iltimos!, savatingizga mahsulot kiriting.")
    
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta
#mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor 
#mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q 
#mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  
#Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar 
#do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar
#do'konimizda yo'q: ....." degan xabarni chiqaring.
mahsulotlar = ['non', 'kalbasa', 'nok', 'olma', 'shaftoli', 'gilos',
               'gilos', 'olcha', 'pomidor', 'bodiring']
bor_mahsulotlar =[]
mavjud_emas = []
print("5ta mahsulot kiriting.")
savat = []
for s in range(5):
    savat.append(input(f"{s+1}-mahsulotni kiriting.\n>>>").lower())

if savat:
    for  mahsulot in savat:
        if mahsulot in mahsulotlar:
            bor_mahsulotlar.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)
    if mavjud_emas:
        print(f"Quyidagi mahsulotlar do'konimizda yo'q.\n{mavjud_emas}")
    else:
        print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print("Iltimos!, savatingizga mahsulot kiriting.")

#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
#Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan
#loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
#Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login 
#tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ["odil", 'anvar', 'tolib', 'ali', 'mansur']
username = input("Iltimos!, login kiriting.\n>>>").lower()
if username in foydalanuvchilar:
    print ("Kechirasiz, login band")
else:
    print(f"Xush kelibsiz, {username.title()}")

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi 
#kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz 
#bo'linishini konsolga chiqaring. 
son5 = int(input("Istalgan butun son kiriting.\n>>>"))
for n in range(2,11):
    if not (son5%n):
        print(f"{son5}, {n}ga qoldiqsiz bo'linadi")


















  