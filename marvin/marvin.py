#!/usr/bin/env python3
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

#import gym
import argparse
#from logzero import logger
#env = gym.make('Marvin-v0')

################################################################################
# Flags
################################################################################

class MarvinFlags(object):
    def __init__(self, flags):
        self.flags = flags

    def walk(self):
        print ("Walk flag works!")

    def load(self):
        print ("Load flag works!")
        print ("Path is : " + str(self.flags['path']))

    def save(self):
        print ("Save flag works!")
        print ("Path is : " + str(self.flags['path']))

    def run(self):
        if self.flags['walk']:
            self.walk()
        #elif self.flags['save']:
        #    self.save()
        #elif self.flags['load']:
        #    self.load()
        #else:
        #    print ("No arguments given")

################################################################################

def parse_flags():
    parser = argparse.ArgumentParser(
        description='Description of your program',
        epilog="That's all she wrote")

    parser.add_argument(
        '-v',
        '--walk',
        action='store_true',
        help='display only the walking process',
        required=False)

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
        version='%(prog)s ' + str(__version__),
        help="show program's version number and exit")

    return parser

################################################################################

def main(args):
    """ Main entry point of the project """
    #logger.info("hello world")
    #logger.info(args)

if __name__ == "__main__":
    """ This is executed when run from the command line """

    parser = parse_flags()
    #print(parser)
    #print(parser.parse_args())
    args = vars(parser.parse_args())

    #print(args)

    MarvinFlags(args).run()
    main(args)
