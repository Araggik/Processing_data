from math import sin,exp
import numpy as np
from scipy.linalg import solve

def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

def solve_sys(vec):
    n = len(vec)
    array_a = []
    vector_b = []
    for el in vec:
        list = []
        for i in range(n):
            list.append(pow(el,i))
        array_a.append(list)
        vector_b.append(f(el))
    narray_a = np.array(array_a)
    nvector_b = np.array(vector_b)
    return solve(narray_a,nvector_b)

vector_a = [1, 15]


