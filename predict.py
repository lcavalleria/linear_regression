import estimate
with open("thetas.txt") as f:
    theta0 = float(f.readline())
    theta1 = float(f.readline())
print("Enter a mileage")
mileage = int(input())
print(str(estimate.estimateLine(theta0, theta1, mileage)))