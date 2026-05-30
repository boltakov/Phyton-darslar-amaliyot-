# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:32:00 2026

@author: Bo'ltakov Diyor
theme: VORISLIK VA POLIMORFIZM
"""
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Scientist(Shaxs):
    """Scientist klassiga Shaxs klassidan voris olamiz"""
    def __init__(self, ism, familiya, passport, tyil, faoliyati):
        """Scientist xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.faoliyati = faoliyati
        self.works = []
        
    def add_works(self, work):
        """Qilgan ishlari qo'shib boriladi"""
        self.works.append(work)
        return ", ".join(self.works)
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        tartib = ", ".join(self.works)
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan, "
        info += f"faoliyati: {tartib}"
        return info
        
class User(Shaxs):
    """Foydalanuvchi klassi Shaxsdan voris oldi"""
    def __init__(self, ism, familiya, passport, tyil, kasbi, foydalanish_vaqti):
        """User xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil) 
        self.job = kasbi
        self.use_time = foydalanish_vaqti
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan, "
        info += f"kasbi {self.job}, ilovadan foydalanish vaqti {self.use_time}"
        return info
    
class Admin(User):
    """Admin kllasi Userdan voris olayapti"""
    def __init__(self, ism, familiya, passport, tyil, kasbi, foydalanish_vaqti):
        """Admin xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil, kasbi, foydalanish_vaqti)
          
    def ban_user(self):
        print("Foydalanuvchi bloklandi.")
        
class Sotuvchi(Shaxs):
    """Sotuvchi klassi Shaxs klassidan voris oldi"""
    def __init__(self, ism, familiya, passport, tyil, ish_soati):
        """Sotuvchi klass xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.work_hour = ish_soati
        self.sotildi = []
        
    def get_sotildi(self, sotuv):
        """Sotuvchi sotgan mahsulotlar ro'yxati"""
        self.sotildi.append(sotuv)
        return ", ".join(self.sotildi)
    
    def ortacha(self):
        return len(self.sotildi) / self.work_hour
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan, "
        info += f"ish kuni {self.work_hour} soat ishlaydi va o'rtacha "
        info += f"{len(self.sotildi)}ta mahsulot sotadi."
        return info

class Mijoz(Shaxs):
    """Mijoz klassi Shaxs klassidan voris oldi"""
    def __init__(self, ism, familiya, passport, tyil):
        """Mijoz klassi xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.savat = []
        
    def get_korzinka(self, tovar):
        """Olingan mahsulotlarni savatga qo'shadi"""
        self.savat.append(tovar)
        return ", ".join(self.savat)
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        t = ", ".join(self.savat)
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan, "
        info += f"bizdan {t} kabi mahsulotlar sotib oladi."
        return info
    
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
    
class Fan:
    """Fan klassi"""
    def __init__(self, nomi, yillik_soati, teacher):
        self.name = nomi
        self.hour = yillik_soati
        self.teacher = teacher
        
matematika = Fan("Matematika", 50, "Qobilov. D")
managment = Fan("Managment", 45, "Nazarov. O")
marketing = Fan("Marketing", 52, "Oripov. U") 
english = Fan("English", 56, "Nigmatova. A")       
    

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
    
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
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
print(see_methods(Admin))





















    

