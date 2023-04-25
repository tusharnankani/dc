import numpy as np

def convolve(matrix, fil, stride):
    op_matrix = np.array([[0]*ow for i in range(oh)])

    i = 0
    j = 0
    oi = 0
    oj = 0

    while (i+fh <= ih):
        while (j+fw <= iw):

            window = []
            for winh in range(fh):
                for winw in range(fw):
                    window.append(matrix[i+winh][j+winw])

            print(window, " * ",  fil.ravel())

            op_matrix[oi][oj] = np.dot(np.array(window), fil.ravel())
            oj += 1
            j = j+stride

        i = i+stride
        oi += 1
        j = 0
        oj = 0

    return op_matrix

ih = int(input('Enter height of matrix : '))
iw = int(input('Enter width of matrix : '))
fh = int(input('Enter height of filter : '))
fw = int(input('Enter width of filter : '))
print()

matrix = [[0]*iw for i in range(ih)]
fil = [[0]*fw for i in range(fh)]

for i in range(ih):
    for j in range(iw):
        matrix[i][j] = int(input(f'Enter value of matrix[{i}][{j}] : '))
print()

for i in range(fh):
    for j in range(fw):
        fil[i][j] = int(input(f'Enter value of filter[{i}][{j}] : '))
print()

p = int(input('Enter amount of padding : '))
p_val = int(input('Enter padding value : '))
s = int(input('Enter amount of stride : '))

ow = ((iw - fw + (2*p))//s) + 1
oh = ((ih - fh + (2*p))//s) + 1

fil = np.array(fil)
print('\nInput Filter :- ')
print(fil)

matrix = np.array(matrix)
print('\nInput Matrix :- ')
print(matrix)

matrix = np.pad(matrix, p, constant_values=p_val)
print('\nAfter Padding :- ')
print(matrix)

op_matrix = convolve(matrix, fil, s)
print('\nAfter Convolution :- ')
print(op_matrix)
