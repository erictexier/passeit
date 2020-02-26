import numpy as np

def predict_(theta, X):
    """
    Description:
        Prediction of output using the hypothesis function (linear model).
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
    Returns:
        pred: numpy.ndarray, a vector of dimension (number of the training examples,1).
        None if X does not match the dimension of theta.
    Raises:
        This function should not raise any Exception.
    """

    bias = theta[0]
    if theta.size < 2 or theta.shape[0] < 2:
        return None
    new_theta = theta[1:]
    try:
        return (X.dot(new_theta) + bias)
    except:
        print("Incompatible dimension match between X and theta.")
        return None

def vec_gradient(x, y, theta):
    """
    Description:
        Computes a gradient vector from three non-empty numpy.ndarray,
        without any for-loop. The three arrays must have the compatible dimensions.
    Args:
        x: has to be an numpy.ndarray, a matrice of dimension m * n. 
        y: has to be an numpy.ndarray, a vector of dimension m * 1. 
        theta: has to be an numpy.ndarray, a vector n * 1.
    Returns:
        The gradient as a numpy.ndarray, a vector of dimensions n * 1, containg
        the result of the formula for all j.
        None if x, y, or theta are empty numpy.ndarray.
        None if x, y and theta do not have compatible dimensions.
    Raises:
        This function should not raise any Exception.
    """
    xt = x.transpose()
    diffy = x.dot(theta) - y
    return xt.dot(diffy) / y.shape[0]

def cost_elem_(theta, X, Y):
    """
    Description:
        Calculates all the elements 0.5*M*(y_pred - y)^2 of the costnfunction.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
    Returns:
        J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
        None if there is a dimension matching problem between X, Y or theta.
    Raises:
        This function should not raise any Exception.
    """
    pred = predict_(theta, X)
    cost = (Y - pred)**2
    return (cost/(2 * X.shape[0]))

def mse(y, y_hat):
    """Computes the mean squared error of two non-empty numpy.ndarray, using
    a for-loop. The two arrays must have the same dimensions. Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector. Returns:
    The mean squared error of the two vectors as a float. None if y or y_hat are empty numpy.ndarray.
    None if y and y_hat does not share the same dimensions.
    Raises:
    This function should not raise any Exception.
    """
    if y.size == 0 or y.ndim == 0:
        return None
    if y_hat.size == 0 or y_hat.ndim == 0:
        return None
    return np.sum((y - y_hat)**2)/y.shape[0]

def cost_(theta, X, Y):
    """
    Description:
        Calculates the value of cost function.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a vector of dimension (number of training examples, number of features).
    Returns:
        J_value : has to be a float.
        None if X does not match the dimension of theta.
    Raises:
        This function should not raise any Exception.
    """
    pred = predict_(theta, X)
    return mse(Y,pred)/2
    # what 1/2 * mse does:
    # cost = (Y - pred)**2
    # return np.sum(cost)/(2 * X.shape[0])


def fit_(theta, X, Y, alpha = 0.01, n_cycle=2000):
    """
    Description:
        Performs a fit of Y(output) with respect to X.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
        Y: has to be a numpy.ndarray, a vector of dimension (number of training examples, 1).
    Returns:
        new_theta: numpy.ndarray, a vector of dimension (number of the features +1,1).
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exception.
    """
    acost = cost_(theta,X, Y)
    n_samples = Y.shape[0]
    print("COST TO START={}, nb_of sample={}".format(acost, n_samples))
    print("shape theta", theta.shape)
    print("THETA", theta.transpose())
    Ttheta = theta.transpose()

    xp = np.ones((X.shape[0],1))
    X2 = np.concatenate((xp,X), axis=1)
    print(X2)
    #a_theta = theta.transpose()
    all_ = np.zeros((n_cycle,1))

    for i in range(n_cycle):
        theta = theta - (alpha/n_samples * vec_gradient(X2, Y, theta))
        all_[i] = cost_(theta, X, Y)

    return (all_, theta)

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
theta1 = np.array([[1.], [1.]])
theta2 = fit_(theta1, X1, Y1, alpha = 0.01, n_cycle=2000)
print(theta2)

#predict_(theta1, X1)