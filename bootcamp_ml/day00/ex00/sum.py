import numpy as np

def sum_(x, f):
    """Computes the sum of a non-empty numpy.ndarray onto wich a function is
        applied element-wise, using a for-loop.
        Args:
        x: has to be an numpy.ndarray, a vector.
        f: has to be a function, a function to apply element-wise to the vector.
        Returns:
        The sum as a float.
        None if x is an empty numpy.ndarray or if f is not a valid function.
        Raises:
        This function should not raise any Exception.
    """
    A = 0
    try:
        if x.size == 0:
            return None
    except:
        return None
    for a in x:
        try:
            A = A + f(a)
        except:
            return None
    return A

X = np.array([0, 15, -9, 7, 12, 3, -21])
sum_(X, lambda x: x)
X = np.array([0, 15, -9, 7, 12, 3, -21])
sum_(X, lambda x: x**2)