# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:46:39 2026

@author: Bo'ltakov Diyor
"""
class Hayvon:
    def __init__(self, turi, ismi, yoshi):
        """Hayvonlar haqida ma'lumot beradi"""
        self.type = turi
        self.name = ismi
        self.age = yoshi
        
    def ovqatlantir(self, food_name):
        print(f"{self.name}ga {food_name} bering.")
        
    def tovush(self):
        print("...")
        
class It(Hayvon):
    """Hayvondan voris olayapti"""
    def __init__(self, turi, ismi, yoshi, tugilgan_joyi):
        super().__init__(turi, ismi, yoshi)
        self.t_joyi = tugilgan_joyi
        
    def tovush(self):
        print("Vov-vov")
        
class Mushuk(Hayvon):
    """Hayvondan voris olayapti"""
    def __init__(self, turi, ismi, yoshi, tugilgan_joyi):
        super().__init__(turi, ismi, yoshi)
        self.t_joyi = tugilgan_joyi
        
    def tovush(self):
        print("Miyov-miyov")
  
class Qush(Hayvon):
    """Hayvondan voris olayapti"""
    def __init__(self, turi, ismi, yoshi, tugilgan_joyi):
        super().__init__(turi, ismi, yoshi)
        self.t_joyi = tugilgan_joyi
        
    def tovush(self):
        print("qag'- qag'")
        
        
it = It("apcharka", "reks", 3, "Nyu-York")
mushuk = Mushuk("Britaniskiy", "lazze", 2, "Qozoqiston")
burgut = Qush("burgut", "snayper", 6, "Samarqand")

tovushlar = [it, mushuk, burgut]
for t in tovushlar:
    t.tovush()





















