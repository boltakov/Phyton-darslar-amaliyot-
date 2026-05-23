# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:08:29 2026

@author: Bo'ltakov Diyor
"""
#Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning 
#xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni 
#kiriting (ism, foydalanuvchi ismi, email, va hokazo)
class User:
    def __init__(self, ism, foydalanuvchi, email, kod):
        self.name = ism
        self.username = foydalanuvchi
        self.email = email
        self.password = kod
        
#Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi 
#haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: 
#"Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).        
    def get_info(self):
        return (f"Ismi: {self.name}, foydalanuvchi ismi: {self.username},"
                f"profil kodi: {self.password}, foydalanuvchi emaili: {self.email}")
        

diyor = User("Diyor", "boltakov_diyor", "boltakovdiyor99gmail.com", 123456778)
javohir = User("Javohir", "Java.here", "ibrohimov90gmail.com", 20042004)
baxtiyor = User("Baxtiyor", "Baxtiyorali_01", "baxtijan", 12344321)

print(diyor.get_info())

    
     
        
     
        
     
        
     
        
     
        
     
        


        
        