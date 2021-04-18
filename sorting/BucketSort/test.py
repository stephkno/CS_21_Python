from src import bucket_sort
import sys

if sys.stdin.isatty():
    quit()

list = sys.stdin.read()
n = int(list[0])

bucket_sort.sort(list[1:],n)
