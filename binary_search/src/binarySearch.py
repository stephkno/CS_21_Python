import math

# binary search function
def search(list, search):
  list.sort()
  low = 0
  high = len(list)
  mid = 0

  while True:
    # get mid index
    mid = int(math.floor(low + (high-low)/2))

    # have we found element
    if(list[mid] == search):
        return True

    # we have not found element - two ends have met
    if(low > high or low == high):
      return False

    # we are too far to left
    if(search > list[mid]):
      low = mid+1
      continue

    # we are too far to right
    if(search < list[mid]):
      high = mid-1
      continue
