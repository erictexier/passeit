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
    if theta.size == 0 or theta.shape[0] < 2:
        return None
    bias = theta[0]
    new_theta = theta[1:]
    try:
        return (X.dot(new_theta) + bias)
    except:
        print("Incompatible dimension match between X and theta.")
        return None

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
print(predict_(theta1, X1).transpose())
# array([[2], [6], [10], [14.], [18.]])

X2 = np.array([[1], [2], [3], [5], [8]])
theta2 = np.array([[2.]])
predict_(theta2, X2)

# Incompatible dimension match between X and theta.

X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta3 = np.array([[0.05], [1.], [1.], [1.]])
print(predict_(theta3, X3).transpose())
# array([[22.25], [44.45], [66.65], [88.85]])