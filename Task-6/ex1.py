import numpy as np
import random
import math

def calс_geometric_mean(arr: np.ndarray):
    mult = 1
    for num in arr:
        mult *= num

    return math.pow(mult, 1/arr.size)

def calc_sum(arr:np.ndarray):
    summa = 0
    for num in arr:
        if (num % 2 == 0) and (num % 3 != 0):
            summa += num
    return summa

n = 3

arr = np.ndarray(n)

for i in range(0, n):
    arr[i] = int(input())

gmean = calс_geometric_mean(arr)
summa = calc_sum(arr)

print(arr)
print(gmean)
print(summa)
