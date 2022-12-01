# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:28:09 2022

@author: ktom7
"""

a,b,c = map(int,input().split())
count = 0
for i in range(a,b+1):
    if c%i == 0:
        count += 1
print(count)     