############### read data ###############
def readData():
    avgkm = 0
    maxkm = 0
    minkm = float("inf")
    with open("data.csv") as f:
        f.readline()
        data = [[]]
        for line in f:
            values = line.split(',')
            km = float(values[0])
            price = int(values[1][:-1])
            data.append([km, price])
            avgkm += km
            if km > maxkm:
                maxkm = km
            if km < minkm:
                minkm = km
        data.pop(0)
    return data, avgkm, minkm, maxkm