# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:50:39 2022

@author: ktom7
"""

n = int(input())
ai = list(map(int,input().split()))
ai.reverse()
for i in range(n):
    if i == n-1:
       print(ai[i])
       break
    print(ai[i],end=' ')