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
GAME = 'Marvin-v0'
MAX_STEPS = 1000
MAX_GENERATIONS = 100
POPULATION_COUNT = 42
MUTATION_RATE = 0.042

def print_stats():
    print("Here is when the log is printed to the stdout")

def main(flg):
    """
    Main entry point of the program.
    """

    print_stats()

    # gym_ai = OpenAIGym(GAME)
    # gen = Generation()
    # pop = Population(POPULATION_COUNT, MUTATION_RATE, gym_ai.getNodeCount)

    # env = gym.make(GAME)
    # #env = env.Marvin
    # #env.reset()
    # #env = TraceRecordingWrapper(env)

    # #env = wrappers.Monitor(env, './videos', force='True')
    #
    #
    # # Enviroment principal, valores random al inicio
    # observation = env.reset()
    #
    #
    # #
    # in_dimen = env.observation_space.shape[0]
    # out_dimen = env.action_space.shape[0]
    #
    # #khe_berga(in_dimen)
    #
    # #
    # obsMin = env.observation_space.low
    # obsMax = env.observation_space.high
    #
    #
    # actionMin = env.action_space.low
    # actionMax = env.action_space.high
    #
    #
    # pop = Population(POPULATION_COUNT, MUTATION_RATE, [in_dimen, 13, 8, 13, out_dimen])
    # bestNeuralNets = []
    #
    # #env.render()
    #
    #
    #

    #pop = Population(POPULATION_COUNT, MUTATION_RATE, node_count)




    # # Generations ->
    # for gen in range(MAX_GENERATIONS):



################################################################################
# flg.runFlags here maybe
################################################################################
        # if flags != None:
            #flg.runFlags()



    #     genAvgFit = 0.0
    #     minFit =  1000000
    #     maxFit = -1000000
    #     maxNeuralNet = None
    #
    #
    #     # Species ->
    #     for nn in pop.population:
    #         observation = env.reset()
    #         totalReward = 0
    #
    #         # Steps ->
    #         for step in range(MAX_STEPS):
    #             env.render()
    #             action = nn.getOutput(observation)
    #             observation, reward, done, info = env.step(action)
    #
    #             totalReward += reward
    #             if done:
    #
    #                 #exit()
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
    #     #env.render()
        #if done: break

################################################################################
# flg.runFlags here maybe
################################################################################
    #flags.recordBestBots(bestNeuralNets, env)
    #flags.replayBestBots(bestNeuralNets, max(1, int(math.ceil(MAX_GENERATIONS/10.0))), 0.0625)

if __name__ == "__main__":
    """
    This is executed when run from the command line
    """

    flg = MarvinFlags(__version__)
    main(flg)
