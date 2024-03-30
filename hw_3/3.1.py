import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '[' + '\n '.join('[' + ' '.join(str(element) for element in row) + ']'
                                    for row in self.matrix) + ']'

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Matrix sizes must match')
        return Matrix([[self.matrix[i][j]+other.matrix[i][j] for j in range(len(self.matrix[0]))]
                       for i in range (len(self.matrix))])

    def __mul__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Matrix sizes must match')
        return Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(len(self.matrix[0]))]
                       for i in range (len(self.matrix))])

    def __matmul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError('Number of columns of left matrix must match with number of rows of right matrix')
        return Matrix([[sum(self.matrix[i][j] * other.matrix[j][k] for j in range(len(self.matrix[0])))
                       for k in range(len(other.matrix[0]))] for i in range(len(self.matrix))])

np.random.seed(0)
a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

mat_add = a + b
mat_mul = a * b
mat_matmul = a @ b

for filename, matrix in [('matrix+.txt', mat_add), ('matrix_element_wise.txt',mat_mul),('matrix@.txt',mat_matmul)]:
    with open(filename, 'w') as f:
        f.write(str(matrix))

