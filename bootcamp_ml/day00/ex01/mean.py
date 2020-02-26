import numpy as np


def mean(x):
    """Computes the mean of a non-empty numpy.ndarray, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The mean as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """
    A = 0
    if len(x) == 0:
        return 0;
    for a in x:
        A = A + a
    return A / len(x)

np.array([0, 15, -9, 7, 12, 3, -21])
X = np.array([0, 15, -9, 7, 12, 3, -21])
mean(X ** 2)