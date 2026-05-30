# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:57:12 2026

@author: Bo'ltakov Diyor
"""
class BankHisob:
    __jami_hisoblar = 0
    def __init__(self, egasi, hisob_raqam, pin_kod, balans = 0):
        self.egasi = egasi
        self.hisob_raqam = hisob_raqam
        self.__pin_kod = pin_kod
        self.__balans = balans
        self.__tranzaksiyalar = []
        BankHisob.__jami_hisoblar +=1
        
    def pul_qosh(self, summa):
        self.__balans += summa
        self.__tranzaksiyalar.append(f"+ {summa} so'm")
        return self.__balans
    
    def pul_yech(self, summa, pin):
        if self.__balans > summa:
            if self.__pin_kod == pin:
                self.__balans -= summa
                self.__tranzaksiyalar.append(f"- {summa} so'm")
                print(self.__balans)
            else:
                print("Pin-kodni xato terdingiz.")
        else:
            print("Balansingizda mablag' yetarli emas")
    
    def get_balans(self, pin):
        if pin == self.__pin_kod:
            print(self.__balans)
        else:
            print("Pin-kodni xato terdingiz.")
            
    def get_tranzaksiyalar(self):
        return self.__tranzaksiyalar
    
    @classmethod
    def get_jami_hisoblar(cls):
        return cls.__jami_hisoblar
    
nodir = BankHisob("Nodir", 9823243565789743, 2354)
maruf = BankHisob("Maruf", 1234567891234567, 2345)

print(nodir.pul_qosh(20000))
print(maruf.pul_qosh(40000))

nodir.pul_yech(15000, 1234)
maruf.pul_yech(25000, 2345)

nodir.get_balans(2354)
maruf.get_balans(4356)
    
print(maruf.get_tranzaksiyalar())

print(BankHisob.get_jami_hisoblar())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    