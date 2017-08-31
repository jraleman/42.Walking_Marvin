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

# OpenAI Gym enviroment config
#env = gym.make('Marvin-v0')

# Marvin modules
from marvin import flags
#from marvin import logs

def main():
    """ Main entry point of the project """

    # log = logging.getLogger("my-logger")
    # log.info("Hello, world")

if __name__ == "__main__":
    """ This is executed when run from the command line """

    flg = flags.MarvinArguments(flags.parser(), __version__)
    flg.runFlags()

    main()
