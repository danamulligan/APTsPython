#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:01:02 2018

@author: danamulligan
"""

def lovely(ingredients, inedible):
    ingr_list = ingredients.split(' ')
    ined_list = inedible.split(' ')
    len_ingr = len(ingr_list)
    len_ined = len(ined_list)
    count = len_ingr
    for k in range(0, len_ined):
        for n in range(0, len_ingr):
            if str(ined_list[k]) == str(ingr_list[n]):
                    count -= 1
    return count