import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def predict(X, weights, lambdaa = 1):
  net = np.dot(X, weights)
  return (1 / (1 + np.exp(-lambdaa * net)))

def calculate_dw(X, y, y_pred):
  return ((y_pred - y) * (y_pred) * (1 - y_pred) * X)

def calculate_error(y, y_pred):
  return np.square(y_pred - y)

def train_vanilla(X, y, weights, epochs = 500, lr = 0.001, gamma = 0.9):
    upd = 0

    for i in range(epochs):
        dw = 0
        error = 0

    for (Xi, yi) in zip(X, y):
        y_pred = predict(Xi, weights)
        dw += calculate_dw(Xi, yi, y_pred)
        error += calculate_error(y, y_pred)

    upd = (lr * dw) + (gamma * upd)
    weights -= upd
    error /= (2 * len(X))

    if((i + 1) % 100 == 1):
        print(f"Weights after {i} epochs: {weights} \n")
        print(f"Error after {i} epochs: {error} \n")

def train_stochastic(X, y, weights, epochs = 500, lr = 0.001, gamma = 0.9):
    upd = 0

    for i in range(epochs):
        dw = 0
        error = 0

        for (Xi, yi) in zip(X, y):
            y_pred = predict(Xi, weights)
            dw += calculate_dw(Xi, yi, y_pred)
            error += calculate_error(y, y_pred)
            upd = (lr * dw) + (gamma * upd)
            weights -= upd

        error /= (2 * len(X))
        
    if((i + 1) % 100 == 1):
        print(f"Weights after {i} epochs: {weights} \n")
        print(f"Error after {i} epochs: {error} \n")
      
def train_minibatch(X, y, weights, epochs = 500, lr = 0.001, gamma = 0.9, bs = 32):
    upd = 0

    for i in range(epochs):
        dw = 0
        error = 0

        for (Xi, yi) in zip(X, y):
            y_pred = predict(Xi, weights)
            dw += calculate_dw(Xi, yi, y_pred)
            error += calculate_error(y, y_pred)

            if i % bs == 0 or i == len(X):
                upd = (lr * dw) + (gamma * upd)
                weights -= upd
                dw = 0

        error /= (2 * len(X))
        
    if((i + 1) % 100 == 1):
        print(f"Weights after {i} epochs: {weights} \n")
        print(f"Error after {i} epochs: {error} \n")

df = pd.read_csv('./bank_note.csv')

df.insert(4, 'x0', 1)

X = df[['variance', 'skewness', 'curtosis', 'entropy', 'x0']].values
y = df['class'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=13, test = 0.2)

weights = input("Enter 4 weights and 1 bias: ").split()
weights = [float(weight) for weight in weights]

weights = np.array(weights)

train_vanilla(X, y, weights.copy())
