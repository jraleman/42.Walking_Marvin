#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logs.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/31 16:28:23 by jaleman           #+#    #+#              #
#    Updated: 2017/08/31 16:28:24 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Python modules
import os
import logging

class MarvinLogs(object):
    def __init__(self):
        return None

def create_log():
    """
    ...
    """

    handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "lol.log"))
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    logging.handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    root.addHandler(handler)

    try:
        exit(main())
    except Exception:
        logging.exception("Exception in main()")
        exit(1)
