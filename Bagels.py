#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:26:54 2018

@author: danamulligan
"""

def bagelCount(orders):
    count = 0
    for k in orders:
        count += k
        if k >= 12:
            count += k // 12
    return count