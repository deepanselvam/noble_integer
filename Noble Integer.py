import numpy as np

def noblesnumber(arr):
    arr.sort()
    countSe = 0
    countNe = 0
    if arr[0] == 0:
        countNe += 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            countSe = i
        if countSe == arr[i]:
            countNe += 1
    return countNe

n = int(input())
ar = np.zeros(n, dtype=int)
for i in range(n):
    ar[i] = int(input())
value = noblesnumber(ar)
print(value)
