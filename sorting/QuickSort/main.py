#!/usr/bin/python3

from src import quicksort
import random
import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    print("Provide number")

list = [x for x in range(n)]
random.shuffle(list)
print(list)

sorter = quicksort.QuickSort(10)
list = sorter.sort(list)
print(list)
