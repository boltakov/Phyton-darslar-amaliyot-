# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:29:00 2026

@author: Bo'ltakov Diyor
"""
class Auto:
    def __init__(self, model, rang, karobka, narx, km):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.yil = 2025
        self.km = km

    def get_info(self):
        print(f"{self.rang.title()} {self.model} {self.karobka} karobka, narxi - {self.narx} so'm, "
              f"{self.yil}-yil ishlab chiqarilgan, {self.km} km yurgan.")
        
    def update_km(self, yurgan):
        """km qo'shadi"""
        self.km += yurgan
        return self.km
    
   
cobalt = Auto("Cobalt", "oq", "avtomat", 90000000, 34000)
cobalt.get_info()
   
class Autosalon:
    def __init__(self, salon_nomi, manzili, automobil, ishchilar_soni):
        self.name = salon_nomi
        self.address = manzili
        self.workers = ishchilar_soni
        self.cars = [automobil]
        
    def add_cars(self, auto):
        return self.cars.append(auto)
    
    def get_info(self):
        mashina = ", ".join(self.cars)
        return (f"Autosalonimiz nomi - {self.name}, u {self.address}da "
                f"joylashgan, bizning {self.workers}ta xodimdan iborat "
                f"jamoamiz {mashina} automobillarini sizga taqdim etadi.")
    
vodiy = Autosalon("Yevropa", "Hasanboy 12","BYD K5", 29)    
vodiy.add_cars("BMW 4")
#print(vodiy.get_info())
        
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

"""class yoki obyektni metodlari va xususiyatlarini chiqarib beradi"""
print(see_methods(vodiy))
print(see_methods(Auto))

"""obyektni xususiyatlarini lug'at ko'rinishi chiqarib beradi __dict__"""
print(vodiy.__dict__)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    