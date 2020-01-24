#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:20:40 2018

@author: danamulligan
"""

def networth(transactions):
    lt = []
    d = {}
    
    for k in transactions:
        lt = k.split(":")
        for s in range(2):
            if s == 0: 
                if lt[s] not in d:
                    d[lt[s]] = float(lt[2]) * -1
                elif lt[s] in d:
                    d[lt[s]] -= float(lt[2])
            if s == 1:
                if lt[s] not in d:
                    d[lt[s]] = float(lt[2])
                elif lt[s] in d:
                    d[lt[s]] += float(lt[2])
                    
    out = [0] * len(d)
   # string = ''
    count = 0
    
    for k in d: 
        for s in range(len(d)):
            if count == s:
                out[s] = str(k) + ":" + str(round(d[k], 2))  
        count += 1   
        
    return sorted(out)