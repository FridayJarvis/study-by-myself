import random
import time
import sys

sys.setrecursionlimit(10000)
start_time = time.time()

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smallest = []
    largest = []
    equal = []

    for i in range(len(arr)):
        if arr[i] < pivot:
            smallest.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])
        else:
            largest.append(arr[i])

    return quickSort(smallest) + equal + quickSort(largest)
end_time = time.time()

arr = [random.randint(-10000, 10000) for i in range(1_000_000)]
print(arr, '\n', "============================================================================================\n")
print(quickSort(arr))
print(end_time - start_time, "seconds")
