# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:22:43 2026

@author: Bo'ltakov Diyor
"""
class Book:
    def __init__(self, name, author, pages, year):
        self.name = name
        self.author = author
        self.pages = pages
        self.year = year
        
    def __repr__(self):
        return f"{self.author}ning {self.name} kitobi {self.pages} sahifadan" \
                " iborat."
   
    def __lt__(self, second):
        return self.year < second.year
    
    def __eq__(self, s_book):
        if isinstance(s_book, Book):
            return self.name == s_book.name
                
            
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, *book):
        for b in book:
            self.books.append(b)
    
    def __len__(self):
        return len(self.books)
    
    def __getitem__(self, index):
        return self.books[index]
    
    def __add__(self, add_book):
        if isinstance(add_book, Book):
            self.add_book(add_book)
        return self.books
        
    def __sub__(self, book_name):
        for book in self.books:
            if book.name == book_name:
                n_book = self.books.copy()
                n_book.remove(book)
                return n_book
            
        print(f"{book_name} topilmadi.")
        return self.books
    
    def __call__(self, author):
       if author:
           return [b for b in self.books if b.author == author]
       else:
           return self.books
        
    def __repr__(self):
        return f"Bizning {self.name} kutubxonamizda hozirgi vaqtda "\
               f"{len(self.books)}ta kitoblarimiz bor."
               
b1 = Book("Atom Odatlar", "James Klear", 360, 2019)
b2 = Book("O'tgan Kunlar", "Abdulla Qodiriy", 540, 2023)
b3 = Book("Men", "Fotih Duman", 280, 2022)
b4 = Book("Beparvolik", "Mark Menson", 186, 2023)

l1 = Library("Ilm nuri")
l1.add_book(b1, b2, b3)

print(len(l1))

print(l1[0])
   
print(b1 > b2)

print(b2 == b3) 
    
print(l1 + b4) 

print(l1-'Men') 
    
print(l1("Mark Menson"))

print(l1)
    
    
    
    
    
    
    
    