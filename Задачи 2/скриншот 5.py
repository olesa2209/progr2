# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:58:35 2024

@author: Pupil
"""

class Biblioteka:
    def __init__(self,spisok):
        self.spisok = spisok
        
    def show(self,book):
        self.spisok.append(book)
    def show1(self,book):
        self.spisok.remove(book) 
    def poisk(self,book):
        a=input('введите книгу которую хотите найти: ')
        for i in self.spisok:
            if  i==a:
                print('книга, которую вы ищете, есть в списке: ',self.spisok)
                
b=Biblioteka(['Гроза'])
b.show("Гроkgjg")
print(b.spisok)
