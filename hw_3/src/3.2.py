import numpy as np

class WriteToFile:
    def write_object(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

class Str:
    def __str__(self):
        return '[' + '\n '.join('[' + ' '.join(str(element) for element in row) + ']'
                                    for row in self.matrix) + ']'

class GetterSetter:
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, new_matrix):
        new_matrix = [[element for element in row] for row in new_matrix]
        assert (type(new_matrix) is list and all(type(row) is list for row in new_matrix)
                and all(len(row) == len(new_matrix[0]) for row in new_matrix))
        self._matrix = new_matrix


class MatrixArithmetic(WriteToFile, Str, GetterSetter, np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, matrix):
        self.matrix = matrix

    def __array_ufunc__(self, ufunc, method, *inputs, out=None, **kwargs):
        if out:
            return NotImplemented
        inputs = [obj.matrix if isinstance(obj, MatrixArithmetic) else obj for obj in inputs]
        result = None
        if method == '__call__':
            result = getattr(ufunc, method)(*inputs, **kwargs)
        return MatrixArithmetic(result) if result is not None else NotImplemented

np.random.seed(0)
a = MatrixArithmetic(np.random.randint(0, 10, (10, 10)))
b = MatrixArithmetic(np.random.randint(0, 10, (10, 10)))

mat_add = a + b
mat_mul = a * b
mat_matmul = a @ b

for filename, matrix in [('matrix+.txt', mat_add), ('matrix_element_wise.txt',mat_mul),('matrix@.txt',mat_matmul)]:
    matrix.write_object(filename)
