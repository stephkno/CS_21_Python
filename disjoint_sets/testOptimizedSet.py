#
# script to test optimization function of disjointSet
#
from lib import disjointSet

set = disjointSet.Set()

n = 100
# create new subset with size n
set.new_subset(n)

# join all subsets
for i in range(n):
    set.union(i,i+1)

# test if 100th set is parented to 1st set
print(set.get(100).value==100)
print(set.get(100).parent.value==1)
