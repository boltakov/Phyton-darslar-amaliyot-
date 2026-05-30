# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:34:43 2026

@author: Bo'ltakov Diyor
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"{self.ism} {self.familiya} Passport:{self.passport} "\
               f"{self.tyil}-yilda tug`ilgan"
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,kurs):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = kurs
        #self.manzil = manzil
        self.fanlar = []
        
    def __repr__(self):
        return f"Talaba: {self.ism} {self.familiya}"
    
    def __lt__(self, y):
        return self.tyil < y.tyil
    
    def __eq__(self, o):
        return self.tyil == o.tyil
    
    def __le__(self, r):
        return self.tyil <= r.tyil
    
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
   
class Fan:
    def __init__(self, fan_nomi):
        self.name = fan_nomi
        self.talabalar = []
        
        
    def add_student(self, *students):
        for s in students:
            if isinstance(s, Talaba):
                self.talabalar.append(s)
            
    def __getitem__(self, index):
        return self.talabalar[index]
    
    def __setitem__(self, index, value):
        self.talabalar[index] = value
        
    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self, student):
        if isinstance(student, Talaba):
            yangi_talabalar = self.talabalar.copy()
            yangi_talabalar.append(student)
        return yangi_talabalar
        
    def __sub__(self, id_raqam):
        for i in self.talabalar:
            if i.idraqam == id_raqam:
                q_talabalar = self.talabalar.copy()
                q_talabalar.remove(i)
                return q_talabalar   
        print(f"{id_raqam} raqamli talaba topilmadi")
        return self.talabalar
    
    def __call__(self, *value):
        if value:
            for v in value:
                self.add_student(v)
                
        
        return self.talabalar
        
talaba1 = Talaba("Farrux", "Raimov", "YO9870985", 1998, 432567, 3)
talaba2 = Talaba("Fozil", "Soipov", "AD8761232", 2004, 904562, 1)
talaba3 = Talaba("Tolib", "Yusupov", "QE4532167", 2002, 897632, 4)
talaba4 = Talaba("Fatih", "Hamidov", "TI9805473", 2003, 789362, 2)
#print(talaba1>=talaba2)
    
fan1 = Fan("English")
fan1.add_student(talaba1,talaba2,talaba3)
fan1[0] = talaba3
fan1[2] = talaba1
#print(fan1[0])
#print(fan1[2])

#print(len(fan1))

print(fan1-432567)
print(fan1 + talaba4)

#print(fan1())
#print(fan1(talaba4))

shaxs1 = Shaxs("Oybek", "Hoshimov", "RE4356709", 2001)    
#print(shaxs1)
















