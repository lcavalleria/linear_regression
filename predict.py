import estimate
import readData as rd

with open("thetas.txt") as f:
    theta0 = float(f.readline())
    theta1 = float(f.readline())
data, _, minkm, maxkm = rd.readData()
print("Enter a mileage")
mileage = int(input())
mileage = (mileage - minkm) / (maxkm - minkm)
thetas = [theta0, theta1]
print(str(estimate.estimateLine(thetas, mileage)))