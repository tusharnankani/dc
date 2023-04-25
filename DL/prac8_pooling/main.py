import numpy as np

# custom padding function, alternatively use numpy pad...
# def pad(matrix, p, p_val):
#     hpad = [p_val]*iw
#     vpad = [p_val]*(ih+(2*p))
#
#     for i in range(p):
#         matrix = np.insert(matrix,0,hpad,axis=0)
#         matrix = np.insert(matrix, len(matrix), hpad, axis=0)
#
#     for j in range(p):
#         matrix = np.insert(matrix, 0, vpad, axis=1)
#         matrix = np.insert(matrix, len(matrix[0]), vpad, axis=1)
#
#     return matrix

def pool(matrix, stride, pool_size):
    op_matrix = np.array([[0]*ow for i in range(oh)])
    ih = len(matrix)
    iw = len(matrix[0])
    i = 0
    j = 0
    oi = 0
    oj = 0

    while (i+pool_size <= ih):
        while (j+pool_size <= iw):
            window = []

            for ph in range(pool_size):
                for pw in range(pool_size):
                    window.append(matrix[i+ph][j+pw])

            op_matrix[oi][oj] = max(window)
            oj += 1
            j = j+stride

        i = i+stride
        oi += 1
        j = 0
        oj = 0

    return op_matrix

ih = int(input('Enter height of matrix : '))
iw = int(input('Enter width of matrix : '))
matrix = [[0]*iw for i in range(ih)]

for i in range(ih):
    for j in range(iw):
        matrix[i][j] = int(input(f'Enter value of matrix[{i}][{j}] : '))

p = int(input('Enter amount of padding : '))
p_val = int(input('Enter padding value : '))
s = int(input('Enter amount of stride : '))
pool_size = int(input('Enter pool size : '))

ow = ((iw - pool_size + (2*p))//s) + 1
oh = ((ih - pool_size + (2*p))//s) + 1

matrix = np.array(matrix)
print()
print('Input Matrix :- ')
print(matrix)

print()
matrix = np.pad(matrix,p, constant_values=p_val)
print('After Padding :- ')
print(matrix)

print()
matrix = pool(matrix, s, pool_size)
print('After Pooling :- ')
print(matrix)
