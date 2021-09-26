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
#plt.show()

out_file = open('submission-2.txt','w')
for w in solution:
    out_file.write(str(w) + ' ')
out_file.close()

# Task2

import re
from scipy.spatial.distance import cosine

in_file = open('10 sentences.txt','r')
lines = in_file.readlines()
in_file.close()

dict_words = {}
i = 0
for line in lines:
    s = line.lower()
    words = re.split('[^a-z]', s)
    for word in words:
        if word not in dict_words and word !='':
            dict_words[word] = i
            i += 1

dict_sentence = {}
array_sentences = []
for line in lines:
    s = line.lower()
    words = re.split('[^a-z]', s)
    for k,v in dict_words.items():
        dict_sentence[k] = 0
    for word in words:
        if word != '':
            dict_sentence[word] += 1
    list_sentence = []
    for k,v in dict_sentence.items():
        list_sentence.append(v)
    array_sentences.append(list_sentence)

dict_result = {}
i = 0
for sen in array_sentences:
    dict_result[i] = cosine(array_sentences[0],array_sentences[i])
    i += 1

list_result = [k for k,v in sorted(dict_result.items(), key = lambda item: item[1])]

out_file = open('submission-1.txt','w')
out_file.write(str(list_result[1]) + ' ')
out_file.write(str(list_result[2]) + ' ')
out_file.close()