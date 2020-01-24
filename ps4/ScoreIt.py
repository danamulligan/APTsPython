#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:45:14 2018

@author: danamulligan
"""

def maxPoints(toss):
    count = [0, 0, 0, 0, 0, 0]
    for k in toss:
        if k == 1:
            count[0] += 1
        if k == 2:
            count[1] += 1
        if k == 3:
            count[2] += 1
        if k == 4:
            count[3] += 1
        if k == 5:
            count[4] += 1
        if k == 6:
            count[5] += 1
    for k in range(1, 7):
        count[k - 1] *= k
    max_num = max(count)
    return max_num