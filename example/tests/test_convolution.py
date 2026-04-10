# this file contains tests of convolution.py
# run pytest from the terminal to run tests
import numpy as np
from numpy.testing import assert_allclose
import pytest
from example import convolution

def test_zero_input():
    """
    Tests that scalar convolution with zero returns zero
    """
    size = 10
    test_K = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    zero = np.zeros(size)
    assert np.array_equal(convolution.scalar(test_K, 0), zero)

def test_multiplying_correctly():
    """
    Test that scalar convolution with 1 returns kernel
    """
    test_K = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert np.array_equal(convolution.scalar(test_K, 1), test_K)

def test_vector_convolution_error():
    """
    Ensure that running vector convolution returns expected result for zero
    vector
    """
    test_K = np.ones((5, 4), dtype=float)
    test_f = np.zeros(4, dtype=float)
    expected_result = 0
    # currently this will return an exception.  After editing
    # convolution.vector() to return the correct result, remove the context
    # manager
    with pytest.raises(NotImplementedError):
        # we use assert_allclose() here to allow rounding error
        assert_allclose(convolution.vector(test_K, test_f), expected_result)
