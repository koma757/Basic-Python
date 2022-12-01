# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:26:55 2022

@author: ktom7
"""
s = int(input())
h = s//3600
m = (s-3600*h)//60
s = s%60
print("%d:%d:%d"%(h,m,s))