#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generation.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 01:36:04 by jaleman           #+#    #+#              #
#    Updated: 2017/09/05 01:36:05 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Generation(object):
    """
    ..........
    """
    avg_fit = 0.0
    min_fit =  1000000
    max_fit = -1000000
    max_neural_net = None
    total_reward = 0
    action = None
    best_neural_nets = []
