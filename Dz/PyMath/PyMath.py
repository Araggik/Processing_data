from math import sin,exp
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

# Task1

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

def calculate(sol,point):
    sum = 0
    i = 0
    for el in sol:
        sum += el * pow(point,i)
        i += 1
    return sum

def get_values(vec,solut):
    list = []
    for el in vec:
        list.append(calculate(solut,el))
    return list

#vector_a = [1, 15]
#vector_a = [1, 8, 15]
vector_a = [1, 4 , 10 ,15]

solution = solve_sys(vector_a)
vector_y = get_values(vector_a,solution)

plt.plot(vector_a,vector_y)
plt.show()

out_file = open('submission-2.txt', 'w')
for w in solution:
    out_file.write(str(w) + ' ')
out_file.close()

# Task2