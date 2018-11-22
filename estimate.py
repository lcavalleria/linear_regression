def estimateLine(theta0, theta1, mileage):
    return theta0 + mileage * theta1

def accuracy(thetas, data):
    iterdata = iter(data)
    next(iterdata)
    accuracy = 0.0
    for values in iterdata:
        estimatedPrice = estimateLine(thetas[0], thetas[1], values[0])
        #mirar com pillar el % de precisio. busca al google. linear regression accuracy o algo
    print(accuracy)
    accuracy /= len(data) -1
    print(accuracy)
    return accuracy