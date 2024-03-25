import math

# Get lambda and alpha
lambda_, alpha = map(float, input().split())
# Get the number of days(n), the number of itetrations(t), and the number of queries(m)
n, t, m = map(int, input().split())
# Get the cloud cover for each day
x = list(map(float, input().split()))
# Get the rainfall(binary) for each day
y = list(map(int, input().split()))
# Get the queries
q = list(map(float, input().split()))

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Define the hypothesis function: h(x) = sigmoid(theta0 + theta1 * x)
def hypothesis(theta0, theta1, x):
    return sigmoid(theta0 + theta1 * x)

# Define the derivative of cost function: dJ/dtheta = sum((h(x) - y) * x) + lambda * theta
def derivative(theta0, theta1, x, y, lambda_):
    dtheta0 = sum([hypothesis(theta0, theta1, x[i]) - y[i] for i in range(n)]) + lambda_ * theta0
    dtheta1 = sum([(hypothesis(theta0, theta1, x[i]) - y[i]) * x[i] for i in range(n)]) + lambda_ * theta1
    return dtheta0, dtheta1

# Fit parameters using gradient descent
theta0, theta1 = 0, 0
for _ in range(t):
    dtheta0, dtheta1 = derivative(theta0, theta1, x, y, lambda_)
    theta0 -= alpha * dtheta0
    theta1 -= alpha * dtheta1
# print(theta0, theta1)
# Predict the rainfall for each query
for i in range(m):
    # print(1 if 0.5 < hypothesis(theta0, theta1, q[i]) else 0, end=' ')
    print(f"{hypothesis(theta0, theta1, q[i]):.2f}", end=' ')
print()