#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utilities.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 01:37:44 by jaleman           #+#    #+#              #
#    Updated: 2017/09/05 01:37:45 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def map_range(value, leftMin, leftMax, rightMin, rightMax):
    """
    Gets the range of a map.
    """

    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def normalize_array(aVal, aMin, aMax):
    """
    Normalize arrays.
    """

    res = []
    for i in range(len(aVal)):
        res.append(mapRange(aVal[i], aMin[i], aMax[i], -1, 1))
    return res

def scale_array(aVal, aMin, aMax):
    """
    Scale arrays.
    """

    res = []
    for i in range(len(aVal)):
        res.append(mapRange(aVal[i], -1, 1, aMin[i], aMax[i]))
    return res

def debug_object(object):
    """
    Print an object and exits the program.
    """

    print (object)
    exit(42)
