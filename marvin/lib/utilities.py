#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-


# 42 HEADER GOES HERE

import time

def map_range(value, leftMin, leftMax, rightMin, rightMax):
    """
    ...
    """
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def normalize_array(aVal, aMin, aMax):
    """
    ...
    """
    res = []
    for i in range(len(aVal)):
        res.append(mapRange(aVal[i], aMin[i], aMax[i], -1, 1))
    return res

def scale_array(aVal, aMin, aMax):
    """
    ...
    """
    res = []
    for i in range(len(aVal)):
        res.append(mapRange(aVal[i], -1, 1, aMin[i], aMax[i]))
    return res

def debug_object(object):
    """
    ...
    """
    print (object)
    exit(42)
