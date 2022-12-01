# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:46:56 2022

@author: ktom7
"""

W,H,x,y,r=map(int,input().split())
if ((x>=r)and(x<=H-r)and(y>=r)and(y<=H-r)):
    print("Yes")
else:
    print("No")