
from src import bubble_sort
import sys
import random

n = 1000
list = [int(random.random()*100) for _ in range(n)]

print(bubble_sort.sort(list))
