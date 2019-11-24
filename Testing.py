from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import pprint
def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
pprint.PrettyPrinter(indent=4).pprint(penData[1])
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)



acurracyListPen = []
for i in range(0,5):
	nnet, accuracy = testPenData()
	accuracyListPen.append(accuracy)

accuracyListCar = []
for j in range(0, 5):
	nnet, accuracy = testCarData()
	accuracyListCar.append(accuracy)

print "-------------Pen--------------"
print "Max: %.5f | Average: %.5f | StDev: %.5f" % (max(accuracyListPen), average(accuracyListPen), stDeviation(accuracyListPen))
print "-------------Car--------------"
print "Max: %.5f | Average: %.5f | StDev: %.5f" % (max(accuracyListCar), average(accuracyListCar), stDeviation(accuracyListCar))



print "=============VARYING THE NUMBER OF HIDDEN LAYERS============="
penData = [[0 for x in range(9)] for y in range(3)]
carData = [[0 for x in range(9)] for y in range(3)]
for i in range(0, 9):
	print "*Number of hidden layers: %d*" % (i * 5)
	
	for j in range(0,5):
		nnet, accuracy = testPenData(hiddenLayers=[i*5])
		accuracyListPen.append(accuracy)

	# Pen Data: [[max, avg, stDev]]
	penData[0][i] = max(accuracyListPen)
	penData[1][i] = average(accuracyListPen)
	penData[2][i] = stDeviation(accuracyListPen)

	accuracyListCar = []
	for k in range(0, 5):
		nnet, accuracy = testCarData(hiddenLayers=[i*5])
		accuracyListCar.append(accuracy)
	
	# Car Data: [[max, avg, stDev]]
	carData[0][i] = max(accuracyListCar)
	carData[1][i] = average(accuracyListCar)
	carData[2][i] = stDeviation(accuracyListCar)
print "=============TEST RESULTS============="
for i in range(0, 9):
	print "Test #%d: %d hidden layers" % (i, i*5)
	for j in range(0,3):
		if j == 0:
			print "Max:   Pen = %.6f, Car = %.6f" % (penData[i][j], carData[i][j])
		elif j == 1:
			print "Mean:  Pen = %.6f, Car = %.6f" % (penData[i][j], carData[i][j])
		else:
			print "StDev: Pen = %.6f, Car = %.6f" %(penData[i][j], carData[i][j])

