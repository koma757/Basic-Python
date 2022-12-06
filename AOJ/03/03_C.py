# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:19:20 2022

@author: ktom7
"""


while True:
    x,y = map(int,input().split())
    if x==0 and y==0:
        break
    if x > y:
        x,y = y,x
    print(x,y)
    