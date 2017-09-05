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
    Overall properties of a generation of species/population.
    """
    def __init__(self):
        self.avg_fit = 0.0
        self.min_fit =  1000000
        self.max_fit = -1000000
        self.max_neural_net = None
        self.total_reward = 0
        self.action = None
        self.best_neural_nets = []
        return None

    # Get methods
    def getAvgFit(self):
        return self.avg_fit
    def getMinFit(self):
        return self.min_fit
    def getMaxFit(self):
        return self.max_fit
    def getMaxNeuralNet(self):
        return self.max_neural_net
    def getTotalReward(self):
        return self.total_reward
    def getAction(self):
        return self.action
    def getBestNeuralNets(self):
        return self.best_neural_nets

    # Set methods
    def setAvgFit(self, val):
        self.avg_fit = val
        return None
    def setMinFit(self, val):
        self.min_fit = val
        return None
    def setMaxFit(self, val):
        self.max_fit = val
        return None
    def setMaxNeuralNet(self, val):
        self.max_neural_net = val
        return None
    def setTotalReward(self, val):
        self.total_reward = val
        return None
    def setAction(self, val):
        self.action = val
        return None
    def setBestNeuralNets(self, val):
        self.best_neural_nets = val
        return None
