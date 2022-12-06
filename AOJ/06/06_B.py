# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:51:27 2022

@author: ktom7
"""

n= int(input())
num_list=[[int(i) for i in range(1,14)] for j in range(4)]
pattern = ['S','H','C','D']
for i in range(n):
    char,num = list(input().split())
    if char==pattern[0]:
        num_list[0].remove(int(num))
    elif char==pattern[1]:
        num_list[1].remove(int(num))
    elif char==pattern[2]:
        num_list[2].remove(int(num))
    elif char==pattern[3]:
        num_list[3].remove(int(num))
for i in range(4):
    for j in range(len(num_list[i])):
        print(pattern[i],num_list[i][j])