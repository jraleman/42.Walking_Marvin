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

<description goes here>
"""

# Project's Metadata
__author__ = "jraleman, corezip"
__version__ = "0.1.0"
__license__ = "MIT"

# Gym AI dependencies
import gym
from lib.enviroment import Marvin
#from lib.open_ai_gym import OpenAIGym

# NeuralNetwork dependencies
from lib.neural_net import NeuralNet
from lib.population import Population
#from lib.generation import Generation

# Modules to parse flags, save logs, and aux functions.
from lib.flags import MarvinFlags, parser
from lib.logs import MarvinLogs
from lib.utilities import map_range, normalize_array, scale_array, debug_object

# Global variables.
GAME = 'Marvin-v0'
MAX_STEPS = 1000
MAX_GENERATIONS = 100
POPULATION_COUNT = 42
MUTATION_RATE = 0.042

def main(flg, log):
    """
    Main entry point of the program.
    """

    print("lol")

    # insert gymai class HERE
    #    x = GymAI(name)
    # insert generation class here
    #    gen = Generation()
    # insert population class here
    #    pop = Population(POPULATION_COUNT, MUTATION_RATE, node_count)






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

    #flags.recordBestBots(bestNeuralNets, env)

    #flags.replayBestBots(bestNeuralNets, max(1, int(math.ceil(MAX_GENERATIONS/10.0))), 0.0625)

if __name__ == "__main__":
    """
    This is executed when run from the command line
    """

    # Remove this soon
    env = 0


    # Make it so MarvinFlags and MarvinLogs just accept one argument: __version__
    flg = MarvinFlags(env, parser(), __version__)
    log = 0
    #log = MarvinLogs(__version__)

    main(flg, log)
