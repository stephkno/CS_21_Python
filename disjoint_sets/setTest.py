#
# script to test basic functions of disjointSet
#
from lib import disjointSet

set = disjointSet.Set()

n = 10
# create new subset with size n
set.new_subset(n)

# join some subsets
set.union(1,2)
set.union(2,3)
set.union(3,4)
set.union(6,5)

# test connection between 6 & 1
print(set.same_set(6,1) == False)
print(set.same_set(4,1) == True)
