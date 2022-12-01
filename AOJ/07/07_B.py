# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:39:34 2022

@author: ktom7
"""

while True:
  n,x = map(int,input().split())
  if n==0 and x==0:
      break
  count=0
  for k in range(3,n+1):
      for i in range(2,k):
          for j in range(1,i):
              if k+i+j == x:
              	count +=1
  print(count)