from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import pprint
import random

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

truthTable = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]

examples = ([], [])
for i in range(0, 10000):
	examples[0].append(random.choice(truthTable))
	if i % 4 == 0:
		examples[1].append(random.choice(truthTable))

accuracies = []
for i in range(0,4):
	accuracy = buildNeuralNet(examples,maxItr = 200, hiddenLayerList = [i])[1]
	accuracies.append(accuracy)
print(accuracies)
for i in range(0, 4):
	print "Hidden Layer Size: %d, Accuracy: %.6f" % (i, (accuracies[i] * 100))
"""
	The results from the accuracy readings are what I would expect for this network. 
	The function is fairly simple insofar it only deals with two variable's relations to each other to produce an output, so
	while having no hidden layers greatly harms accuracy, only a few layers are required to obtain a network with 100% accuracy.
"""