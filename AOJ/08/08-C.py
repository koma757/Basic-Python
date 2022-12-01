# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:44:50 2022

@author: ktom7
"""

count = [0 for i in range(26)]
while True:
    try:
        l = (''.join(input().split())).lower()
    except EOFError:
        break
    for s in l:
        if ord('a')<=ord(s) and ord(s)<=ord('z'):
            count[ord(s)-ord('a')] += 1
for i in range(26):
  print("{} : {}".format(chr(ord('a')+i),count[i]))