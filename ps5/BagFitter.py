#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:38:26 2018

@author: danamulligan
"""
def bags(strength, food):
    d = {}
    num = 0
    rem = 0
    count = 0
    for k in food:
        if k not in d:
            d[k] = 1
        else:
            d[k] += 1
    for k in d:
        num = d[k]
        rem = num % strength
        count += num // strength
        if rem != 0:
            count += 1
            
    return count