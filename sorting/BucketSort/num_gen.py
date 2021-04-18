from src import bucket_sort
import random

n = 1000000
num_length = 8

num = [0 for _ in range(num_length)]
numlist = []

print(num_length)

for i in range(n):
    for n in range(num_length):

        num[n] += round(random.random()*9)
        num[n] = num[n] % 9

    nstring = ""
    for n in num:
        nstring += str(n)
    numlist.append(nstring)


print(numlist)
