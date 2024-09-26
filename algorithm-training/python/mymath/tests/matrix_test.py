from mymath import Matrix
import pytest

class TestMatrix:
	@pytest.mark.parametrize("rows, columns, data, expected", [
		(2, 2, [1, 2, 3, 4], [[1, 2], [3, 4]]),
		(2, 2, [], [[None, None], [None, None]]),
		(2, 2, [1, 2, 3], [[1, 2], [3, None]]),
		(2, 2, [1, 2, 3, 4, 5], [[1, 2], [3, 4]])
	])
	def test_initialization(self, rows, columns, data, expected):
		matrix = Matrix(rows, columns, data)
		assert matrix.matrix == expected
						 
	def test_addition(self, sample_2x2_matrix):
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