import numpy as np
import random

def multiplicate_matrix(first_matrix: np.ndarray, second_matrix: np.ndarray):
    resault_matrixv = None

    if(are_matrix_valid(first_matrix, second_matrix)):
        resault_matrix = np.ndarray((first_matrix.shape[0], second_matrix.shape[1]))
        for i in range(resault_matrix.shape[0]):
            for j in range(resault_matrix.shape[1]):
                for k in range(first_matrix.shape[0]):
                    resault_matrix[i, j] += first_matrix[i, k] * second_matrix[k,j]

    return resault_matrix

def are_matrix_valid(first_matrix: np.ndarray, second_matrix: np.ndarray):
    return ((first_matrix.shape[1] == second_matrix.shape[0]) 
        and (first_matrix.shape[0] == second_matrix.shape[1]))

a = random.randint(0, 5)
b = random.randint(0, 5)
g = random.randint(0, 5)
v = random.randint(0, 5)
u = random.randint(0, 5)

Amatrix = np.array([[2, 3 + a, 4 - u], 
                    [b, g, v], 
                    [5, 10*u, -2]])

Bmatrix = np.array([[b, -3, 4 + u], 
                    [a, 4, v], 
                    [5 * u, 10, -2]])

Cmatrix = np.array([[-1, 3 + u, 4 - v], 
                    [2, 1, v], 
                    [5, 5 - u, -2]])

print(Amatrix)
print(Bmatrix)
AxB = multiplicate_matrix(Amatrix, Bmatrix)
print(AxB)
print(np.matmul(Amatrix, Bmatrix))