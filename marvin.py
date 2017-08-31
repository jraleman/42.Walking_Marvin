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
import os
import logging
import logging.handlers

# Marvin modules
from marvin import flags


#import gym
#env = gym.make('Marvin-v0')

################################################################################
################################################################################
# Log
################################################################################


# handler = logging.handlers.WatchedFileHandler(
# os.environ.get("LOGFILE", "lol.log"))
# formatter = logging.Formatter(logging.BASIC_FORMAT)
# handler.setFormatter(formatter)
# root = logging.getLogger()
# root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
# root.addHandler(handler)


# try:
#     exit(main())
# except Exception:
#     logging.exception("Exception in main()")
#     exit(1)

################################################################################
################################################################################
# Main
################################################################################

def main():
    """ Main entry point of the project """

    # log = logging.getLogger("my-logger")
    # log.info("Hello, world")

if __name__ == "__main__":
    """ This is executed when run from the command line """

    parser = flags.parse()
    flags.MarvinFlags(parser, __version__).run()

    main()
