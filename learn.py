import estimate
import copy
import readData as rd
import matplotlib.pyplot as pylab

learningRate = 1
thetas = [0, 0]

data, avgkm, minkm, maxkm = rd.readData()

############### scale data ###############
m = len(data)
avgkm = avgkm / m
for values in data:
    values[0] = (values[0] - minkm) / (maxkm - minkm)

############### gradient descent ###############
costdelta = 1
cost = float("inf")
cost_f = []
i = 0
while abs(costdelta) > 0.001 and i < 500:
    thetasum0 = 0
    thetasum1 = 0
    for values in data:
        estimatedPrice = estimate.estimateLine(thetas, values[0])
        thetasum0 += estimatedPrice - values[1]
        thetasum1 += (estimatedPrice - values[1]) * values[0]
    thetas[0] = thetas[0] - learningRate * thetasum0 / m
    thetas[1] = thetas[1] - learningRate  * thetasum1 / m
    oldcost = cost
    cost = estimate.cost(thetas, data)
    cost_f.append(cost)
    costdelta = oldcost - cost
    i += 1

############### save thetas file ###############
print("theta0: " + str(thetas[0]) + ", theta1: " + str(thetas[1]) + ", squared error: " + str(cost))
f = open("thetas.txt","w")
f.write(str(thetas[0]) + "\n")
f.write(str(thetas[1]))

############### plot ###############
pylab.plot(range(len(cost_f)), cost_f)
pylab.show()