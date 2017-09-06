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

def print_stats():
    print("Here is when the log is printed to the stdout")

def main(flg):
    """
    Main entry point of the program.
    """

    # Just to see if anything gives me an error as of now.
    print_stats()

################################################################################
# Objects and class declarations
################################################################################

    # OpenAIGym class and method declarations
    # gym_ai = OpenAIGym(GAME_NAME)
    # max_steps = gym_ai.getMaxSteps()
    # max_generations = gym_ai.getMaxGenerations()
    # node_count = gym_ai.getNodeCount()
    # population_count = gym_ai.getPopulationCount()
    # mutation_rate = gym_ai.getMutationRate()
    # debug_object(gym_ai)

    # Generation class declaration
    # gen = Generation()
    # avg_fit = gen.getAvgFit()
    # min_fit = gen.getMinFit()
    # max_fix = gen.getMaxFit()
    # max_neural_net = gen.getMaxNeuralNet()
    # total_reward = gen.getTotalReward()

    # debug_object(gen)

    # Population class declaration
    # pop = Population(population_count, mutation_rate, node_count)
    # debug_object(pop)

################################################################################

    # for gen in range(max_generations):

        #
        # Maybe run the flag method here????
        #

    #
    #     # Species ->
    #     for nn in pop.population:



    #         observation = env.reset()
    #         totalReward = 0


    #
    #         # Steps ->
    #         for step in range(max_steps):



    #             action = nn.getOutput(observation)



    #             observation, reward, done, info = env.step(action)



    #



    #             totalReward += reward




    #             if done:
    #                 break
    #
    #         nn.fitness = totalReward


    #         minFit = min(minFit, nn.fitness)
    #         genAvgFit += nn.fitness


    #         if nn.fitness > maxFit :


    #             maxFit = nn.fitness
    #             maxNeuralNet = copy.deepcopy(nn);
    #






    #     bestNeuralNets.append(maxNeuralNet)
    #     genAvgFit/=pop.popCount
    #     print("Generation : %3d  |  Min : %5.0f  |  Avg : %5.0f  |  Max : %5.0f  " % (gen+1, minFit, genAvgFit, maxFit) )
    #     pop.createNewGeneration(maxNeuralNet)


################################################################################
# flg.runFlags here maybe
################################################################################
    #flags.recordBestBots(bestNeuralNets, env)
    #flags.replayBestBots(bestNeuralNets, max(1, int(math.ceil(max_generations/10.0))), 0.0625)

if __name__ == "__main__":
    """
    This is executed when run from the command line
    """

    flg = MarvinFlags(__version__)
    main(flg)
