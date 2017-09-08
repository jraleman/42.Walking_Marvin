#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    flags.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/31 02:24:22 by jaleman           #+#    #+#              #
#    Updated: 2017/08/31 02:24:23 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import argparse
import datetime

from lib.open_ai_gym import OpenAIGym

def parser():
    """
    ..........
    """
    # TODO:
    # if string is capitalize, lowercase it and then parse it.
    # If not, error (show argparse error or something)
    parser = argparse.ArgumentParser(
        description="Python project that uses OpenAI Gym with the environment \
            (provided) Marvin. The goal is to train Marvin to walk, \
            having the training and walking process.",
        epilog="Go ahead and run the visualizer! :D")

    parser.add_argument(
        '-w',
        '--walk',
        action='store_true',
        help='display only the walking process',
        required=False)

    parser.add_argument(
        '-v',
        '--video',
        action='store',
        help='saves videos of the walking proccess of the best species \
        from each generation',
        required=False)\

    parser.add_argument(
        '-l',
        '--load',
        action='store',
        dest='path',
        help='load weights for Marvin agent from a file \
        (skip training process if this option is specified)',
        required=False)

    parser.add_argument(
        '-s',
        '--save',
        action='store',
        dest='path',
        help='save weights to a file after running the program',
        required=False)

    parser.add_argument(
        '-n',
        '--name',
        action='store_true',
        help='the name of the game (enviroment)',
        required=False)

    parser.add_argument(
        '-g',
        '--generation',
        action='store_true',
        help='number of max generations to be ',
        required=False)

    parser.add_argument(
        '-p',
        '--population',
        action='store_true',
        help='count',
        required=False)

    parser.add_argument(
        '-r',
        '--rate',
        action='store_true',
        help='mutuation ',
        required=False)

    parser.add_argument(
        '-m',
        '--movement',
        action='store_true',
        help='number of steps (movement)',
        required=False)

    parser.add_argument(
        '--log',
        action='store_true',
        help='save info of the generations to a file',
        required=False)

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s ' + "0.1.0",
        help="show program's version number and exit")

    return vars(parser.parse_args())

class MarvinFlags(object):
    """
    ..........
    """
    def __init__(self, name, version):
        self.flags = parser()
        self.name = name
        self.version = version
        self.flag_walk = False
        self.flag_video = False
        self.flag_load = False
        self.flag_save = False
        self.flag_name = False
        self.flag_gen = 0
        self.flag_pop = 0
        self.flag_move = 0
        self.flag_rate = 0.0
        self.flag_log = False
        return None

    # Get methods
    def getFlagWalk(self):
        return self.flag_walk
    def getFlagVideo(self):
        return self.flag_video
    def getFlagLoad(self):
        return self.flag_load
    def getFlagSave(self):
        return self.flag_save
    def getFlagName(self):
        return self.flag_name
    def getFlagGen(self):
        return self.flag_gen
    def getFlagPop(self):
        return self.flag_pop
    def getFlagMove(self):
        return self.flag_move
    def getFlagRate(self):
        return self.flag_rate
    def getFlagLog(self):
        return self.flag_log

    # Set methods
    def setFlagWalk(self, val):
        self.flag_walk = val
        return None
    def setFlagVideo(self, val):
        self.flag_video = val
        return None
    def setFlagLoad(self, val):
        self.flag_load = val
        return None
    def setFlagSave(self, val):
        self.flag_save = val
        return None
    def setFlagName(self, val):
        self.flag_name = val
        return None
    def setFlagGen(self, val):
        self.flag_gen = val
        return None
    def setFlagPop(self, val):
        self.flag_pop = val
        return None
    def setFlagMove(self, val):
        self.flag_move = val
        return None
    def setFlagRate(self, val):
        self.flag_rate = val
        return None
    def setFlagLog(self, val):
        self.flag_log = val
        return None

    def createLogFile(self):
        log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file = self.name + "_" + log_time + ".log"
        sys.stdout = open(log_file, 'a+')
        print("===================")
        print(self.name)
        print(log_time)
        print("===================\n")

    def initFlags(self):
        if self.flags['log']:
            self.setFlagLog(True)




# def flagWalk(bestNeuralNets, steps, sleep):
#     print ("Load flag works!")
#     # choice = input("Do you want to watch the replay ?[Y/N] : ")
#     # if choice=='Y' or choice=='y':
#     for i in range(len(bestNeuralNets)):
#         #if bestNeuralNets[i] == None:
#             #return
#         if (i + 1) % steps == 0:
#             observation = env.reset()
#             totalReward = 0
#             for step in range(MAX_STEPS):
#                 env.render()
#                 time.sleep(sleep)
#                 action = bestNeuralNets[i].getOutput(observation)
#                 observation, reward, done, info = env.step(action)
#                 totalReward += reward
#                 if done:
#                     observation = env.reset()
#                     break
#             #print("Generation %3d | Expected Fitness of %4d | Actual Fitness = %4d" % (i+1, bestNeuralNets[i].fitness, totalReward))
#     return None
#
# def flagVideo(bestNeuralNets, path, env):
#     print ("Video flag works!")
#     print ("Path is : " + str(self.flags['path']))
#     env = wrappers.Monitor(env, path, force='True')
#     #print("\n Recording Best Bots ")
#     #print("---------------------")
#     env = gym.wrappers.Monitor(env, 'vids/'+GAME)
#     observation = env.reset()
#     for i in range(len(bestNeuralNets)):
#         #if bestNeuralNets[i] == None:
#             #return
#         totalReward = 0
#         for step in range(MAX_STEPS):
#             env.render()
#             action = bestNeuralNets[i].getOutput(observation)
#             observation, reward, done, info = env.step(action)
#             totalReward += reward
#             if done:
#                 observation = env.reset()
#                 break
#         #print("Generation %3d | Expected Fitness of %4d | Actual Fitness = %4d" % (i+1, bestNeuralNets[i].fitness, totalReward))
#     env.monitor.close()
#     return None
