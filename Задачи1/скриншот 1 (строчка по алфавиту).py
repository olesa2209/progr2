# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:28:51 2024

@author: Pupil
"""
b=[]
c=[]
a='dd fh le yyy yyy yyy aaa'
a=a.split()
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
    b.append(a[i])
for i in range(len(c)):
    a.remove(c[i])
a=sorted(a)
print(a)