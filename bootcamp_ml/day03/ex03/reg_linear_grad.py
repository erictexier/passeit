def reg_linear_grad(y, x, theta, lambda_):
    """Computes the regularized linear gradient of three non-empty numpy.ndarray,
        with two for-loop. The three arrays must have compatible dimensions.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        x: has to be a numpy.ndarray, a matrix of dimesion m * n.
        theta: has to be a numpy.ndarray, a vector of dimension n * 1.
        alpha: has to be a float.
        lambda_: has to be a float.
    Returns:
        A numpy.ndarray, a vector of dimension n * 1, containing the results of the formula for all j.
        None if y, x, or theta are empty numpy.ndarray.
        None if y, x or theta does not share compatibles dimensions.
    Raises:
        This function should not raise any Exception.
    """
    # from vector gradient
    #    xt = x.transpose()
    #    diffy = x.dot(theta) - y
    #    return xt.dot(diffy) / y.shape[0]

X = np.array([
         [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,10.5,-6])
print(reg_linear_grad(X, Y, Z, 1))
print(reg_linear_grad(X, Y, Z, 0.1, 0.5))
print(reg_linear_grad(X, Y, Z, 0.0))