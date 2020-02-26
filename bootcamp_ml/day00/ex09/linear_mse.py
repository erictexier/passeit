import numpy as np

def vec_mse(y, y_hat):
	"""Computes the mean squared error of two non-empty numpy.ndarray,
	without any for loop. The two arrays must have the same dimensions. Args:
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
	a = y_hat - y
	b = (y_hat - y).transpose()
	return b.dot(a)/y.size

def linear_mse(x, y, theta):
	"""Computes the mean squared error of three non-empty numpy.ndarray,
	using a for-loop. The three arrays must have compatible dimensions. Args:
	y: has to be an numpy.ndarray, a vector of dimension m * 1.
	x: has to be an numpy.ndarray, a matrix of dimesion m * n. theta: has to be an numpy.ndarray, a vector of dimension n * 1.
	Returns:
	The mean squared error as a float.
	None if y, x, or theta are empty numpy.ndarray.
	None if y, x or theta does not share compatibles dimensions.
	Raises:
	This function should not raise any Exception.
	"""
	f = x.dot(theta)
	return vec_mse(f, y)

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
print(linear_mse(X, Y, Z))