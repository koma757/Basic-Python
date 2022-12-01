# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:48:46 2022

@author: ktom7
"""

while True:
    l = input()
    sum = 0
    if int(l)==0:
        break
    for s in l:
        sum += int(s)
    print(sum)
        