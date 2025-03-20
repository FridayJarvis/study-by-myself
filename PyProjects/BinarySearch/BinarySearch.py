import time
import tracemalloc
import random


inputFile = open("input.txt", "w")
n = 100_000
inputFile.write(f"{str(n)}")
for i in range(n):
    inputFile.write(f" {str(10**9 - n + i)}")
k = n - 1
inputFile.write(f"\n{str(k)}")
for i in range(k):
    inputFile.write(f" {str(random.randint(1, 10**9))}")
inputFile.close()


tracemalloc.start()
start_time = time.time()


inFile = open("input.txt", "r")

numsArr = list(map(int, inFile.readline().split(" ")))
quantityOfNums = numsArr.pop(0)

targets_to_search = list(map(int, inFile.readline().split(" ")))
quantityOfTargets = targets_to_search.pop(0)

inFile.close()

outFile = open("output.txt", "w")

for i in range(quantityOfTargets):
    head = len(numsArr) - 1
    begin = 0
    isFind = False

    while begin <= head:
        middle = (begin + head) // 2

        if targets_to_search[i] == numsArr[middle]:
            outFile.write(f"{middle} ")
            isFind = True
            break
        elif targets_to_search[i] > numsArr[middle]: begin = middle + 1
        else: head = middle - 1

    if not(isFind): outFile.write(f"{-1} ")

outFile.close()


end_time = time.time()
resultTime = end_time - start_time
currentMemory, peakMemory = tracemalloc.get_traced_memory()
tracemalloc.stop()


print(f"Время выполнения: {resultTime:.2f} секунды")
print(f"Пиковое использование памяти: {peakMemory / 1024 / 1024:.2f} MB")