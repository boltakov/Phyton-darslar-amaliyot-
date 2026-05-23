# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:28:50 2026

@author: bo'ltakov Diyor
"""
class Talaba:
    def __init__(self, ism, yosh):
        self.name = ism
        self.age = yosh
        self.grade = []
        
    def baho_qosh(self, baho):
        return self.grade.append(baho)
    
    def ortacha_baho(self):
        return sum(self.grade) // len(self.grade)
    
     
class Jurnal:
    def __init__(self):
        self.student = []
        
    def talaba_qosh(self, talaba):
        return self.student.append(talaba)
    
    def hammasini_korsat(self):
        for talaba in self.student:
            print(f"{talaba.name}ning o'rtacha bahosi: {talaba.ortacha_baho()}")
        
    def yuqori_baho(self):
        yaxshiroq = max(self.student, key= lambda t: t.ortacha_baho())
        print(f"Eng yaxshi o'quvchi {yaxshiroq.name}, uning o'rtacha bahosi: "
              f"{yaxshiroq.ortacha_baho()}")
    
        
jurnal = Jurnal()

bekzod = Talaba("Bekzod", 21)
bekzod.baho_qosh(4)
bekzod.baho_qosh(5)
bekzod.baho_qosh(4)

nodir = Talaba("Nodir", 23)
nodir.baho_qosh(2)
nodir.baho_qosh(4)
nodir.baho_qosh(5)

jurnal.talaba_qosh(nodir)
jurnal.talaba_qosh(bekzod)

jurnal.hammasini_korsat()
jurnal.yuqori_baho()       
