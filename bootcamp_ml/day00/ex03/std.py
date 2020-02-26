import numpy as np
import math
import variance 

def mean(x):
    A = 0
    if len(x) == 0:
        return 0;
    for a in x:
        A = A + a
    return A / len(x)


def std(x):
    return math.sqrt(variance.variance(x))

X = np.array([0, 15, -9, 7, 12, 3, -21])
print(std(X))