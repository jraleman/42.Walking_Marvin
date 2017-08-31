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

import argparse

################################################################################
# Flags
################################################################################

class MarvinFlags(object):
    def __init__(self, flags, version):
        self.flags = flags
        self.version = version
        return None

    def flagWalk(self):
        print ("Walk flag works!")

    def flagLoad(self):
        print ("Load flag works!")
        print ("Path is : " + str(self.flags['path']))

    def flagSave(self):
        print ("Save flag works!")
        print ("Path is : " + str(self.flags['path']))

    def run(self):
        if self.flags['walk']:
            self.flagWalk()
        #elif self.flags['save']:
        #    self.save()
        #elif self.flags['load']:
        #    self.load()
        #else:
        #    print ("No arguments given")

def parse():
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
        version='%(prog)s ' + "0.1.0",
        help="show program's version number and exit")

    return vars(parser.parse_args())
