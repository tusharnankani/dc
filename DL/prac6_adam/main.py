import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def predict(X,weights,lambdaa = 1):
    net = np.dot(X,weights)
    return (1/(1 + np.exp(-lambdaa*net)))

def calculate_dw(X,y,y_pred):
    return ((y_pred - y)*(y_pred)*(1-y_pred)*X)

def calculate_error(yi,y_pred):
    return np.square(y_pred-yi)

def train_vanilla(X, y, weights, epochs=500, lr =0.01, epsilon = 1e-8, beta1 = 0.9, beta2 = 0.999):
    mom = 0
    vel = 0
    for epoch in range(epochs):
        dw = 0
        error = 0

        for Xi,yi in zip(X,y):
            y_pred = predict(Xi,weights)
            dw += calculate_dw(Xi,yi,y_pred)
            error += calculate_error(yi,y_pred)

        mom = (beta1 * mom) + ((1 - beta1) * dw)
        vel = (beta2 * vel) + ((1 - beta2) * (dw ** 2))
        step = epoch + 1
        momcap = mom / (1 - (beta1 ** step))
        velcap = vel / (1 - (beta2 ** step))
        weights -= ((lr*momcap)/(np.sqrt(velcap+epsilon)))
        error /= (2*len(X))

        if (epoch+1)%50 == 0:
            print(f'Weights after epoch {epoch+1} : ',weights)
            print(f'Error after epoch {epoch+1} : ',error)


def train_stochastic(X, y, weights, epochs=500, lr =0.01, epsilon = 1e-8, beta1 = 0.9, beta2 = 0.999):
    vel = 0
    mom = 0
    step = 0
    for epoch in range(epochs):
        error = 0
        for Xi,yi in zip(X,y):
            y_pred = predict(Xi,weights)
            dw = calculate_dw(Xi,yi,y_pred)
            error += calculate_error(yi,y_pred)
            mom = (beta1 * mom) + ((1 - beta1) * dw)
            vel = (beta2 * vel) + ((1 - beta2) * (dw ** 2))
            step += 1
            momcap = mom / (1 - (beta1 ** step))
            velcap = vel / (1 - (beta2 ** step))
            weights -= ((lr * momcap) / (np.sqrt(velcap + epsilon)))

        error /= (2*len(X))

        if (epoch+1)%50 == 0:
            print(f'Weights after epoch {epoch+1} : ',weights)
            print(f'Error after epoch {epoch+1} : ',error)


def train_minibatch(X, y, weights, epochs=500, lr =0.01, epsilon = 1e-8, beta1 = 0.9, beta2 = 0.999, bs = 32):
    vel = 0
    mom = 0
    step = 0
    for epoch in range(epochs):
        error = 0
        i = 0
        dw = 0
        for Xi,yi in zip(X,y):
            y_pred = predict(Xi,weights)
            dw += calculate_dw(Xi,yi,y_pred)
            i += 1
            error += calculate_error(yi,y_pred)

            if i%bs == 0 or i==len(X):
                mom = (beta1 * mom) + ((1 - beta1) * dw)
                vel = (beta2 * vel) + ((1 - beta2) * (dw ** 2))
                step += 1
                momcap = mom / (1 - (beta1 ** step))
                velcap = vel / (1 - (beta2 ** step))
                weights -= ((lr * momcap) / (np.sqrt(velcap + epsilon)))
                dw = 0

        error /= (2*len(X))

        if (epoch+1)%50 == 0:
            print(f'Weights after epoch {epoch+1} : ',weights)
            print(f'Error after epoch {epoch+1} : ',error)


dataset = pd.read_csv('bank_note.csv')
dataset.insert(4,'x0',1)

X = dataset[['variance','skewness','curtosis','entropy','x0']].values
y = dataset['class']

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=13,test_size=0.2)
weights = input('Enter 4 weights and 1 bias : ').split()
weights = np.array([float(weight) for weight in weights], dtype='longdouble')

print()
print('---- Adam (Vanilla) ----')
train_vanilla(X_train,y_train,weights.copy())

print()
print('---- Adam (Stochastic) ----')
train_stochastic(X_train,y_train,weights.copy())

print()
print('---- Adam (Mini Batch) ----')
train_minibatch(X_train,y_train,weights.copy())
