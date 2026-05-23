# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:17:36 2026

@author: Bo'ltakov Diyor
"""

#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar
#haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta 
#ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
mashhur1 = {
    'ismi':'Aziz',
    'familiyasi':'Rahimov',
    't_yili':'1993',
    't_joy':'Toshkent',
    'kasbi':'o\'qituvchi', 
    }

mashhur2 = {
    'ismi':'Al-Buxoriy',
    'familiyasi':'Ismoil',
    't_yili':'810',
    't_joy':'Buxora',
    'kasbi':'muhaddis'
    }

mashhur3 = {
    'ismi':'Jaloliddin',
    'familiyasi':'Manguberdi',
    't_yili':'1198',
    't_joy':'Xorazm',
    'kasbi':'sarkarda'
    }

mashhur4 = {
    'ismi':'Amir',
    'familiyasi':'Temur',
    't_yili':'1336',
    't_joy':'Qashqadaryo',
    'kasbi':'sarkarda'
    }

mashhur = [mashhur1, mashhur2, mashhur3, mashhur4]
for n in mashhur:
    print(f"{n['ismi']} {n['familiyasi']} {n['t_yili']}-yilda, "
          f"{n['t_joy']}da tug'ilgan kasbi {n['kasbi']}. ")
  
#Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham
#qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini 
#konsolga chiqaring.
mashhur1 = {
    'ismi':'Aziz',
    'familiyasi':'Rahimov',
    't_yili':'1993',
    't_joy':'Toshkent',
    'kasbi':'o\'qituvchi', 
    'loyihasi':['podkast','parallel muhit','Rahimov school']
    }

mashhur2 = {
    'ismi':'Al-Buxoriy',
    'familiyasi':'Ismoil',
    't_yili':'810',
    't_joy':'Buxora',
    'kasbi':'muhaddis',
    'loyihasi':['Al-jome As-sahih',"Al-Adab al-Mufrad",
                "At-Ta'rix al-Kabir","Tafsir al-Qur'on"]
    }

mashhur3 = {
    'ismi':'Jaloliddin',
    'familiyasi':'Manguberdi',
    't_yili':'1198',
    't_joy':'Xorazm',
    'kasbi':'sarkarda',
    'loyihasi':['Xorazm davlatini qayta tiklagan',
                'Chingizxonga qarshi kurashgan',]
    }

mashhur4 = {
    'ismi':'Amir',
    'familiyasi':'Temur',
    't_yili':'1336',
    't_joy':'Qashqadaryo',
    'kasbi':'sarkarda',
    'loyihasi':['Samarqandni dunyo markaziga aylantirgan',
                'Dunyoni 1/3ni boshqargan', 
                'Yevropani mo\'g\'ullardan qutqarib qolgan.']
    }

mashhur = [mashhur1, mashhur2, mashhur3, mashhur4]
for a in mashhur:
    print(f"\n{a['ismi']} {a['familiyasi']}ni qilgan ishlari:")
    for k in a['loyihasi']:
         print(k)

#Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida 
#so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat 
#ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
kino = {
        'Nodir':['3 savdoyi','Lyusi','Stiv Jobs'],
        'Fozil':['Baron', 'Jasur', 'Temur'],
        'Abduqodir':['Jannat',"Payg'ambar oshig'i Hasan",'Risolat'],
        'Yusuf':['Ichkarida','Qashqirlar makoni','Shaytanat'],
        'Asliddin':['Ilhaq',"O'zbek qizi",'Sotqin']
        }

for e, f in kino.items():
    print(f"\n{e}ning sevimli kinolari:")
    for nomi in f:
        print(nomi)

#Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar 
#haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida 
#ma'lumotni konsolga chiqaring.
davlatlar = {
    "O'zbekiston":{
        'poytaxti':'Toshkent',
        'hududi':'448.9ming km.kv',
        'aholisi':'38mln',
        'p_birligi':"so'm"
        },
    "Turkiya":{
        'poytaxti':'Anqara',
        'hududi':'783.5ming km.kv',
        'aholisi':'87.9mln',
        'p_birligi':'lira'
        },
    'Germaniya':{
        'poytaxti':'Berlin',
        'hududi':'357ming km.kv',
        'aholisi':'83mln',
        'p_birligi':'euro'
        },
    'Yaponiya':{
        'poytaxti':'Tokio',
        'hududi':'377.9ming km.kv',
        'aholisi':'124mln',
        'p_birligi':'yen'
        },
    'Norvegiya':{
        'poytaxti':'Olso',
        'hududi':'385ming km.kv',
        'aholisi':'5.5mln',
        'p_birligi':'krone'
        }
    }
  
for kalit, qiymat in davlatlar.items():
    print(f"\n{kalit}ning poytaxti {qiymat['poytaxti']} shahri.\n"
          f"Maydoni: {qiymat['hududi']}\nAholisi: {qiymat['aholisi']}\n"
          f"Pul birligi: {qiymat['p_birligi']}")

#Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni 
#emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat 
#sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot 
#yo'q" degan xabarni chiqaring.
davlatlar = {
    "uzbekistan":{
        'poytaxti':'Toshkent',
        'hududi':'448.9ming km.kv',
        'aholisi':'38mln',
        'p_birligi':"so'm"
        },
    "turkiya":{
        'poytaxti':'Anqara',
        'hududi':'783.5ming km.kv',
        'aholisi':'87.9mln',
        'p_birligi':'lira'
        },
    'germaniya':{
        'poytaxti':'Berlin',
        'hududi':'357ming km.kv',
        'aholisi':'83mln',
        'p_birligi':'euro'
        },
    'yaponiya':{
        'poytaxti':'Tokio',
        'hududi':'377.9ming km.kv',
        'aholisi':'124mln',
        'p_birligi':'yen'
        },
    'norvegiya':{
        'poytaxti':'Olso',
        'hududi':'385ming km.kv',
        'aholisi':'5.5mln',
        'p_birligi':'krone'
        }
    }

x = input("Qaysi davlat haqida ma'lumotlarni bilishni xohlaysiz?!\n>>>").lower()
if x in davlatlar.keys():
    o = davlatlar[x]
    print(f"\n{x.title()}ning poytaxti {o['poytaxti']} shahri.\n"
          f"Maydoni: {o['hududi']}\nAholisi: {o['aholisi']}\n"
          f"Pul birligi: {o['p_birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q.") 

    
#sets
nums = [1, 2, 2, 3, 4, 4, 5]
print(set(nums))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a&b)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a-b)

users = {"ali", "vali"}

new_user = input("Login kiriting: ").lower()

if new_user in users:
    print("Kechirasiz, login band.")
    
else:
    print(f"Xush kelibsiz {new_user}")    

text = "programming"
print(set(text))   

a = {1, 2, 3}
b = {3, 4, 5} 

print(a^b)


# To'plamga element qo'shish
mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
mevalar.add("banan")
print(mevalar)
mevalar.update(["anor", "qovun"])
print(mevalar)

# Element o'chirish
mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
mevalar.discard("anjir")
print(mevalar)
mevalar.remove("banan")
print(mevalar)

sonlar = {1, 2, 3, 4, 5, 6}
sonlar.discard(7)
print(sonlar)
sonlar.remove(7)
print(sonlar)

sonlar = {1, 2, 3, 4, 5, 6}
son = sonlar.pop()
print(son)
print(sonlar)

# Jamlanma
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = A | B
print(C)
D = A.union(B)
print(D)

# Kesishma
print(A & B)
print(A.intersection(B))

# Farq
print(A - B)
print(B.difference(A))

# Simmetrik farq
print(A ^ B)
print(A.symmetric_difference(B))


ranglar = {"qizil", "oq", "yashil"}
ranglar.add("sariq")
ranglar.update(["ko'k", "qora", "pushti"])

# Umumiy elementlar
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1 & set2
print(set3)

# To'plamlar orasida farq
print(set1.difference(set2))
print(set2.difference(set1))

# Simmetrik farq
print(set1.symmetric_difference(set2))







