import itertools
import numpy as np


def bipolar_activation(net, lambdaa = 1):
    return (2/(1+np.exp(-lambdaa*net))) - 1

def unipolar_activation(net, lambdaa = 0.3):
    return (1/(1+np.exp(-lambdaa*net)))

def bipolar_fdash(y_pred):
    return (1/2)*(1-(y_pred**2))

def unipolar_fdash(y_pred):
    return (y_pred*(1-y_pred))

def predict(X, weights, type):
    net = np.dot(X,weights)
    if type == 'unipolar':
        return unipolar_activation(net)
    elif type == 'bipolar':
        return bipolar_activation(net)

def calculate_r(yi, y_pred, type):
    r = yi - y_pred
    if type == 'unipolar':
        return r*unipolar_fdash(y_pred)
    elif type == 'bipolar':
        return r*bipolar_fdash(y_pred)

def train(X,y,weights, type, epochs = 500, c = 0.5):
    for epoch in range(epochs):
        loss = 0
        for Xi, yi in zip(X,y):
            y_pred = predict(Xi, weights, type)
            r = calculate_r(yi, y_pred, type)
            loss += abs(r)
            delta_w = c*r*Xi
            weights += delta_w

        if (epoch+1)%50 == 0 :
            print(f'Weights after epoch {epoch+1} : ',weights)
        if loss == 0:
            break

    print('Learned weights : ', weights)
    weights = weights.reshape((n + 1, 1))
    test(X,y, weights, type)

def test(X, y, learned_weights, type):
    nets = np.dot(X,learned_weights).flatten()
    print('Actual Values : ',y)
    if type == 'unipolar':
        y_pred = np.array([unipolar_activation(net) for net in nets])
        print('Predicted Values : ', y_pred)
    else:
        y_pred = np.array([bipolar_activation(net) for net in nets])
        print('Predicted Values : ', y_pred)

n = int(input('Enter number of bits : '))
X = np.array([list(i) + [1] for i in itertools.product([0,1], repeat = n)])

weights = input(f'Enter initial {n} weights and 1 bias : ')
weights = np.array([float(weight) for weight in weights.split()], dtype='longdouble')
print()

# 1) AND GATE UNIPOLAR
print('---- AND GATE USING PERCEPTRON ----')
y = np.array([0]*(2**n))
y[-1] = 1
train(X, y, weights.copy(), 'unipolar')
print()
print()


# 2) OR GATE UNIPOLAR
print('---- OR GATE USING PERCEPTRON ----')
y = np.array([1]*(2**n))
y[0] = 0
train(X, y, weights.copy(), 'unipolar')
print()
print()


# 3) NOR GATE UNIPOLAR
print('---- NOR GATE USING PERCEPTRON ----')
y = np.array([0]*(2**n))
y[0] = 1
train(X, y, weights.copy(), 'unipolar')
print()
print()


# 4) NAND GATE UNIPOLAR
print('---- NAND GATE USING PERCEPTRON ----')
y = np.array([1]*(2**n))
y[-1] = 0
train(X, y, weights.copy(), 'unipolar')
print()
print()


# 5) AND GATE BIPOLAR
print('---- AND GATE USING PERCEPTRON ----')
y = np.array([-1]*(2**n))
y[-1] = 1
train(X, y, weights.copy(), 'bipolar')
print()
print()


# 6) OR GATE BIPOLAR
print('---- OR GATE USING PERCEPTRON ----')
y = np.array([1]*(2**n))
y[0] = -1
train(X, y, weights.copy(), 'bipolar')
print()
print()


# 7) NOR GATE BIPOLAR
print('---- NOR GATE USING PERCEPTRON ----')
y = np.array([-1]*(2**n))
y[0] = 1
train(X, y, weights.copy(), 'bipolar')
print()
print()


# 8) NAND GATE BIPOLAR
print('---- NAND GATE USING PERCEPTRON ----')
y = np.array([1]*(2**n))
y[-1] = -1
train(X, y, weights.copy(), 'bipolar')
print()
print()
