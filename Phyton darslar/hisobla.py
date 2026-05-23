# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:56:51 2026

@author: Bo'ltakov Diyor
"""
'''
def yigindi(a, b, *sonlar):
    c = a+b
    if sonlar:
       for son in sonlar:
           c+=son
    return c

def kopaytma(a, b, *sonlar):
    c = a*b
    if sonlar:
        for son in sonlar:
            c *= son
    return c  

def ortacha(a, b, *sonlar):
    c = a + b
    d = 2
    if sonlar:
        for son in sonlar:
            c += son
            d += 1
    return c / d
'''
def yigindi(*sonlar):
    return sum(sonlar)

def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

def ortacha(*sonlar):
    return sum(sonlar) / len(sonlar)