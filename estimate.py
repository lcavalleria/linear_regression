def estimateLine(thetas, mileage):
    ret = thetas[0] + mileage * thetas[1]
    return ret

def cost(thetas, data):
    cost = 0.0
    for values in data:
        estimatedPrice = estimateLine(thetas, values[0])
        tmp = (estimatedPrice - values[1]) ** 2
        cost += tmp
    cost = cost / len(data) / 2
    return cost