import estimate
with open("thetas.txt") as f:
    theta0 = float(f.readline())
    theta1 = float(f.readline())
print("Enter a mileage")
mileage = int(input())
thetas = [theta0, theta1]
print(str(estimate.estimateLine(thetas, mileage)))