#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:21:59 2018

@author: danamulligan
"""

def decrypt(library, message):
    length_lib = len(library)
    dict_list = [0,0]
    split_mes = message.split(" ")
    length_mes = len(split_mes)
    strd = ''
    d = {}
    decoded = ''
    for k in range(0, length_lib):
        strd = library[k]
        dict_list = strd.split(' ')
        for n in range(0,2):
            if n == 0:
                d[dict_list[1]] = dict_list[n]
    for m in range(0, length_mes):
        decoded += d.get(split_mes[m], '?')
    return decoded