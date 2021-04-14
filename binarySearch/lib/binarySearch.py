import math

def binarySearch(list, search):
  list.sort()
  # get start index
  low = 0
  high = list.length
  mid

  while(list[mid] != search):
    mid = math.floor(low + (high-low)/2)

    if(low > high or low == high):
      return False

    if(search > list[mid]):
      low = mid+1
      continue

    if(search < list[mid]):
      high = mid-1
      continue


  # item has been found
  return True
