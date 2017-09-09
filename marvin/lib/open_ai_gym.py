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
from gym import wrappers

class OpenAIGym(object):
    """
    Class to set up the Open AI Gym environment
    """
    def __init__(self, game):
        self.game_name = game
        self.max_steps = 1000
        self.max_generations = 100
        self.population_count = 42
        self.mutation_rate = 0.042
        self.env = gym.make(game)
        self.video = './videos'
        self.in_dimen = self.env.observation_space.shape[0]
        self.out_dimen = self.env.action_space.shape[0]
        self.obs_min = self.env.observation_space.low
        self.obs_max = self.env.observation_space.high
        self.action = None
        self.action_min = self.env.action_space.low
        self.action_max = self.env.action_space.high
        self.node_count = [self.in_dimen, 13, 8, 13, self.out_dimen]
        return None

    def videoMonitor(self):
        self.env = wrappers.Monitor(self.env, self.video, force='True')
        return self.env

    # Get methods
    def getGameName(self):
        return self.game_name
    def getMaxGenerations(self):
        return self.max_generations
    def getPopulationCount(self):
        return self.population_count
    def getMaxSteps(self):
        return self.max_steps
    def getMutationRate(self):
        return self.mutation_rate
    def getEnv(self):
        return self.env
    def getRender(self):
        return self.env.render()
    def getObservation(self):
        return self.env.reset()
    def getInDimen(self):
        return self.in_dimen
    def getOutDimen(self):
        return self.out_dimen
    def getObsMin(self):
        return self.obs_min
    def getObsMax(self):
        return self.obs_max
    def getAction(self):
        return self.action
    def getActionMin(self):
        return self.action_min
    def getActionMax(self):
        return self.action_max
    def getNodeCount(self):
        return self.node_count

    # Set methods
    def setGameName(self, val):
        self.game_name = val
        return None
    def setMaxGenerations(self, val):
        self.max_generations = val
        return None
    def setPopulationCount(self, val):
        self.population_count = val
        return None
    def setMaxSteps(self, val):
        self.max_steps = val
        return None
    def setMutationRate(self, val):
        self.mutation_rate = val
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
    def setAction(self, val):
        self.action = self.env.step(val)
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
    def setVideo(self, val):
        self.video = val
        return None
