#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# 42 HEADER GOES HERE

from __future__ import print_function
import numpy as np

################################################################################
# Neural Network
################################################################################

class NeuralNet :
    def __init__(self, nodeCount):
        self.fitness = 0.0
        self.nodeCount = nodeCount
        self.weights = []
        self.biases = []
        for i in range(len(nodeCount) - 1):
            self.weights.append( np.random.uniform(low=-1, high=1, size=(nodeCount[i], nodeCount[i+1])).tolist() )
            self.biases.append( np.random.uniform(low=-1, high=1, size=(nodeCount[i+1])).tolist())

    def getOutput(self, input):
        output = input
        for i in range(len(self.nodeCount)-1):
            output = np.reshape( np.dot(output, self.weights[i]) + self.biases[i], (self.nodeCount[i+1]))
        return output


    def printWeightsandBiases(self):
        print("--------------------------------")
        print("Weights :\n[", end="")
        for i in range(len(self.weights)):
            print("\n [ ", end="")
            for j in range(len(self.weights[i])):
                if j!=0:
                    print("\n   ", end="")
                print("[", end="")
                for k in range(len(self.weights[i][j])):
                    print(" %5.2f," % (self.weights[i][j][k]), end="")
                print("\b],", end="")
            print("\b ],")
        print("\n]")

        print("\nBiases :\n[", end="")
        for i in range(len(self.biases)):
            print("\n [ ", end="")
            for j in range(len(self.biases[i])):
                    print(" %5.2f," % (self.biases[i][j]), end="")
            print("\b],", end="")
        print("\b \n]\n--------------------------------\n")

    def sigmoid(x):
        """
        Type of activation function for artifical neurons.
        """
        return 1.0/(1.0 + np.exp(-x))
