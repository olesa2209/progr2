# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:58:41 2024

@author: Pupil
"""

class Soda:
    def __init__(self, dobavka):
        self.dobavka = dobavka 
        
    def show(self):
        if self.dobavka == '':
            print('Обычная газировка')
        else:
            print ('газировка', self.dobavka)
            
soda1 = Soda("dobavka1")
soda2 = Soda("dobavka2")
soda3 = Soda("")

soda2.show()

