import numpy as np

def mean(x):
    A = 0
    if len(x) == 0:
        return 0;
    for a in x:
        A = A + a
    return A / len(x)



def variance(x):
    """Computes the variance of a non-empty numpy.ndarray, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The variance as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """
    ep = mean(x)
    A = 0
    for a in x:
        A = A + ((a-ep) * (a-ep))
    return A/len(x)


X = np.array([0, 15, -9, 7, 12, 3, -21])
res = variance(X)
