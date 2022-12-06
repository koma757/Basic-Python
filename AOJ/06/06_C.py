# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:27:14 2022

@author: ktom7
"""

n = int(input())
house = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
for i in range(n):
  b,f,r,v =map(int,input().split())
  house[b-1][f-1][r-1] += v
    
for b in range(4):
  for f in range(3):
    h_str = [str(i) for i in house[b][f]]
    print("",end="")
    print(""," ".join(h_str))
  if b == 3:
    break
  print("#"*20)