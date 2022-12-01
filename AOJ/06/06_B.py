# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:51:27 2022

@author: ktom7
"""

n= int(input())
num=[[int(i) for i in range(1,14)] for j in range(4)]
pattern = ['S','H','C','D']
for i in range(n):
    card = list(input().split())
    if card[0]==pattern[0]:
        num[0].remove(int(card[1]))
    elif card[0]==pattern[1]:
        num[1].remove(int(card[1]))
    elif card[0]==pattern[2]:
        num[2].remove(int(card[1]))
    elif card[0]==pattern[3]:
        num[3].remove(int(card[1]))
for i in range(4):
    for j in range(len(num[i])):
        print(pattern[i],num[i][j])