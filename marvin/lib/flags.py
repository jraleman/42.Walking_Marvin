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
        '--generations',
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
    def __init__(self, game_name, version):
        self.game_name = game_name
        self.flags = parser()
        self.version = version

        self.flag_log = False

        return None


    def getFlagLog(self):
        return self.flag_log

    def setFlagLog(self, val):
        self.flag_log = val
        return None

    def createLogFile(self):
        log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file = self.game_name + "_" + log_time + ".log"
        sys.stdout = open(log_file, 'a+')
        print("===================")
        print(self.game_name)
        print(log_time)
        print("===================\n")

    def initFlags(self):
        if self.flags['log']:
            self.setFlagLog(True)
