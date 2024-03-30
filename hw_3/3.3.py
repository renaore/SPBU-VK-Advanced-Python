class Hash:
    """
    The given hash function returns sum of entries of the matrix that are multiplied by their index in row
    (index numbering from 1)
    """
    def __hash__(self):
        return int(sum(sum(element*i for element,i in zip(row,range(1, len(row)+1))) for row in self.matrix))


class Matrix(Hash):
    cache = {}

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

        hash_key = (hash(self), hash(other))
        if hash_key in Matrix.cache.keys():
            product = Matrix.cache[hash_key]
            Matrix.cache.pop(hash_key)
            Matrix.cache[hash_key] = product
            return Matrix(product)

        if len(Matrix.cache) >= 100:
            Matrix.cache.pop(list(Matrix.cache)[0])
        product = [[sum(self.matrix[i][j] * other.matrix[j][k] for j in range(len(self.matrix[0])))
                       for k in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        Matrix.cache[hash_key] = product
        return Matrix(product)


A = Matrix([[3,4],[6,9]])
B = Matrix([[0,0,1],[0,0,0]])
C = Matrix([[5,6],[2,8]])
D = Matrix([[0,0,1],[0,0,0]])

AB = A @ B
Matrix.cache.clear()
CD = C @ D
AB_hash = hash(AB)
CD_hash = hash(CD)

for filename, matrix in [('A.txt', A), ('B.txt', B), ('C.txt', C), ('D.txt', D), ('AB.txt', AB), ('CD.txt', CD)]:
    with open(filename, 'w') as f:
        f.write(str(matrix))
with open('hash.txt','w') as f:
    f.write(str(f'hash AB = {AB_hash} \nhash CD = {CD_hash}'))
