import estimate
learningRate = 0.0001
with open("data.csv") as f:
    f.readline()
    data = [[]]
    for line in f:
        values = line.split(',')
        data.append([int(values[0]), int(values[1][:-1])])
thetas = [0.1, 5.0]
accuracy = 1
m = len(data) - 1
while accuracy > 0.05:
    iterdata = iter(data)
    next(iterdata)
    thetasum0 = 0
    thetasum1 = 0
    for values in iterdata:
        estimated = estimate.estimateLine(thetas[0], thetas[1], values[0])
        thetasum0 = thetasum0 + estimated - values[1]
        thetasum1 = thetasum1 + estimated - values[1] * values[0]
    oldthetas = [0,0]
    oldthetas[0] = thetas[0]
    oldthetas[1] = thetas[1]
    thetas[0] = learningRate * thetasum0 / m
    thetas[1] = learningRate * thetasum1 / m
    accuracy = estimate.accuracy(thetas, data)
print(estimate.accuracy(thetas, data))
