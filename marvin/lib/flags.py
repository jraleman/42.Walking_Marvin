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

# Python modules
import os
import logging
import argparse

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
        '--version',
        action='version',
        version='%(prog)s ' + "0.1.0",
        help="show program's version number and exit")

    return vars(parser.parse_args())

class MarvinFlags(object):
    """
    ..........
    """
    def __init__(self, version):
        #self.flags = flags
        self.flags = parser()
        self.version = version
        return None

    def runFlags(self):
        if self.flags['walk']:
            self.flagWalk()
        #elif self.flags['video']:
        #    self.flagVideo()
        #elif self.flags['save']:
        #    self.save()
        #elif self.flags['load']:
        #    self.load()
        #else:
        #    print ("No arguments given")

    #
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

    def flagLoad(self):
        print ("Load flag works!")
        print ("Path is : " + str(self.flags['path']))

    def flagSave(self):
        print ("Save flag works!")
        print ("Path is : " + str(self.flags['path']))

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

    def flagLog(self, path):
        """
        ...
        """

        handler = logging.handlers.WatchedFileHandler(
        os.environ.get("LOGFILE", path))
        formatter = logging.Formatter(logging.BASIC_FORMAT)
        logging.handler.setFormatter(formatter)
        root = logging.getLogger()
        root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
        root.addHandler(handler)
        # Check how to save a array of strings (maybe a dictionary, like json)
        # to a file, given with the argument path.
