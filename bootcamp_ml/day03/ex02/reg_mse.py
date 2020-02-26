import numpy as np

def vectorized_regularization(theta, lambda_):
    """Computes the regularization term of a non-empty numpy.ndarray,without any for-loop.
    Args:
     theta: has to be a numpy.ndarray, a vector of dimension n * 1.
     lambda: has to be a float.
    Returns:
     The regularization term of theta.
     None if theta is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """

    #if theta.shape[1] != 1:
    #    print("Wrong shape")
    #    return None
    return theta.dot(theta.transpose()) * lambda_

def reg_mse(y, x, theta, lambda_):
    """Computes the regularized mean squared error of three non-empty   
        numpy.ndarray, without any for-loop. The three arrays must have compatible
        dimensions.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        x: has to be a numpy.ndarray, a matrix of dimesion m * n.
        theta: has to be a numpy.ndarray, a vector of dimension n * 1.
        lambda: has to be a float.
    Returns:
        The mean squared error as a float.
        None if y, x, or theta are empty numpy.ndarray.
        None if y, x or theta does not share compatibles dimensions.
    Raises:
        This function should not raise any Exception.
    """
    nb_sample = Y.shape[0]
    res = vectorized_regularization(theta, lambda_)
    U = X.dot(theta) - Y
    diff = (U.transpose()).dot(U)
    return (diff + res)/nb_sample

X = np.array([
         [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])
print(reg_mse(X, Y, Z, 0))
print(reg_mse(X, Y, Z, 0.1))
print(reg_mse(X, Y, Z, 0.5))