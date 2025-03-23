import tracemalloc
import time
import random


inputFile = open("input.txt", "w")
n = 1000
inputFile.write(f"{str(n)}\n")
numbers = random.sample(range(-10**9, 10**9), n)
# numbers = random.sample(range(-10, 10), n)
for i in range(n):
  inputFile.write(f"{numbers[i]} ")
inputFile.seek(0)
inputFile.close()


tracemalloc.start()
start_time = time.perf_counter()


inFile = open("input.txt", "r")

quantityOfNums = int(inFile.readline())
listOfNums = list(map(int, inFile.read().split()))

for i in range(quantityOfNums):
    flag = False
    for j in range(quantityOfNums - 1, i, -1):
       if listOfNums[j] < listOfNums[j - 1]:
           listOfNums[j], listOfNums[j - 1] = listOfNums[j - 1], listOfNums[j]
           flag = True
    if not flag:
        break

outFile = open("output.txt", "w")
for x in listOfNums:
    outFile.write(f"{str(x)} ")
outFile.close()


end_time = time.perf_counter()
currentMemory, peakMemory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнение программы: {end_time - start_time:.5f} секунд")
print(f"Пиковое использование памяти: {peakMemory / 1024 ** 2:.5f} Мб")
