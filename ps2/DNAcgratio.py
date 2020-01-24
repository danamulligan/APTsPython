#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 12:33:10 2018

@author: danamulligan
"""

def ratio(dna):
    counter = 0 
    total = len(dna)
    for k in dna:
        if k == 'g' or k == 'c':
            counter += 1
    return counter/total