# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:48:17 2024

@author: Pupil
"""

class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        if self.name != 'Николай':
            print('Я не ' + self.name + ', а Николай' + ". Мне " + self.age)
        else:
            print ('Я '+ self.name + ". Мне " + self.age)
            
name1 = Nikola("Петя",'3')
name2 = Nikola("Николай", "32")
name3 = Nikola("Гоша","52")

name2.show()


