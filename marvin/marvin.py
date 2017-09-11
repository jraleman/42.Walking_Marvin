#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    marvin.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/29 23:48:00 by jaleman           #+#    #+#              #
#    Updated: 2017/08/29 23:48:01 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Walking Marvin

Uses OpenAI Gym with an environment called Marvin.
The goal is to train Marvin to walk, having the training and walking process.
"""

# Project's Metadata
__author__ = "jraleman, corezip"
__version__ = "0.1.0"
__license__ = "MIT"

# Marvin dependencies
import gym
import copy
import pickle
import numpy as np
from lib.enviroment import Marvin
from lib.open_ai_gym import OpenAIGym

# NeuralNetwork dependencies
from lib.neural_net import NeuralNet
from lib.population import Population
from lib.generation import Generation

# Modules to parse flags, save logs, and aux functions.
from lib.flags import MarvinFlags
from lib.utilities import map_range, normalize_array, scale_array, debug_object

# Global variables.
GAME_NAME = 'Marvin-v0'
FILE_NAME = 'weights.plk'
MAX_STEPS = 1000
MAX_GENERATIONS = 100
POPULATION_COUNT = 420
MUTATION_RATE = 0.042

def global_values(flg):
    """
    Change global variables values depending on the flags given.
    """
    global GAME_NAME
    global MAX_STEPS
    global MAX_GENERATIONS
    global POPULATION_COUNT
    global MUTATION_RATE
    global FILE_NAME

    if flg.getFlagName() != None:
        GAME_NAME = flg.getFlagName()
    if flg.getFlagMove() != 0:
        MAX_STEPS = flg.getFlagMove()
    if flg.getFlagGen() != 0:
        MAX_GENERATIONS = flg.getFlagGen()
    if flg.getFlagPop() != 0:
        POPULATION_COUNT = flg.getFlagPop()
    if flg.getFlagRate() != 0.0:
        MUTATION_RATE = flg.getFlagRate()
    if flg.getFlagSave() != None:
        FILE_NAME = flg.getFlagSave()
    elif flg.getFlagLoad() != None:
        FILE_NAME = flg.getFlagLoad()
    return None

def main(flg):
    """
    Main entry point of the program.
    """

    if flg != None:
        global_values(flg)
    ai_gym = OpenAIGym(GAME_NAME)
    gen = Generation()
    pop = Population(POPULATION_COUNT, MUTATION_RATE, ai_gym.getNodeCount())
    net = NeuralNet(ai_gym.getNodeCount())
    best_neural_nets = gen.getBestNeuralNets()

    # Loads the weights and exit the program.
    if flg.getFlagLoad() != None:
        #try:
        best_neural_nets = pickle.load(open(FILE_NAME, "rb"))
        flg.loadWeights(best_neural_nets, steps, ai_gym)
        #except:
        #    print ("Error loading file! Are you sure it exists?")
        #    exit(-1)

    # Loop for each generation
    for gen in range(MAX_GENERATIONS):
        avg_fit = 0.0
        min_fit =  1000000
        max_fit = -1000000
        max_neural_net = None
        # Loop for each species in the generation
        for nn in pop.population:
            total_reward = 0
            observation = ai_gym.getObservation()
            # Loop for every step taken by Marvin
            for step in range(MAX_STEPS):
                if flg.getFlagWalk() == True:
                    ai_gym.getRender()
                ai_gym.setAction(nn.getOutput(observation))
                observation, reward, done, info = ai_gym.getAction()
                if flg.getFlagQuiet() == False:
                    print ("Step        : %d" % step)
                    print ("Reward      : %f" % reward)
                    print ("Total Reward: %f" % total_reward)
                    print ("Generation  : %d" % gen)
                    print (observation)
                    print ("-----\n")
                total_reward += reward
                if done:
                    break
            nn.fitness = total_reward
            min_fit = min(min_fit, nn.fitness)
            avg_fit += nn.fitness
            if  nn.fitness > max_fit:
                max_fit = nn.fitness
                max_neural_net = copy.deepcopy(nn)
        best_neural_nets.append(max_neural_net)
        avg_fit /= pop.getPopulationCount()
        pop.createNewGeneration(max_neural_net)
        if flg.getFlagLog == True:
            saveLog(flg, gen, min_fit, avg_fit, max_fit)
    if flg.getFlagSave() != None:
        pickle.dump(best_neural_nets, open(FILE_NAME, "wb"))
    if flg.getFlagVideo() != None:
        flg.saveVideo(best_neural_nets, steps, ai_gym)

if __name__ == "__main__":
    """
    This is executed when run from the command line.
    """

    flg = MarvinFlags(GAME_NAME, __version__)
    flg.initFlags()
    main(flg)
