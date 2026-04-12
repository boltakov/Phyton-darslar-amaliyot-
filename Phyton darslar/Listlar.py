# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:10:18 2026

@author: Bo'ltakov Diyor
"""
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni
#konsolga chiqaring.
davlatlar = ["O'zbekiston", "Qirg'iziston", "Qozog'iston", 'Turkiya',
             'Ozarbayjon']
print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar))

#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, 
#keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120,1200,2))

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(juft_sonlar))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang 
#va konsolga chiqaring
katta = max(juft_sonlar)
kichik = min(juft_sonlar)
print(katta-kichik)

#Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni
#konsolga chiqaring
print(juft_sonlar[:20], juft_sonlar[260:280], juft_sonlar[-20:])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'manti', 'shashlik', 'somsa', 'chuchvara']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, 
#va qo'shimcha 2 ta taom qo'shing
nonushta.remove('osh')
nonushta.remove('chuchvara')
nonushta.remove('shashlik')
nonushta.remove('manti')
nonushta.append('tuxum')
nonushta.append('quymoq')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va 
#nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non' #tuple medotda qiymatni o'zgartirib bo'lmaydi.













