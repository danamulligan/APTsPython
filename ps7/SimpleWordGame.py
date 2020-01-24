#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:00:33 2018

@author: danamulligan
"""

def points(player, dictionary):
    count = 0
    k_list = {}
    for k in range(len(player)):
        if player[k] in dictionary:
            if player[k] not in k_list:
                k_list[player[k]] = len(player[k]) ** 2
                count += len(player[k]) ** 2
    return count