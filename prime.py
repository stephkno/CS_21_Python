import sys
import math

max = int(sys.argv[1])
print(max)

def isprime(num):
    count = 2
    while count < num:
        d = num/count
        if d - math.floor(d) == 0.0:
            return False
        count+=1
    return True

p = 1
for i in range(1, max):
    if isprime(i):
        print(p, i)
        p+=1
