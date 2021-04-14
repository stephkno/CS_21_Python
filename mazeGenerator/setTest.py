from lib import disjointSet

set = disjointSet.DisjointSet()

n = 6
# create new subset with size n
set.new_subset(n)

# join some subsets
set.union(3,2)
set.union(0,3)
set.union(2,0)

# test connection between 6 & 1
print(set.same_set(2,3) == True)
print(set.same_set(0,3) == True)
print(set.same_set(3,0) == True)
print(set.same_set(3,1) == True)
print(set.same_set(3,2) == True)
print(set.same_set(1,0) == True)
print(set.same_set(0,1) == True)
