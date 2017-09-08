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

# Gym AI dependencies
import gym
import copy
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
FILE_PATH = 'checkpoints/marvin-state'
MAX_STEPS = 1000
MAX_GENERATIONS = 100
POPULATION_COUNT = 420
MUTATION_RATE = 0.042

# Debug reasons
MAX_STEPS = 10
MAX_GENERATIONS = 5
POPULATION_COUNT = 2

################################################################################
# Save and load checkpoints
################################################################################

# import os
# import torch
#
# def save(net, optimizer, epoch):
#     state = {
#         'state_dict': net.state_dict(),
#         'optimizer': optimizer.state_dict(),
#         'epoch': epoch,
#     }
#     print ("Saving checkpoint to file '{}'" . format(FILE_PATH))
#     torch.save(state, FILE_PATH)
#
# def load():
#     #net = Net()
#     net = 0
#     optimizer = optim.Adam(net.parameters(), lr=MUTATION_RATE)
#     epoch = 0
#
#     if os.path.isfile(FILE_PATH):
#         print ("Loading checkpoint from file '{}'" . format(FILE_PATH))
#         checkpoint = torch.load(FILE_PATH)
#         epoch = checkpoint['epoch']
#         net.load_state_dict(checkpoint['state_dict'])
#         optimizer.load_state_dict(checkpoint['optimizer'])
#     return net, optimizer, epoch
#
################################################################################

def global_values(flg):
    """
    Change global variables values depending on the flags given.
    """

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
    return None

def print_stats(flg, gen, min_fit, avg_fit, max_fit):
    """
    Prints the generation stats.
    """

    if gen == 0 and flg.getFlagLog() == True:
        print("Stats will be saved in a log file.")
        flg.createLogFile()
    print("Generation  : %5d" % (gen + 1))
    print("Min Fitness : %5.0f" % min_fit)
    print("Avg Fitness : %5.0f" % avg_fit)
    print("Max Fitness : %5.0f" % max_fit)
    print("-------------------\n")
    return None

def main(flg):
    """
    Main entry point of the program.
    """

    global_values(flg)
    gym_ai = OpenAIGym(GAME_NAME)
    gen = Generation()
    pop = Population(POPULATION_COUNT, MUTATION_RATE, gym_ai.getNodeCount())
    best_neural_nets = gen.getBestNeuralNets()

    # Loop for each generation
    for gen in range(MAX_GENERATIONS):
        avg_fit = 0.0
        min_fit =  1000000
        max_fit = -1000000
        max_neural_net = None
        # Loop for each species in the generation
        for nn in pop.population:
            total_reward = 0
            observation = gym_ai.getObservation()
            # Loop for every step taken by Marvin
            for step in range(MAX_STEPS):
                gym_ai.getRender()
                gym_ai.setAction(nn.getOutput(observation))
                observation, reward, done, info = gym_ai.getAction()
                total_reward += reward
                if done:
                    break
            nn.fitness = total_reward
            min_fit = min(min_fit, nn.fitness)
            avg_fit += nn.fitness
            if  nn.fitness > max_fit:
                max_fit = nn.fitness
                max_neural_net = copy.deepcopy(nn);
        best_neural_nets.append(max_neural_net)
        avg_fit /= pop.getPopulationCount()
        pop.createNewGeneration(max_neural_net)

        print_stats(flg, gen, min_fit, avg_fit, max_fit)

    # Records and replayes the best bots
    #recordBestBots(best_neural_nets, gym_ai.getEnv())
    #replayBestBots(bestNeuralNets, max(1, int(math.ceil(MAX_GENERATIONS / 10.0))), 0.0625)

if __name__ == "__main__":
    """
    This is executed when run from the command line.
    """

    flg = MarvinFlags(GAME_NAME, __version__)
    flg.initFlags()
    main(flg)
