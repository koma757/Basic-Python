# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:45:37 2022

@author: ktom7
"""
while True:
    a,op,b = input().split()
    a,b = map(int,(a,b))
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a//b)
    elif op == '?':
        break 