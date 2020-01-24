#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:12:18 2018

@author: danamulligan
"""

def check(word):
    new = word.replace('pi', 'xx')
    counter = 0
    new_list = list(new)
    for k in new_list:
        if k == 'x':
            counter += 1
    new = word.replace('ka', 'xx')
    new_list = list(new)
    for k in new_list:
        if k == 'x':
            counter += 1
    new = word.replace('chu', 'xxx')
    new_list = list(new)
    for k in new_list:
        if k == 'x':
            counter += 1
    if counter == len(word):
        return "YES"
    else:
        return "NO"
    