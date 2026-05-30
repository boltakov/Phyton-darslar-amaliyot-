# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:09:48 2026

@author: Bo'ltakov Diyor
"""
class Shaxs:
    __num_shaxs = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil,jinsi,millati,yashash_joyi):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__millat = millati
        self.__jinsi = jinsi
        self.__y_joyi = yashash_joyi
        Shaxs.__num_shaxs += 1
        
    @classmethod
    def get_num_shaxs(cls):
        return cls.__num_shaxs
    
    def get_country(self):
        return self.__y_joyi
    
    def set_new_country(self, yangi_davlat):
        self.__y_joyi = yangi_davlat
        return self.__y_joyi
        
    def get_gender(self):
        return(self.__jinsi)
        
    def get_nationality(self):
        return(self.__millat)
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
class Talaba(Shaxs):
    __num_talaba = 0
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil, jinsi, millati,yashash_joyi):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil, jinsi, millati,yashash_joyi)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        Talaba.__num_talaba += 1
        
    @classmethod
    def get_num_students(cls):
        return cls.__num_talaba
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
            
    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz.")
               
        

talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil,"erkak", "o'zbek", "O'zbekiston")

talaba1_manzil = Manzil(32, "Yusuf Ota", "Payariq", "Samarqand")
talaba1 = Talaba("Maruf", "Fozilov", "BA0987893", 2005, "345600", talaba1_manzil, "erkak", "o'zbek","O'zbekiston")
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
