"""
matrix.py

Matrix class for matrix operations

Available Functions:
- add(value): Add a value to the matrix
- multiply(value): Multiply a value to the matrix
- dot(value): Dot product of two matrices
- transpose(): Transpose the matrix
- flatten(): Flatten the matrix
- copy(): Copy the matrix
- determinant(): Calculate the determinant of the matrix
"""


class Matrix:
    """Matrix class"""
    rows = 0
    columns = 0
    matrix = []
    matrix_row = []
    data_count = 0
    temp_matrix_list = []
    temp_product = 0

    def __init__(self, rows, columns, data):
        """Initialize the matrix"""
        if data is None:
            data = []
        self.matrix = []
        self.rows = rows
        self.columns = columns
        if len(data) != rows * columns:
            raise ValueError("Data size does not match matrix size")
        for _ in range(rows):
            self.matrix_row = []
            for _ in range(columns):
                self.matrix_row.append(data[self.data_count])
                self.data_count += 1
            self.matrix.append(self.matrix_row)

    def add(self, value):
        """
        Add a value to the matrix

        Parameters:
        value: int or Matrix

        Returns:
        Matrix: Result of the addition
        """
        if isinstance(value, int):
            temp_matrix_list = []
            for i in range(self.rows):
                for j in range(self.columns):
                    temp_matrix_list.append(self.matrix[i][j] + value)
        elif isinstance(value, Matrix):
            temp_matrix_list = []
            if self.rows != value.rows or self.columns != value.columns:
                raise ValueError("Matrices are not of the same size")
            for i in range(self.rows):
                for j in range(self.columns):
                    temp_matrix_list.append(
                        self.matrix[i][j] + value.matrix[i][j])
        else:
            return NotImplemented
        return Matrix(self.rows, self.columns, temp_matrix_list)

    def __add__(self, value):
        """Special method for addition"""
        return self.add(value)

    def __radd__(self, other):
        """Special method for right addition"""
        return self.add(other)

    def multiply(self, value):
        """
        Multiply a value to the matrix

        Parameters:
        value: int or Matrix

        Returns:
        Matrix: Result of the multiplication
        """
        if isinstance(value, int):
            temp_matrix_list = []
            for i in range(self.rows):
                for j in range(self.columns):
                    temp_matrix_list.append(self.matrix[i][j] * value)
        elif isinstance(value, Matrix):
            temp_matrix_list = []
            if self.columns != value.columns or self.rows != value.rows:
                raise ValueError("Matrices are not of the same size")
            for i in range(self.rows):
                for j in range(value.columns):
                    temp_matrix_list.append(
                        self.matrix[i][j] * value.matrix[i][j])
        else:
            return NotImplemented
        return Matrix(self.rows, self.columns, temp_matrix_list)

    def __mul__(self, value):
        """
        Special method for multiplication
        """
        return self.multiply(value)

    def __rmul__(self, other):
        """
        Special method for right multiplication
        """
        return self.multiply(other)

    def dot(self, value):
        """
        Dot product of two matrices

        Parameters:
        value: Matrix

        Returns:
        Matrix: Result of the dot product
        """
        if isinstance(value, Matrix):
            if self.columns != value.rows:
                raise ValueError("Matrices are not of compatible size")
            temp_matrix_list = []
            for i in range(self.rows):
                for j in range(value.columns):
                    self.temp_product = 0
                    for k in range(self.columns):
                        self.temp_product += self.matrix[i][k] * \
                            value.matrix[k][j]
                    temp_matrix_list.append(self.temp_product)
        else:
            return NotImplemented
        return Matrix(self.rows, value.columns, temp_matrix_list)

    def transpose(self):
        """
        Transpose the matrix

        Returns:
        Matrix: Transposed matrix
        """
        temp_matrix_list = []
        for i in range(self.columns):
            for j in range(self.rows):
                temp_matrix_list.append(self.matrix[j][i])
        return Matrix(self.columns, self.rows, temp_matrix_list)

    def flatten(self):
        """
        Flatten the matrix

        Returns:
        list: Flattened matrix
        """
        temp_matrix_list = []
        for r in range(self.rows):
            for c in range(self.columns):
                temp_matrix_list.append(self.matrix[r][c])
        return temp_matrix_list

    def copy(self):
        """
        Copy the matrix

        Returns:
        Matrix: Copied matrix
        """
        return Matrix(self.rows, self.columns, self.flatten())

    def determinant(self):
        """
        Calculate the determinant of the matrix

        Returns:
        int: Determinant of the matrix
        """
        if self.rows != self.columns:
            raise ValueError("Matrix is not square")
        if self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        result = 0
        rows = list(range(len(self.matrix)))
        for focus in rows:
            temp_matrix = self.copy()
            temp_matrix.matrix = temp_matrix.matrix[1:]
            subrows = len(temp_matrix.matrix)
            for j in range(subrows):
                temp_matrix.matrix[j] = temp_matrix.matrix[j][0:focus] + \
                    temp_matrix.matrix[j][focus+1:]
            sign = (-1) ** (focus % 2)
            temp_matrix.rows -= 1
            temp_matrix.columns -= 1
            subdeterminant = temp_matrix.determinant()

            result += sign * self.matrix[0][focus] * subdeterminant
        return result
