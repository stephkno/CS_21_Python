import math

def search(list, search):
  list.sort()
  # get start index
  low = 0
  high = len(list)
  mid = 0

  while True:
    mid = int(math.floor(low + (high-low)/2))

    if(list[mid] == search):
        return True

    if(low > high or low == high):
      return False

    if(search > list[mid]):
      low = mid+1
      continue

    if(search < list[mid]):
      high = mid-1
      continue
