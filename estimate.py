def estimateLine(theta0, theta1, mileage):
    ret = theta0 + mileage * theta1
    return ret

def accuracy(thetas, data):
    iterdata = iter(data)
    next(iterdata)
    accuracy = 0.0
    for values in iterdata:
        estimatedPrice = estimateLine(thetas[0], thetas[1], values[0])
        tmp = abs(estimatedPrice - values[1])
        accuracy += tmp
    accuracy = accuracy / (len(data) -1) / 2
    return accuracy