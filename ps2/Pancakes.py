#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 18:34:23 2018

@author: danamulligan
"""
"""
def minutesNeededs(numCakes, capacity):
    nice = 0
    time = 0
    if capacity > numCakes:
        nice = numCakes % capacity - 1
        for n in range(nice-1):
            time += 5
    for k in range(numCakes - nice):
        time += 5
    if numCakes == 0:
        time = 0
    return time
    """
def minutesNeededs(numCakes, capacity):
    time = 0
    remaining = numCakes % capacity
    print(remaining)
    perfect = numCakes - remaining
    print('new', numCakes//capacity)
    print('perf', perfect)
    full_sets = perfect // capacity
    print(full_sets)
    for k in range(full_sets):
        time += 10
        print('full', time)
    #if remaining < capacity:
    #if remaining > 0 and remaining % 2 == 0:
       # time += 10
       # print('even', time)
    #elif remaining > 0 and remaining % 2 == 1:
     #   time += 5
      #  print('odd', time)
    #elif remaining > capacity:
    if remaining <= capacity / 2 and remaining != 0:
        time += 5
    elif remaining > capacity / 2 and remaining != 0:
        time += 10
    if numCakes <= capacity and numCakes != 0:
        time = 10
    elif numCakes == 0:
        time = 0
    return time

def minutesNeeded(numCakes, capacity):
    rem = numCakes % capacity
    full = numCakes // capacity
    time = full * 10
    if numCakes == 0:
        time = 0
    elif numCakes < capacity and numCakes != 0:
        time = 10
    elif rem <= capacity / 2 and rem != 0:
        time += 5
    elif rem > capacity / 2 and rem != 0:
        time += 10
    return time