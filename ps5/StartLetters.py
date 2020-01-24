#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:47:06 2018

@author: danamulligan
"""

def howManyLetters(phrase):
    phrase = phrase.lower()
    d = {}
    list_p = phrase.split(' ')
    count = 0
    if len(phrase) > 0:
        for k in range(len(list_p)):
            if list_p[k][0] not in d:
                d[list_p[k][0]] = 1
            else:
                d[list_p[k][0]] += 1
    count = len(d)
    return count