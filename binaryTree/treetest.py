from src import tree as Tree
import random

print("Binary tree - 04/03/2021")
tree = Tree()
n = 10000

insert_list = []
for i in range(n):
      insert_list.push(i)

random.shuffle(insert_list)

for i in range(n):
  tree.insert(insert_list[i])

print(tree.getInOrder())
print(tree.reverseTree())
print(tree.getInOrder())
