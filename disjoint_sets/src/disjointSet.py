#!/usr/bin/python3

#disjoint set

#create_set() creates new set with one node
#union()
#find()

import random
import sys
sys.setrecursionlimit(99999)

#class to represent subset node
class SetNode:
	def __init__(self, value):
		self.value = value+1
		self.parent = self
		self.rank = 1

#class to represent set of subsets
class Set:
	def __init__(self):
		self.sets = []

	#print set as string
	#Node:int Parent:int
	#
	def __str__(self):
		return_string = ""
		for i,node in enumerate(self.sets):
			return_string += "Node:{} Parent:{}\n".format(node.value, node.parent.value)

		return return_string

	#create new set with n nodes
	def new_subset(self, number):
		for i in range(number):
			self.sets.append(SetNode(i))

	def get(self, index):
		return self.sets[index-1]

	#merge two sets
	def union(self, subset1, subset2):
		#find subset object given set index
		subset1 = self.get(subset1)
		subset2 = self.get(subset2)
		#find subset roots
		root1 = self.find(subset1)
		root2 = self.find(subset2)

		#subset with fewer nodes is joined to larger subset
		if subset1.rank > subset2.rank:
			self.find(subset2).parent = subset1.parent
		else:
			self.find(subset1).parent = subset2.parent

		#increment subset ranks
		subset1.rank += subset2.rank
		subset2.rank += subset1.rank

	#return root of given subset
	def find_root(self, subset):
		return self.find(subset)

	#determine if two subsets are joined
	def same_set(self, subset1, subset2):
		return self.find_root(self.get(subset1)) == self.find_root(self.get(subset2))

	#recursive find function
	def find(self, subset):
		#call find function on subset's parent
		#if it is not parented to itself (root node)
		if subset.parent != subset:
			subset = self.find(subset.parent)
		#return (root) subset as subset for each node
		return subset
