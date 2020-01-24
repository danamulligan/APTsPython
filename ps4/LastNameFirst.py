#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:55:54 2018

@author: danamulligan
"""

def modify(name):
    l = name.split(' ')
    out = out = l[-1] + ', ' + l[0]
    initial = ''
    if len(l) == 1:
        out = name
    elif len(l) > 2:
        for k in range(1, len(l)-1):
            initial = l[k][0]
            out += ' ' + initial
            if len(l[k]) > 1:
                out += '.'
    return out