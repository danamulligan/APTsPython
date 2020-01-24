#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 12:40:55 2018

@author: danamulligan
"""

def combine(first,flen,second,slen):
    length = flen + slen
    final = [0] * length
    counter = 0
    end = len(second)
    for k in range(0, flen):
        final[k] = first[k]
        counter += 1
    for n in range(slen, 0, -1):
        final[counter] = second[end - n]
        counter += 1
    return ''.join(final)