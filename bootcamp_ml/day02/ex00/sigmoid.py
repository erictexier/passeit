import numpy as np
from collections import abc

def sigmoid_(x):
    """
    Compute the sigmoid of a scalar or a list.
    Args:
        x: a scalar or list
    Returns:
        The sigmoid value as a scalar or list.
        None on any error.
    Raises:
        This function should not raise any Exception.
    """
    y = 1 + np.exp(-x)
    if y != 0:
        return 1/y
    return None