# -*- coding: utf-8 -*-
"""
Created on Sat May 16 13:02:31 2026

@author: Bo'ltakov Diyor
Son o'yini. Avval kompyuter son o'ylaydi foydalanuvchi topadi,
keyin foydalanuvchi son o'ylaydi kompyuter topadigan dastur.' 
"""
import random as r

def son_top(x = 10):
    print(f"1dan {x}gacha son o'yladim topa olasizmi?")
    q_son = r.randint(1, x)
    n = 0
    while True:
        son = int(input(">>>"))
        n+=1
        if son > q_son:
            print("Men bundan kichikroq son o'ylagan edim.")
        elif son < q_son:
            print("Men bundan kattaroq son o'ylagan edim")
        else:
            print(f"Tabriklayman, {n}ta urinishda to'g'ri topdingiz.")
            break
    return n    
  
def son_topaman(x = 10):
    past = 1
    yuqori = x
    num = 0
    print(f"\nEndi siz 1dan {x}gacha bo'lgan son o'ylang men topaman.")
    input("\nAgar o'ylagan bo'lsangiz istalgan tugmani bosing.")
    while True:
            com_son = r.randint(past, yuqori)
            print(com_son)
            num +=1
            user_son = input("Agar siz o'ylagan son bundan katta bo'lsa(+), "
                             "kichik bo'lsa(-), agar to'g'ri bo'lsa(t)"
                             "belgisini qoldiring\n>>>").lower()
            if user_son == '+':
                past = com_son + 1
            elif user_son == '-':
                yuqori= com_son - 1
            else:
                print(f"Men {num}ta urinishda topdim.")
                break
    return num   

def play(a):          
    while True:
        n = son_top(a)
        num = son_topaman(a)
        if num > n:
            print("O'yinda siz g'alaba qozondingiz.")
        elif num < n:
            print("O'yinda men g'alaba qozondim")
        else:
            print("Durrang! 🤝")
        
        value = int(input("O'yinni davom ettirishni xohlaysizmi ha(1) yoki"
                      "yo'q(0)\n>>>"))
        if value ==0:
           break
       
        
play(167)       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
         

