# -- coding: utf8 --
import numpy as np


arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.size)

arr1 = np.arange(0, 20, 1.5)  # От 0 до 20 с шагом 1,5
print(arr1)

arr2 = np.linspace(1,20,5)
print(arr2)

random_arr = np.random.random((5,))
print(random_arr)

matrix = np.array([(1,2,3),(6,3,2),(4,7,9)])
print(matrix)

