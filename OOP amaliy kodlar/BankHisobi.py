# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:27:26 2026

@author: Bo'ltakov Diyor
"""
class BankHisobi:
    def __init__(self, egasi_ismi, balans = 0):
        self.name = egasi_ismi
        self.money = balans
       
    def pul_qosh(self, qancha):
        self.money += qancha
        return (f"Hisobingizga {qancha}so'm qo'shildi. Balansingiz: {self.money}so'm")
    
    def pul_yech(self, summa):
        if self.money >= summa:
            self.money -= summa
            return (f"Balansingizdan {summa}so'm yechildi. Hisobingiz: {self.money}")
        else:
            return ("Hisobingizda mablag' yetarli emas.")

    def balansni_korsat(self):
        return (f"Hozirgi balansingiz {self.money}so'm.")
    
tolib = BankHisobi("Tolib")
nodir = BankHisobi("Nodir")
mansur = BankHisobi("Mansur")

print(mansur.pul_qosh(45000))
