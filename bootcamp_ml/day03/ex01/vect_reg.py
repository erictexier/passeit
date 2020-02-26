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


X = np.array([0, 15, -9, 7, 12, 3, -21])
print(vectorized_regularization(X, 0.3))
print(vectorized_regularization(X, 0.01))
print(vectorized_regularization(X, 0))