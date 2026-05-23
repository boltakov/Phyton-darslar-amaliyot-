# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:21:42 2026

@author: Bo'ltakov Diyor
"""

import random as r 

from words_list import words

def get_word():
    word = r.choice(words)
    print(f"Men {len(word)} xonali so'z o'yladim topa olasizmi?")
    soz = []
    for harf in word:
        soz.append('_')
    
    print(' '.join(soz))   
    return word, soz


def harf_qabul():
    harf = input("\nHarf kiriting: ").lower()

    return harf


def tekshir(harf, word, soz, harflar):
    if harf in harflar:
        print("Bu harfni oldin kiritgansiz.")
    elif harf in word:
        harflar.append(harf)
        for i in range(len(word)):
            if word[i] == harf:
                soz[i] = harf 
    else:
        harflar.append(harf)
        print("Bu harf yashirin so'zga tegishli emas.")
        print("Kiritgan harflaringiz: ", end="") 
        print((', '.join(harflar)))        
    
  
def play():
    harflar = []  
    word, soz = get_word()
    harf = harf_qabul()
    tekshir(harf, word, soz, harflar)
    n = 0
    while '_' in soz:
       print(' '.join(soz))
       harf = harf_qabul()
       tekshir(harf, word, soz, harflar)
       n += 1
       if '_' not in soz:
          break
    print(f"Tabriklayman, siz {word} so'zini {n}ta urinishda topdingiz.")   
    
    
play()
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    