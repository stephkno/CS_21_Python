from lib import tree
import random
import math
import time

# create tree
tree = tree.Tree()
n = 999999

# welcome message
print("Binary tree in Python")
print("Demo with 999999 integers...")

# create random list
insert_list = [x for x in range(n)]
random.shuffle(insert_list)

# insert list elements
for i,element in enumerate(insert_list):
    if(i%10000==0):
        print("Inserting element #{}: {}...".format(i,element))
    tree.insert(element)

# tree traversal
print("In order tree traversal in 3 seconds... ")
time.sleep(3)
for i,int in enumerate(tree.getInOrder()):
    print("Integer #{}: {}".format(i, int))

# reverse tree
print("Reversing tree...")
tree.reverseTree()
time.sleep(3)

# reversed tree traversal
for i,int in enumerate(tree.getInOrder()):
    print("Integer #{}: {}".format(i, int))

print("Done. Discarding tree.")
