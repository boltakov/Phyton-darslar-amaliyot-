# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:26:57 2026

@author: Bo'ltakov Diyor
"""

#otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu 
#inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, 
#manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga
#chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida 
#tug'ilgan
otam = {'ismi':'Xolmatov Ubaydullo', 't_yili':'1970',\
         'shahri':'Chelak', 'mahalla':'Turkibola'}
men = {'ismi':'Bo\'ltakov Diyor', 't_yili':'2003',\
       'shahri':'Chelak','mahalla':'Aliobod'}   
 
print(f"Otamning ismi {otam['ismi']}, {otam['t_yili']}-yili\
 {otam['shahri']} shahri {otam['mahalla']} mahallasida tug'ilgan. ")

print(f"Mening ismim {men['ismi']}, {men['t_yili']}-yil\
 {men['shahri']} {men['mahalla']} mahallasida tug'ilganman.")
 
#Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 
#5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini 
#konsolga chiqaring: Alining sevimli taomi osh
taomlar = {
    'Mansur':'manti',
    'Ortiq':'osh',
    "Farid":'shashlik',
    'Yodgor':'somsa',
    'Mirzabek':'chuchvara'
    }
print(f"Mansurning sevimli taomi {taomlar['Mansur']}.")
print(f"Yodgorning sevimli taomi {taomlar['Yodgor']}.")
print(f"Ortiqning sevimli taomi {taomlar['Ortiq']}.")

#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta 
#so'z (atamani) kiriting (masalan integer, float, string, if, else va 
#hokazo) va har birining qisqacha tarjimasini yozing.
phyton = {
    'int':'faqat butun sonlarni qabul qiladi',
    'float':'barcha sonlarni qabul qiladi',
    'string':'faqat matn qabul qiladi',
    'if':'Agar deb nomlanadigan shart operatori',
    'else':'Aks holda deb nomlanadigan shart operatori',
    'for':'takrorlab beruvchi operator',
    'elif':'if va else bilan birga ishlatiladi',
    'list':'ma\'lumotlar ro\'yxati',
    "lug'at":'kalit va qiymatdan iborat bo\'lgan ro\'yxat',
    'print':'console ga matn chiqarib beradi'
    }

#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini 
#yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa,
#"Bunda so'z mavjud emas" degan xabarni chiqaring
k = input("Phytonda siz uchun tushunarsiz bo'lgan atamani kiriting\n>>>").lower()
print(phyton.get(k,'Bunday atama mavjud emas'))

#Yuqoridagi vazifani if-else yordamida qiling va natijani ham 
#foydalanuvchiga tushunarli ko'rinishda chiqaring.
a = input("Phytonda siz uchun tushunarsiz bo'lgan atamani kiriting\n>>>").lower()
if a in phyton:
    print(phyton[a])
else:
    print("Bunday atama mavjud emas.")    













