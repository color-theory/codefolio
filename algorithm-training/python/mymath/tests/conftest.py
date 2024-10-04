"""Defines fixtures for the mymath package tests"""
import pytest
from mymath import Matrix


@pytest.fixture
def sample_2x2_matrix():
    """Returns a 2x2 matrix with values 1, 2, 3, 4"""
    return Matrix(2, 2, [1, 2, 3, 4])
