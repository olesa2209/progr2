# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:55:18 2024

@author: Pupil
"""

inp = open('input.txt','r')
q = [x for x in inp.readline().split()]
m=[]
for i in range(len(q)):
   a=q.count(q[i])
   m.append(i)
print(q[max(m)])
   
   
   