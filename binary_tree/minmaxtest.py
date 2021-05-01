from src import tree

tree = tree.Tree()

ints = [9,10,22,1,3,12,40,16,2,6,8,4]

for i in ints:
    tree.insert(i)

for i in tree.getInOrder():
    print(i)

print(tree.findMax()==40)
print(tree.findMin()==1)
print(tree.findMax()==2)
print(tree.findMin()==2)
