# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:39:19 2026

@author: Bo'ltakov Diyor
"""
class Tolov:
    def __init__(self, summa, sana):
        self.summa = summa
        self.sana = sana
        
    def tolov_qil(self):
        print("To'lov Amalga oshirilmoqda...")
        
    def chek(self):
        print(f"{self.sana} sanasida, {self.summa} so'm miqdorida to'lov "
              "amalga oshirildi.")

class KartaTolov(Tolov):
    """Tolovdan voris olayapti"""
    def __init__(self, summa, sana, karta_raqam):
        super().__init__(summa, sana)
        self.karta_raqam = karta_raqam
        
    def tolov_qil(self):
        print(f"Karta orqali {self.summa}so'm to'landi. Karta: {self.karta_raqam}")
        
    def chek(self):
        print(f"Chek: {self.summa}. {self.sana}. Karta orqali.")
        
class NaqdTolov(Tolov):
    """Tolovdan voris olayapti"""
    def __init__(self, summa, sana):
        super().__init__(summa, sana)
        
    def tolov_qil(self):
        print(f"Naqd {self.summa}so'm to'landi.")
        
    def chek(self):
        print((f"Chek: {self.summa}. {self.sana}. Naqd")) 
        
class OnlineTolov(Tolov):
    """Tolovdan voris olayapti"""
    def __init__(self, summa, sana, ilova):
        super().__init__(summa, sana)
        self.ilova = ilova
    
    def tolov_qil(self):
        print(f"{self.ilova} orqali {self.summa}so'm to'landi.")
        
    def chek(self):
        print((f"Chek: {self.summa}. {self.sana}. {self.ilova} orqali")) 
        
karta = KartaTolov(340000, "25.05.2026", 8600329845632135)
naqd =NaqdTolov(470000, "20.05.2026")
online = OnlineTolov(600000, "23.04.2026", "Alif")
   
tolovlar = [karta, naqd, online]
for t in tolovlar:
    t.tolov_qil()
    t.chek()
    print("-----")     
        
        
        
        
        
        
        
        
        
        
        
        
        