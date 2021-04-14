from lib import binarySearch
import random

list = []
search = [99, 100]

for i in range(999):
  if(i not in search):
    list[i] = i

random.shuffle(list)

console.log(binarySearch(list, search[0])==false)
console.log(binarySearch(list, 3)==true)
console.log(binarySearch(list, 100)==false)
