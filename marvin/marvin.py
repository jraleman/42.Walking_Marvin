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




# Debugging functions, remove them before turning in the project!!!
def print_stats():
    print("Here is when the log is printed to the stdout")

def main(flg):
    """
    Main entry point of the program.
    """

    # OpenAIGym class and method declarations
    gym_ai = OpenAIGym(GAME_NAME)
    max_steps = 1000
    max_generations = 100
    population_count = 1000
    mutation_rate = 0.042
    node_count = gym_ai.getNodeCount()

    # Generation class declaration
    gen = Generation()
    total_reward = gen.getTotalReward()
    best_neural_nets = gen.getBestNeuralNets()

    # Population class declaration
    pop = Population(population_count, mutation_rate, node_count)

    # Loop for each generation
    for gen in range(max_generations):
        avg_fit = 0.0
        min_fit =  1000000
        max_fit = -1000000
        max_neural_net = None
        # Loop for each species in the generation
        for nn in pop.population:
            total_reward = 0
            observation = gym_ai.getObservation()
            # Loop for every step taken by Marvin
            for step in range(max_steps):
                #gym_ai.getRender()
                gym_ai.setAction(nn.getOutput(observation))
                observation, reward, done, info = gym_ai.getAction()
                total_reward += reward
                if done:
                    break
            nn.fitness = total_reward
            min_fit = min(min_fit, nn.fitness)
            avg_fit += nn.fitness
            if nn.fitness > max_fit:
                max_fit = nn.fitness
                max_neural_net = copy.deepcopy(nn);
        best_neural_nets.append(max_neural_net)
        avg_fit /= pop.getPopulationCount()

        print("Generation : %3d  |  Min : %5.0f  |  Avg : %5.0f  |  Max : %5.0f  " % (gen + 1, min_fit, avg_fit, max_fit))

        pop.createNewGeneration(max_neural_net)

    # Records and replayes the best bots
    #recordBestBots(best_neural_nets, env)
    #replayBestBots(bestNeuralNets, max(1, int(math.ceil(max_generations / 10.0))), 0.0625)

if __name__ == "__main__":
    """
    This is executed when run from the command line
    """

    flg = MarvinFlags(__version__)
    main(flg)
