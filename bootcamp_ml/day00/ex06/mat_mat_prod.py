import numpy as np

def get_col(mat, i):
    return mat[:,i]

def dot(x, y):
    """Computes the dot product of two non-empty numpy.ndarray, using a
        for-loop. The two arrays must have the same dimensions.
    Args:
     x: has to be an numpy.ndarray, a vector.
     y: has to be an numpy.ndarray, a vector.
    Returns:
     The dot product of the two vectors as a float.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share the same dimensions.
    Raises:
     This function should not raise any Exception.
    """
    res = 0
    for a in zip(x,y):
        res += (a[0] * a[1])
    return res

def mat_vec_prod(mat, vec):
    if vec.size == 0 or vec.shape == ():
        return None
    if mat.size == 0 or mat.shape == ():
        return None
    if vec.shape[0] != mat.shape[1]:
        return None
    res = list()
    for line in mat:
        a = 0
        for i,v in enumerate(vec):
            a += (v[0] * line[i])
        res.append(a)
    return np.array(res).reshape( mat.shape[0],1)

def mat_mat_prod(x, y):
    """Computes the product of two non-empty numpy.ndarray, using a
    for-loop. The two arrays must have compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * p.
    Returns:
     The product of the matrices as a matrix of dimension m * p.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
    """
    if x.shape[0] != y.shape[1]:
        return None
    RES = np.zeros((x.shape[0], y.shape[1]))
    for i, line in enumerate(x):
        for j in range(y.shape[1]):
            col = get_col(y,j)
            RES[i][j] = dot(line,col)
    return RES

W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])
Z = np.array([
    [ -6, -1, -8, 7, -8],
        [ 7, 4, 0, -10, -10],
        [ 7, -13, 2, 2, -11],
        [ 3, 14, 7, 7, -4],
        [ -1, -3, -8, -4, -14],
        [ 9, -14, 9, 12, -7],
        [ -9, -4, -10, -3, 6]])
print("W shape",W.shape)
print("Z shape",Z.shape)
res = mat_mat_prod(W, Z)
print(res.shape)
res = mat_mat_prod(Z, W)
print(res.shape)