from src import binarySearch
import random

list = []
search = [99, 100]

for i in range(99999):
  if(i not in search):
    list.append(i)

random.shuffle(list)

print(binarySearch.search(list, search[0])==False)
print(binarySearch.search(list, 3)==True)
print(binarySearch.search(list, 100)==False)
