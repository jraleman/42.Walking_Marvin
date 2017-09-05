#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    open_ai_gym.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 01:36:10 by jaleman           #+#    #+#              #
#    Updated: 2017/09/05 01:36:11 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import gym

class OpenAIGym(object):
    """
    Class to set up the Open AI Gym environment
    """
    def __init__(self, game):
        self.env = gym.make(game)
        self.observation = env.reset()
        self.in_dimen = env.observation_space.shape[0]
        self.out_dimen = env.action_space.shape[0]
        self.obs_min = env.observation_space.low
        self.obs_max = env.observation_space.high
        self.action_min = env.action_space.low
        self.action_max = env.action_space.high
        # Why 13, 8 and 13??? lol!
        self.node_count = [in_dimen, 13, 8, 13, out_dimen]
        return None

    # Get methods
    def getEnv(self):
        return self.env
    def getObservation(self):
        return self.observation
    def getInDimen(self):
        return self.in_dimen
    def getOutDimen(self):
        return self.out_dimen
    def getObsMin(self):
        return self.obs_min
    def getObsMax(self):
        return self.obs_max
    def getActionMin(self):
        return self.action_min
    def getActionMax(self):
        return self.action_max
    def getNodeCount(self):
        return self.node_count

    # Set methods
    def setEnv(self, val):
        self.env = val
        return None
    def setObservation(self, val):
        self.observation = val
        return None
    def setInDimen(self, val):
        self.in_dimen = val
        return None
    def setOutDimen(self, val):
        self.out_dimen = val
        return None
    def setObsMin(self, val):
        self.obs_min = val
        return None
    def setObsMax(self, val):
        self.obs_max = val
        return None
    def setActionMin(self, val):
        self.action_min = val
        return None
    def setActionMax(self, val):
        self.action_max = val
        return None
    def setNodeCount(self, val):
        self.node_count = val
        return None