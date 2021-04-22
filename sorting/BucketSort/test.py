from src import bucket_sort
import sys

if sys.stdin.isatty():
    quit()

list = sys.stdin.read()
list = list.split("\n")
list.remove('')
print("In: ", list)
print("Out: ", bucket_sort.sort(list))
