# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:37:35 2026

@author: Bo'ltakov Diyor
"""
'''
#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan 
#funksiya yozing.
def yosh_hisobla(ism, yosh):
    """Foydalanuvchidan ismi va yoshini so'rab 
    tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()}, siz {2026-yosh}-yil tug'ilgansiz.")
    
yosh_hisobla('Fozil', 23)

#Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi 
#funksiya yozing.
def kv_kub_hisobla(son):
    """Foydalanuvchidan son qabul qilib uni 
    kvadrati va kubini hisoblaydigan funksiya"""
    print(f"{son}ning kvadrati {son**2}ga teng, kubi esa {son**3}ga teng.")
    
kv_kub_hisobla(10)

#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi 
#funksiya yozing.
def son_juft_toq(son1):
    """Foydalanuvchidan son qabul qilib uni juft 
    yoki toq sonligini tekshiruvchi dastur"""
    if son1%2==0:
        print(f"Siz juft son kiritdingiz, ya'ni {son1}")
    else:
        print(f"Siz toq son kiritdingiz, ya'ni {son1}")
  
son_juft_toq(45)   

#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
#funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni 
#chiqaring.
def son_taqqosla(son2,son3):
    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga 
    chiqaruvchi funksiya.  Agar sonlar teng bo'lsa "Sonlar teng" degan
    xabarni chiqaring."""
    if son2>son3:
        print(son2)
    elif son2 == son3:
        print(f"Sonlar teng {son2} = {son3}.")
    else:
        print(son3)
        
son_taqqosla(24,22)   

#Foydalanuvchidan x va y sonlarini olib, x**y ni konsolga chiqaruvchi 
#funksiya yozing.
def darajani_hisobla(x,y):
    """Foydalanuvchidan 2ta son qabul qilib ikkinchi sonni birinchi
    sonni darajasi deb hisoblab console ga chiqaradi"""
    print(f"{x}ning {y}-darajasi {x**y}ga teng")
    
darajani_hisobla(4, 3)  

#Yuqoridagi funksiyada y uchun 2 standart qiymatini bering  
def darajani_hisoblaymiz(x, y=2):
    """Foydalanuvchidan 2ta son qabul qilib ikkinchi sonni birinchi
    sonni darajasi deb hisoblab console ga chiqaradi"""
    print(f"{x}ning {y}-darajasi {x**y}ga teng")
    
darajani_hisoblaymiz(4)    

#Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
#qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga
#chiqaring.     
def songa_bolinadimi(son4):
    """Foydalanuvchidan son qabul qilib uni 2 dan 10 gacha bo'lgan sonlarni 
    qaysi biriga qoldiqsiz bo'linishini console ga chiqaruvchi funksiya"""
    for a in range(2,10):
        if son4 % a == 0:
            print(f"{son4}, {a}ga qoldiqsiz bo'linadi")
            
songa_bolinadimi(78)            
'''
'''
#Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email 
#manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi 
#funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi 
#argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
def document(ism, familiya, t_yili, email = '', tel_raqam = ''):
    """Foydalanuvchi ma'lumotlarini lug'at qilib saqlovchi funksiya"""
    malumot = {
         'ism': ism,
         'familiya': familiya,
         't_yili': t_yili,
         'email': email,
         'tel_raqam': tel_raqam
       }
    return malumot

i = document('Diyor', 'Bo\'ltakov', 2003, tel_raqam=+998873902145,
             email='boltakovdiyor490@gmail.com')

#Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va 
#mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi 
#ma'lumotni konsolga chiqaring.
print("Mijozlar ro'yxatini shakllantiramiz.")
users = []
while True:
    print("Foydalanuvchini quyidagi ma'lumotlarini kiriting.")
    ism = input("Ismi?>>>")
    familiya = input("Familiyasi?>>>")
    t_yili = input("Tug'ilgan yili?>>>")
    email = input("Email elektron pochtasi?>>>")
    tel_raqam = input("Telefon raqami?>>>")
    
    users.append(document(ism, familiya, t_yili, email, tel_raqam))
    value = input("Yana, boshqa foydalanuvchi ma'lumotlarini ham "
                 "kiritishni xohlaysizmi(yes\no)>>>")
    if value == "no":
        break
       
print(users)

#Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def kattasi(son1, son2, son3):
    return max(son1, son2, son3)
    
#Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
#diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya 
#yozing
import math

def aylana_olchamlari(radius):
    diametr = float(radius) * 2
    perimetr = float(diametr) * math.pi
    yuzi = float(radius)**2 * math.pi
    olcham = {
        'radius': radius,
        'diametr': diametr,
        'perimetr': perimetr,
        'yuzi': yuzi
        }
    return olcham

print(aylana_olchamlari(21))

#Berilgan oraliqdagi tub sonlar ro'yx'atini qaytaruvchi f'unksiya yozing 

def tub_son(min_son, max_son):
    tub_sonlar = []
    for a in range(min_son, max_son + 1):
        tub = True
        if a == 1:
           tub = False
        elif a == 2:
            tub = True
        else:
            for b in range(2, a):
                if a % b == 0:
                    tub = False
        if tub == True:
             tub_sonlar.append(a)
                    
    return tub_sonlar             

print(tub_son(2, 50))            

#Foydalanuvchidan son "qabul qilib, shu son m"iqdoricha Fibonachchi "
#ketma-ketligidagi s"onlar ro'yxatni qayta"ruvchi funksiya yozin"g.  
#Ta’rif: Har bi"r hadi o’zidan oldin"gi ikkita hadning yi"g’indisiga 
#teng b"o’lgan ketma-ketlik" Fibonachchi ketma-"ketligi deyiladi.
def fibonachchi(q):
    """Kiritilgan son miqdoricha o'zidan 2ta oldingi sonni yig'indisiga 
    teng sonli ketma-ketlik(Fibonachchi)ni chiqaruvchi funksiya"""
    tartib = []
    for r in range(q):
        if r==0 or r==1:
            tartib.append(1)
        else:
             tartib.append(tartib[r-2] + tartib[r-1])
    return tartib 
print(fibonachchi(7))

#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning 
#birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 
def katta_harf(matn):
    """Ro'yxatdagi elementlarni bosh harfini katta qilib 
    beruvchi funksiya"""
    shaharlar = []
    for s in matn:
        s = s.title()
        shaharlar.append(s)
    return shaharlar
      
city = ['samarqand', 'buxoro', 'toshkent', 'xiva']   
shahar = katta_harf(city[:])  
print(shahar)  
print(city)  
    
#Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
#foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at 
#qaytaradigan qilib yozing.  
def bahola(ismlar):
    """Ro'yxatdan talabalar ismlarini qabul qilib, ularga baho qo'yib,
    lug'at ko'rinishida saqlovchi funksiya"""
    baholar = {}
    for h in ismlar:
        baho = input(f"Talabangiz {h}ning bahosini kiriting:>>>")
        baholar[h] = int(baho)
    return baholar
    
talabalar = ['Nodir', 'Fozil', 'Abduqodir', 'Qutbiddin']
student = bahola(talabalar[:])
print(talabalar)
print(student)
'''
#Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi 
#funksiya yozing
def kopaytama(*sonlar):
    """Kiritilganlar sonlar ko'paytmasi hisoblovchi funksiya"""
    kopaytamalar = 1
    for son in sonlar:
        kopaytamalar *= son
    return kopaytamalar

print(kopaytama(2,3,4,5,6))    

#Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi
#funkisya yozing. Talabaning ismi va familiyasi majburiy argument, 
#qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi 
#mumkin bo'lsin.
def talabalar(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

talaba1 = talabalar('Zafar', 'Erkinov', t_yili = 2005, t_joyi = 'Jizzax',
                   kurs = 3)
print(talaba1)

#*args va **kwargs ni birgalikda ishlatib, quyidagini amalga oshiring:

#*args orqali sonlar qabul qilinsin va ularning o'rtacha qiymati hisoblansin
#**kwargs orqali qo'shimcha ma'lumotlar qabul qilinsin
#Natijada lug'at qaytarilsin
def hisob(*args, **kwargs):
    ortacha = sum(args) / len(args)
    natija = {'o\'rtacha': ortacha}  # faqat bitta kalit bor
    natija.update(kwargs)            # kwargs dan kelgan kalitlar qo'shiladi
    return natija

print(hisob(10, 20, 30, nom="Ali", guruh="CS-101"))





















    
    
    
    
    
    
    
    
    






