import estimate
learningRate = 0.1
with open("data.csv") as f:
    f.readline()
    data = [[]]
    for line in f:
        values = line.split(',')
        data.append([int(values[0]), int(values[1][:-1])])
i = 1
thetas = [0, 0]
while estimate.accuracy(thetas, data) < 0.95 and i < 1000:
    iterdata = iter(data)
    next(iterdata)
    thetasum0 = 0
    thetasum1 = 0
    for values in iterdata:
        thetasum0 += estimate.estimateLine(thetas[0], thetas[1], values[0]) - values[1]
        thetasum1 += estimate.estimateLine(thetas[0], thetas[1], values[0]) - values[1] * values[0]
    thetas[0] = thetasum0 / (len(data) - 1) * learningRate
    thetas[1] = thetasum1 / (len(data) - 1) * learningRate
    i += 1