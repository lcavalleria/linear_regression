import estimate

learningRate = 0.00000000000001
thetas = [0, 0]
# avgkm = 0
# minkm = float("inf")
# maxkm = float(0)
with open("data.csv") as f:
    f.readline()
    data = [[]]
    for line in f:
        values = line.split(',')
        km = float(values[0])
        data.append([km, int(values[1][:-1])])
        # avgkm += km
        # if km > maxkm:
        #     maxkm = km
        # if km < minkm:
        #     minkm = km
data.pop(0)
m = len(data)
# avgkm = avgkm / m
# for values in data:
#     values[0] = (values[0] - avgkm) / (maxkm - minkm)
error = 1
dataplot = list(map(list, zip(*data)))
errordelta = 1
cost_f = []
i = 0
while abs(errordelta) > 0.00005 and i < 50000:
    thetasum0 = 0
    thetasum1 = 0
    for values in data:
        mileage = values[0]
        price = values[1]
        estimatedPrice = estimate.estimateLine(thetas, mileage)
        thetasum0 += estimatedPrice - price
        thetasum1 += (estimatedPrice - price) * mileage
    thetas[0] = thetas[0] - learningRate * thetasum0 / m
    thetas[1] = thetas[1] - learningRate  * thetasum1 / m
    olderror = error
    error = estimate.cost(thetas, data)
    cost_f.append(error)
    errordelta = olderror - error
    i += 1
print("theta0: " + str(thetas[0]) + ", theta1: " + str(thetas[1]) + ", squared error: " + str(error))
f = open("thetas.txt","w")
f.write(str(thetas[0]) + "\n")
f.write(str(thetas[1]))
import matplotlib.pyplot as pylab
pylab.scatter(dataplot[0], dataplot[1])
pylab.show()
pylab.plot(range(len(cost_f)), cost_f)
pylab.show()