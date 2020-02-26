import numpy as np

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

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

print(mse(X, Y))
print(mse(X, X))