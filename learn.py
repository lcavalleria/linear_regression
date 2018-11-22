thetas = [0,0]
with open("data.csv") as f:
    keys = f.readline().split(',')
    keys[1] = keys[1][:-1]
    for line in f:
        values = line.split(',')
        values[0] = int(values[0])
        values[1] = int(values[1][:-1])
        print("km: " + str(values[0]) + ", price: " + str(values[1]))
print(keys[0] + " - "+keys[1] + " |")