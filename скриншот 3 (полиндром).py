# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:31:45 2024

@author: Pupil
"""

a='коту тащат уток'
for i in range(len(a)):
    a=a.replace(' ','')
    a=a.replace('.','')
    a=a.replace('!','')
    a=a.replace(',','')
b=a[::-1]
if b==a:
    print('это полиндром')