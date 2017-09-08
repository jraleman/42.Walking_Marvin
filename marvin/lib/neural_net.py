#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    neural_net.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 01:36:21 by jaleman           #+#    #+#              #
#    Updated: 2017/09/05 01:36:21 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from __future__ import print_function
import numpy as np

class NeuralNet(object):
    """
    Class ...
    """
    def __init__(self, nodeCount):
        self.biases = []
        self.weights = []
        self.fitness = 0.0
        self.nodeCount = nodeCount
        for i in range(len(nodeCount) - 1):
            self.weights.append(np.random.uniform(low = -1, high = 1, \
                size = (nodeCount[i], nodeCount[i + 1])).tolist())
            self.biases.append(np.random.uniform(low = -1, high = 1, \
                size = (nodeCount[i + 1])).tolist())
        return None

    def sigmoid(x):
        """
        Type of activation function for artifical neurons.
        """

        return 1.0/(1.0 + np.exp(-x))

    def getOutput(self, input):
        """
        .........
        """
        output = input
        for i in range(len(self.nodeCount)-1):
            output = np.reshape(np.dot(output, self.weights[i]) \
                + self.biases[i], (self.nodeCount[i + 1]))
        return output

    def printWeights(self):
        """
        .........
        """

        print("Weights :\n[")
        for i in range(len(self.weights)):
            print("\n [ ")
            for j in range(len(self.weights[i])):
                if j != 0:
                    print("\n   ")
                print("[")
                for k in range(len(self.weights[i][j])):
                    print(" %5.2f," % (self.weights[i][j][k]))
                print("\b],")
            print("\b ],")
        print("\n]")
        return None

    def printBiases(self):
        """
        .........
        """

        print("\nBiases :\n[")
        for i in range(len(self.biases)):
            print("\n [ ")
            for j in range(len(self.biases[i])):
                print(" %5.2f," % (self.biases[i][j]))
            print("\b],")
        print("\b \n]")
        return None
