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
    if theta.size < 2 or theta.shape[0] < 2:
        return None
    bias = theta[0]
    new_theta = theta[1:]
    try:
        return (X.dot(new_theta) + bias)
    except:
        print("Incompatible dimension match between X and theta.")
        return None

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
    return np.sum((y-y_hat)**2)/y.shape[0]

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
    return (cost/(2*X.shape[0]))

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
    # what 1/2 mse does:
    #cost = (Y - pred)**2
    #return np.sum(cost)/(2 * X.shape[0])

X0 = np.array([[1],[2],[3]])
Y0 = np.array([[1],[2],[3]])
theta0 = np.array([[0],[0]])
print (" 0:",cost_(theta0,X0,Y0))

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print("COST_ELEM", cost_elem_(theta1, X1, Y1).transpose())
print("COST:",cost_(theta1, X1, Y1))


X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
Y2 = np.array([[19.], [42.], [67.], [93.]])
print("COST_ELEM2",cost_elem_(theta2, X2, Y2).transpose())
#array([[1.3203125], [0.7503125], [0.0153125], [2.1528125]])
print("COST",cost_(theta2, X2, Y2))
#4.238750000000004