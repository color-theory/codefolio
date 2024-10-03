"""Tests for the Matrix class"""
import pytest
from mymath import Matrix


class TestMatrix:
    """Tests for the Matrix class"""
    @pytest.mark.parametrize("rows, columns, data, expected", [
        (1, 1, [1], [[1]]),
        (1, 2, [1, 2], [[1, 2]]),
        (2, 1, [1, 2], [[1], [2]]),
        (2, 2, [1, 2, 3, 4], [[1, 2], [3, 4]]),
        (3, 2, [1, 2, 3, 4, 5, 6], [[1, 2], [3, 4], [5, 6]]),
        (2, 3, [1, 2, 3, 4, 5, 6], [[1, 2, 3], [4, 5, 6]]),
    ])
    def test_normal_initialization(self, rows, columns, data, expected):
        """Tests that a matrix is initialized correctly"""
        matrix = Matrix(rows, columns, data)
        assert matrix.matrix == expected

    def test_invalid_initialization(self):
        """Tests that invalid matrix initialization raises an error"""
        with pytest.raises(ValueError):
            Matrix(2, 2, [1, 2, 3])
        with pytest.raises(ValueError):
            Matrix(2, 2, [])
        with pytest.raises(ValueError):
            Matrix(2, 2, [1, 2, 3, 4, 5])

    def test_addition(self, sample_2x2_matrix):
        """Tests matrix addition"""
        matrix2 = Matrix(2, 2, [1, 2, 3, 4])
        result = sample_2x2_matrix + matrix2
        assert result.matrix == [[2, 4], [6, 8]]
        result = sample_2x2_matrix + 2
        assert result.matrix == [[3, 4], [5, 6]]
        result = 2 + sample_2x2_matrix
        assert result.matrix == [[3, 4], [5, 6]]
        with pytest.raises(TypeError):
            result = sample_2x2_matrix + 123.24
        with pytest.raises(TypeError):
            result = sample_2x2_matrix + "string"

    def test_multiplication(self, sample_2x2_matrix):
        """Tests matrix multiplication"""
        matrix2 = Matrix(2, 2, [1, 2, 3, 4])
        result = sample_2x2_matrix * matrix2
        assert result.matrix == [[1, 4], [9, 16]]
        result = sample_2x2_matrix * 2
        assert result.matrix == [[2, 4], [6, 8]]
        result = 2 * sample_2x2_matrix
        assert result.matrix == [[2, 4], [6, 8]]
        with pytest.raises(TypeError):
            result = sample_2x2_matrix * 123.24
        with pytest.raises(TypeError):
            result = sample_2x2_matrix * "string"
        with pytest.raises(ValueError):
            result = sample_2x2_matrix * Matrix(2, 3, [1, 2, 3, 4, 5, 6])
        with pytest.raises(ValueError):
            result = sample_2x2_matrix * Matrix(3, 2, [1, 2, 3, 4, 5, 6])
        with pytest.raises(TypeError):
            result = sample_2x2_matrix * "string"

    def test_dot(self, sample_2x2_matrix):
        """Tests matrix dot product"""
        matrix2 = Matrix(2, 2, [1, 2, 3, 4])
        result = sample_2x2_matrix.dot(matrix2)
        assert result.matrix == [[7, 10], [15, 22]]
        result = sample_2x2_matrix.dot(Matrix(2, 3, [1, 2, 3, 4, 5, 6]))
        assert result.matrix == [[9, 12, 15], [19, 26, 33]]
        with pytest.raises(ValueError):
            result = sample_2x2_matrix.dot(Matrix(3, 2, [1, 2, 3, 4, 5, 6]))
        result = sample_2x2_matrix.dot(123.24)
        assert result == NotImplemented
        result = sample_2x2_matrix.dot("string")
        assert result == NotImplemented
        result = sample_2x2_matrix.dot(2)
        assert result == NotImplemented
        result = sample_2x2_matrix.dot("string")

    def test_transpose(self, sample_2x2_matrix):
        """Tests matrix transpose"""
        result = sample_2x2_matrix.transpose()
        assert result.matrix == [[1, 3], [2, 4]]
        result = Matrix(3, 2, [1, 2, 3, 4, 5, 6]).transpose()
        assert result.matrix == [[1, 3, 5], [2, 4, 6]]
        result = Matrix(2, 3, [1, 2, 3, 4, 5, 6]).transpose()
        assert result.matrix == [[1, 4], [2, 5], [3, 6]]

    def test_copy(self):
        """Tests matrix copy"""
        matrix = Matrix(2, 2, [1, 2, 3, 4])
        assert matrix.matrix == [[1, 2], [3, 4]]
        result = matrix.copy()
        assert result.matrix == [[1, 2], [3, 4]]
        matrix.matrix[0][0] = 5
        assert result.matrix == [[1, 2], [3, 4]]

    def test_determinant(self):
        """Tests matrix determinant"""
        matrix = Matrix(2, 2, [1, 2, 3, 4])
        assert matrix.determinant() == -2
        matrix = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert matrix.determinant() == 0
        matrix = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 10])
        assert matrix.determinant() == -3
        with pytest.raises(ValueError):
            matrix = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
            matrix.determinant()
        with pytest.raises(ValueError):
            matrix = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
            matrix.determinant()
        with pytest.raises(ValueError):
            matrix = Matrix(2, 2, [1, 2, 3, 4, 5])
            matrix.determinant()
        with pytest.raises(ValueError):
            matrix = Matrix(2, 2, [1, 2, 3])
            matrix.determinant()
        with pytest.raises(ValueError):
            matrix = Matrix(2, 2, [])
            matrix.determinant()
