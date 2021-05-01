#!/usr/local/bin/python3
# Binary tree
# class for single node in binary tree

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

  # get successor
  # leftmost node of right subtree
    def successor(self):
      currentNode = self.right
      while(currentNode.left != None):
          currentNode = currentNode.left

      return currentNode

  # get predecessor
  # rightmost node of left subtree
    def predecessor(self):
        currentNode = self.left
        while(currentNode.right != None):
            currentNode = currentNode.right

        return currentNode



# Tree class for structure of tree and tree functions
#
# 04/02/21
class Tree:
    def __init__(self):
        self.root = None
        self.verbose = False
        self.inverted = False

  # determine if input value is fit for insertion ;)
    def testInput(self, n):
      if(type(n) == 'int'):
          throw ("Must only insert numbers.")

  # insert node to tree
    def insert(self, n):
        self.testInput(n)
        self.debug("Insert ")
        if(not self.root):
            self.root = Node(n, None)
            self.debug("Added root node")
            return True
        else:
            parentNode = None
            currentNode = self.root

      # repeat process until we reach leaf
        while (currentNode != None):
            parentNode = currentNode
            if (n > currentNode.value and not self.inverted) or (n < currentNode.value and self.inverted):
                self.debug("Traversing right")
                currentNode = currentNode.right
            elif (n < currentNode.value and not self.inverted) or (n > currentNode.value and self.inverted):
                self.debug("Traversing left")
                currentNode = currentNode.left
            else:
                # node already exists in tree
                self.debug("Insertion failed")
                raise("Insertion failed - value already in tree")
                return(False)

            self.debug(parentNode)

        # if we get here it means we have found where to place nod
        if((n > parentNode.value and not self.inverted) or (n < parentNode.value and self.inverted)):
            parentNode.right = Node(n, parentNode)
            self.debug("Insert right")
        elif((n < parentNode.value and not self.inverted) or (n > parentNode.value and self.inverted)):
            parentNode.left = Node(n, parentNode)
            self.debug("Insert left")

        return True

    def findMax(self):
        currentNode = self.root
        while not currentNode.right == None:
            currentNode = currentNode.right

        return currentNode.value

    def findMin(self):
        currentNode = self.root
        while not currentNode.left == None:
            currentNode = currentNode.left

        return currentNode.value

  # find node in tree by value -> return node object
    def find(self, n):
        self.testInput(n)
        self.debug("Find: ", n)
        currentNode = self.root
        if(currentNode.value == n):
            return currentNode


        while (currentNode != None and currentNode.value != n ):
            if ((n > currentNode.value and not self.inverted) or (n < currentNode.value and self.inverted)):
                self.debug("Traversing right")
                currentNode = currentNode.right
            elif((n < currentNode.value and not self.inverted) or (n > currentNode.value and self.inverted)):
                self.debug("Traversing left")
                currentNode = currentNode.left

        # did we find the number?
        return currentNode

  # test if node is in tree
    def contains(self, n):
        if(n==self.root.value):
            return True

        a = self.find(n)
        if(a):
            self.debug("Found ", a)

        return a!=None

        # node children test cases
    def hasLeftChild(self, node):
        return node.left and not node.right

    def hasRightChild(self, node):
        return not node.left and node.right

    def hasBothChildren(self, node):
        return node.left and node.right

    def isLeaf(self, node):
        return not node.left and not node.right

    # tree traversals
    def preOrder(self, node, list=[]):
        if(not node):
            return list

            list.append(node.value)
            self.preOrder(node.left, list)
            self.preOrder(node.right, list)
            return list

    def inOrder(self, node, list):
        if(not node):
            return list

        self.inOrder(node.left, list)
        list.append(node.value)
        self.inOrder(node.right, list)
        return list

    def postOrder(self, node, list):
        if(not node):
            return list

        self.postOrder(node.left, list)
        self.postOrder(node.right, list)
        list.append(node.value)
        return list

    # recursive function for reversing Tree
    # also switches tree insert/search mode
    def invert(self, node):
        if(not node):
            return False

        self.invert(node.left)
        self.invert(node.right)
        self.swap(node)
        return True

    # function to initialize tree reversal
    def invertTree(self):
        self.inverted = not self.inverted
        return self.invert(self.root)

    # node swap helper
    def swap(self, node):
        tmp = node.right
        node.right = node.left
        node.left = tmp

    # traversals
    def getPreOrder(self):
        return self.preOrder(self.root, [])

    def getPostOrder(self):
        return self.postOrder(self.root, [])

    def getInOrder(self):
        return self.inOrder(self.root, [])

    # delete element from list
    def delete(self, n):
        # get node to delete
        currentNode = self.find(n)
        # node not found
        self.debug("Delete ", n)
        if(not currentNode):
            return False

        # node has no children
        if(self.isLeaf(currentNode)):
          if(currentNode == self.root):
            self.root = None
            return True

          if(currentNode.parent.right == currentNode):
            currentNode.parent.right = None
            return True

          if(currentNode.parent.left == currentNode):
            currentNode.parent.left = None
            return True
          return False

        # node has only left child
        if(self.hasLeftChild(currentNode)):
          if(currentNode == self.root):
            self.root.value = self.root.left.value
            self.root.left = None
            return True

          if(currentNode.parent.left == currentNode):
            currentNode.parent.left = currentNode.left
            return True

          if(currentNode.parent.right ==currentNode):
            currentNode.parent.right = currentNode.right
            return True

          return False

        # node has only right child
        if(self.hasRightChild(currentNode)):
          if(currentNode == self.root):
            self.root.value = self.root.right.value
            self.root.right = None
            return True

          if(currentNode.parent.left == currentNode):
            currentNode.parent.left = currentNode.right
            return True

          if(currentNode.parent.right == currentNode):
            currentNode.parent.right = currentNode.right
            return True

          return False

        # node has two children
        if(self.hasBothChildren(currentNode)):
          successor = currentNode.successor()
          currentNode.value = successor.value

          if(successor.parent == None):
            return True

          if(successor.parent.right != None and successor.parent.right == successor):
            successor.parent.right = None
            return True

          if(successor.parent.left != None and successor.parent.right == successor):
            successor.parent.left = None
            return True


        self.debug("No delete")
        return False

    # debug log helper
    def debug(self, arguments):
        if(self.verbose):
            print(arguments)
