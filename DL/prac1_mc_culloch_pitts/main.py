import itertools
import numpy as np


def predict(X, y, weights, threshold):
    net = np.dot(X,weights)
    y_pred = (net >= threshold).astype(int).flatten()

    print('Net : ', net.flatten())
    print('Weights : ',weights.flatten())
    print('Threshold : ',threshold)
    print('Actual Values : ', y)
    print('Predicted Values : ',y_pred)


# 1) NOT GATE
X = np.array([[0], [1]])
y = np.array([1, 0])
w = np.array([-1]).reshape((1,1))
T = 0
print('\n---- NOT GATE ----')
predict(X,y,w,T)


n = int(input('\nEnter number of bits : '))
X = np.array([list(i) for i in itertools.product([0, 1], repeat=n)])

# 2) AND GATE
y = np.array([0]*(2**n))
y[-1] = 1
w = np.array([1]*(n)).reshape((n,1))
T = n
print('\n\n---- AND GATE ----')
predict(X,y,w,T)


# 3) OR GATE
y = np.array([1]*(2**n))
y[0] = 0
w = np.array([1]*(n)).reshape((n,1))
T = 1
print('\n\n---- OR GATE ----')
predict(X,y,w,T)


# 4) NAND GATE
y = np.array([1]*(2**n))
y[-1] = 0
w = np.array([-1]*(n)).reshape((n,1))
T = -n+1
print('\n\n---- NAND GATE ----')
predict(X,y,w,T)


# 5) NOR GATE
y = np.array([0]*(2**n))
y[0] = 1
w = np.array([-1]*(n)).reshape((n,1))
T = 0
print('\n\n---- NOR GATE ----')
predict(X,y,w,T)

'''

---- NOT GATE ----
Net :  [ 0 -1]
Weights :  [-1]
Threshold :  0
Actual Values :  [1 0]
Predicted Values :  [1 0]

Enter number of bits : 3


---- AND GATE ----
Net :  [0 1 1 2 1 2 2 3]
Weights :  [1 1 1]
Threshold :  3
Actual Values :  [0 0 0 0 0 0 0 1]
Predicted Values :  [0 0 0 0 0 0 0 1]


---- OR GATE ----
Net :  [0 1 1 2 1 2 2 3]
Weights :  [1 1 1]
Threshold :  1
Actual Values :  [0 1 1 1 1 1 1 1]
Predicted Values :  [0 1 1 1 1 1 1 1]


---- NAND GATE ----
Net :  [ 0 -1 -1 -2 -1 -2 -2 -3]
Weights :  [-1 -1 -1]
Threshold :  -2
Actual Values :  [1 1 1 1 1 1 1 0]
Predicted Values :  [1 1 1 1 1 1 1 0]


---- NOR GATE ----
Net :  [ 0 -1 -1 -2 -1 -2 -2 -3]
Weights :  [-1 -1 -1]
Threshold :  0
Actual Values :  [1 0 0 0 0 0 0 0]
Predicted Values :  [1 0 0 0 0 0 0 0]
'''