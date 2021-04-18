#!/usr/bin/python3

from src import quicksort
import random
import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    quit()

list = [x for x in range(n)]
random.shuffle(list)

sorter = quicksort.QuickSort(10)
list = sorter.sort(list)
#print(list)
