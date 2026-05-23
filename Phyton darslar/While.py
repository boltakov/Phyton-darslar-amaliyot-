# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:38:28 2026

@author: Bo'ltakov Diyor
"""

#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
#Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
savol = "Sevimli kitobingizni kiriting:\n"
savol += "(Dasturni to'xtatish uchun stop deb yozing)\n>>>"
qiymat = ''

while qiymat != 'stop':
    qiymat = input(savol).lower()
   
#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
#7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 
#65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi
#yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit
#deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).   
question = "\nMuzeyga kirish uchun yoshingizni kiriting:\n"
question += "(Dasturni to'xtatish uchun exit yoki quit deb yozing)\n>>>"
while  True:
    value = input(question).lower()
    if value in ['exit','quit']:
        break
    else:
        yosh = int(value)
        
    if yosh < 7:
        narx = 2000
    elif 7<= yosh <18:
        narx = 3000
    elif 18<= yosh < 65:
        narx = 10000
    else:
        narx = 0
        
        
    if narx == 0:
        print("Sizga chipta bepul")
    else:    
        print(f"Xush kelibsiz siz uchun chipta narxi {narx} so'm")    
       
#Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki 
#shart tekshirish)        
question = "\nMuzeyga kirish uchun yoshingizni kiriting:\n"
question += "(Dasturni to'xtatish uchun exit yoki quit deb yozing)\n>>>"
ishora = True
while  ishora:
    value = input(question).lower()
    if value == 'exit' or value == 'quit':
        ishora = False
    else:
        yosh = int(value)
        
        if yosh < 7:
            narx = 2000
        elif 7<= yosh <18:
            narx = 3000
        elif 18<= yosh < 65:
            narx = 10000
        else:
            narx = 0
        
        
        if narx == 0:
            print("Sizga chipta bepul")
        else:    
            print(f"Xush kelibsiz siz uchun chipta narxi {narx} so'm")    
              

question = "\nMuzeyga kirish uchun yoshingizni kiriting:\n"
question += "(Dasturni to'xtatish uchun stop deb yozing)\n>>>"
value = ''
while  value != 'stop':
    value = input(question).lower()
    if value != 'stop':
       yosh = int(value)
       
       if yosh < 7:
           narx = 2000
       elif 7<= yosh <18:
           narx = 3000
       elif 18<= yosh < 65:
           narx = 10000
       else:
           narx = 0
        
        
       if narx == 0:
           print("Sizga chipta bepul")
       else:    
           print(f"Xush kelibsiz siz uchun chipta narxi {narx} so'm")    
                            

#Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy 
#holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay 
#olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol).lower()
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
    
#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar 
#nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
buyurtmalar = []
while True:
    buyurtma = input("Buyurtmangizni kiting:\n>>>")
    buyurtmalar.append(buyurtma)
    during = input("Dasturni davom ettirasizmi? ha\yo'q>>>")
    if during != 'ha':
        break
    
print("Kechirasiz buyurtmalaringizni to'g'ri kiritdimmi?!")    
for b in buyurtmalar:
     print(b)
  
#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi
#dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar 
#(mahsulot va uning narhi) kiritishni so'rang.  
e_bozor = {}
hint = True
while hint:
   product = input("Siz uchun qaysi mahsulotni do'konimizga olib kelaylik?!\n>>>")    
   price = input(f"{product}ni narxi qancha bo'lishini xohlaysiz?!\n>>>")
   e_bozor[product] = float(price)
   question1 = input("Yana qaysidur mahsulot kerakmi?!(ha\yo'q)>>>") 
   if question1 != 'ha':
       hint = False
       
print("Siz e-bozor rastalarida shunaqa mahsulot bo'lishini xohlaysizmi?!")
for k, v in e_bozor.items():
    print(f"{k.title()} {v} so'm")       
  
#Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi 
#har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
#(tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud 
#bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" 
#degan xabarni kor'sating.    
e_bozor1 = {
    'olma':5000,
    'gilos':8000,
    'anjir':30000,
    'tarvuz':15000,
    'qovun':14000,
    'shaftoli':9000,
    'xurmo':20000
    }
buyurtmalar = []
while True:
    buyurtma = input("Buyurtmangizni kiting:\n>>>").lower()
    buyurtmalar.append(buyurtma)
    
    during = input("Dasturni davom ettirasizmi? ha\yo'q>>>")
    if during != 'ha':
        break
print("\n---Buyurtmalar tahlili---")
for e in buyurtmalar:
    if e in e_bozor1.keys():
        print(f"\n{e.title()} do'konimizda {e_bozor1[e]} so'm")
    
    else:
        print(f"\nKechirasiz bizda {e} yo'q")

    
    
    
    
    
    
    
    

    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
