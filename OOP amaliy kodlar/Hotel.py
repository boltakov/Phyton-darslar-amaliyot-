# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:11:17 2026

@author: Bo'ltakov Diyor
"""

class Room:
    def __init__(self, raqam, turi, narxi, band = False):
        self.number = raqam
        self.type = turi
        self.price = narxi
        self.busy = band
        
    def set_busy(self):
        if self.busy == True:
            return f"{self.number}-xona band qilingan."
        else:
            self.busy = True
            return f"{self.number}-xona band qilindi."
        
    def set_empty(self):
        self.busy = False
        return f"{self.number}-xona bo'shatildi."
    
    def get_info(self):
        holat = "band" if self.busy else "bo'sh"
        return (f"{self.number}-raqamli {self.type} xonamizni narxi {self.price} "
               f"hozirda bu xonamiz {holat}.")
    
class Hotel:
    def __init__(self, nomi, manzil, xona):
        self.name = nomi
        self.address = manzil
        self.rooms = [xona]
        
    def add_room(self, room):
        return self.rooms.append(room)
    
    def empty_rooms(self):
        for room in self.rooms:
            if room.busy == False:
                print(f"{room.number}-xona bo'sh")
                
    def profit(self):
       jami = sum(room.price for room in self.rooms if room.busy == True)
       return f"Umumiy daromad {jami} so'm."
                
            
    
r1 = Room(12, "lyuks", 300000)
r2 = Room(15, "standart", 200000, True)
r3 = Room(13, "standart", 220000)
r4 = Room(14, "lyuks", 280000, True)  

h1 = Hotel("Bek", "Chelak shahri 23A", r3)
h1.add_room(r2)
h1.add_room(r1)
h1.add_room(r4)

print(r2.set_empty())
print(r1.set_busy())

print(r4.get_info())

h1.empty_rooms()

print(h1.profit())




