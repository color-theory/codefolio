import pytest
from mymath import Matrix

@pytest.fixture
def sample_2x2_matrix():
	return Matrix(2, 2, [1, 2, 3, 4])