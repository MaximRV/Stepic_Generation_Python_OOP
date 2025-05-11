class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self.data[row][col]

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def __repr__(self):
        return f'{self.__class__.__name__}{self.rows,self.cols}'

    def __str__(self):
        return '\n'.join(' '.join([str(j) for j in i]) for i in self.data)

    def __pos__(self):
        return Matrix(self.rows,self.cols, value=1)

    def __neg__(self):
        neq_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                neq_matrix.data[i][j] = -self.data[i][j]
        return neq_matrix

    def __invert__(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def __round__(self, ndigits=0):
        rounded_data = [[round(value, ndigits) for value in row] for row in self.data]
        return Matrix(self.rows, self.cols, value=0).from_data(rounded_data)

    def from_data(self, data):
        self.data = data
        return self



