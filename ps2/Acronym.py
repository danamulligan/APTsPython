#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:50:06 2018

@author: danamulligan
"""

def acronym(phrase):
    l = phrase.split(' ')
    acro = ""
    for k in range(len(l)):
        for m in range(len(l[k])):
            if m == 0:
                acro += l[k][m]
    return acro