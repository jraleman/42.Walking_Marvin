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
"""

__author__ = "Jose Ramon Aleman, Gerardo Solis"
__version__ = "0.1.0"
__license__ = "MIT"

# Python modules
import gym
import time
from marvin_modules import env, specs, flags, logs, utils

# Global variables
GAME = 'Marvin-v0'
MAX_STEPS = 1000
MAX_GENERATIONS = 30
POPULATION_COUNT = 1000
MUTATION_RATE = 0.042


def main():
    """ Main entry point of the project """

    # log = logging.getLogger("my-logger")
    # log.info("Hello, world")
    env = gym.make(GAME)
    #env = env.Marvin
    #env.reset()
    #env = TraceRecordingWrapper(env)
    #env = wrappers.Monitor(env, './videos', force='True')


    # Enviroment principal, valores random al inicio
    observation = env.reset()


    #
    in_dimen = env.observation_space.shape[0]
    out_dimen = env.action_space.shape[0]

    #khe_berga(in_dimen)

    #
    obsMin = env.observation_space.low
    obsMax = env.observation_space.high


    actionMin = env.action_space.low
    actionMax = env.action_space.high


    pop = specs.Population(POPULATION_COUNT, MUTATION_RATE, [in_dimen, 13, 8, 13, out_dimen])
    bestNeuralNets = []

    print("\nObservation\n--------------------------------")
    print("Shape :", in_dimen, " \n High :", obsMax, " \n Low :", obsMin)
    print("\nAction\n--------------------------------")
    print("Shape :", out_dimen, " | High :", actionMax, " | Low :", actionMin,"\n")
    #env.render()



    # Generations ->
    for gen in range(MAX_GENERATIONS):
        genAvgFit = 0.0
        minFit =  1000000
        maxFit = -1000000
        maxNeuralNet = None


        # Species ->
        for nn in pop.population:
            observation = env.reset()
            totalReward = 0

            # Steps ->
            for step in range(MAX_STEPS):
                env.render()
                action = nn.getOutput(observation)
                observation, reward, done, info = env.step(action)


                # print ("\nObservation : ")
                # print (observation)
                # #time.sleep(0.005)
                # print ("\nReward      : ")
                # print (reward)
                # #time.sleep(0.005)
                # print ("\nDone        : ")
                # print (done)
                # #time.sleep(0.005)
                # print ("\nInfo        : ")
                # print (info)
                # #time.sleep(0.005)

                #print("\nObservation\n--------------------------------")
                #print("Generation : %3d  |  Min : %5.00f  |  Avg : %5.00f  |  Max : %5.00f  " % (gen+1, minFit, genAvgFit, maxFit) )


                totalReward += reward
                if done:

                    #exit()
                    break

            nn.fitness = totalReward
            minFit = min(minFit, nn.fitness)
            genAvgFit += nn.fitness
            if nn.fitness > maxFit :
                maxFit = nn.fitness
                maxNeuralNet = copy.deepcopy(nn);

        bestNeuralNets.append(maxNeuralNet)
        genAvgFit/=pop.popCount
        print("Generation : %3d  |  Min : %5.0f  |  Avg : %5.0f  |  Max : %5.0f  " % (gen+1, minFit, genAvgFit, maxFit) )
        pop.createNewGeneration(maxNeuralNet)
        #env.render()
        #if done: break

    #flags.recordBestBots(bestNeuralNets, env)

    #uploadSimulation()

    #flags.replayBestBots(bestNeuralNets, max(1, int(math.ceil(MAX_GENERATIONS/10.0))), 0.0625)




if __name__ == "__main__":
    """ This is executed when run from the command line """

    flg = flags.MarvinArguments(flags.parser(), __version__)
    #flg.runFlags()

    main()
