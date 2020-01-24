#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:21:08 2018

@author: danamulligan
"""
def count(a, b):
    count = 0
    statement = False
    la = len(a)
    lb = len(b)
    
    for k in range(la):
        for r in range(lb):
            if a[k] == b[r]:
                statement = True
                a = change(a, k)
                b = change(b, r)
        if statement == True:
            count += 1
        statement = False
        
    return count
                
def change(string, n):
    re = ''
    for k in range(len(string)):
        if k == n:
            re += '!'
        else:
            re += string[k]
    return re