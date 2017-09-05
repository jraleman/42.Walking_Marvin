#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import time

def map_range(value, leftMin, leftMax, rightMin, rightMax):
    """
    ...
    """
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.

    return rightMin + (valueScaled * rightSpan)


def normalize_array(aVal, aMin, aMax):
    """
    ...
    """
    res = []
    for i in range(len(aVal)):
        res.append( mapRange(aVal[i], aMin[i], aMax[i], -1, 1) )
    return res

def scale_array(aVal, aMin, aMax):
    """
    ...
    """
    res = []
    for i in range(len(aVal)):
        res.append( mapRange(aVal[i], -1, 1, aMin[i], aMax[i]) )
    return res

def debug_object(object):
    """
    ...
    """
    print (object)
    exit(42)
