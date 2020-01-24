#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:18:07 2018

@author: danamulligan
"""

def shorten(name):
    name_list = name.split(' ')
    length = len(name_list)
    if length > 1:
        name_short = name_list[0] + ' ' + name_list[length - 1]
    else:
        name_short = name_list[0]
    return name_short

def shorrten(name):
    name_list = name.split(' ')
    length = len(name_list)
    new = name_list[0]
    if length > 1:
        new += ' ' + name_list[length - 1]
    return new