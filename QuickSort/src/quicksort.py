#include <iostream>
#include <vector>

#
# Stephen Knotts
# sknotts - stephkno@gmail.com
#
#
# quicksort.h
#
# quicksort class method defines basic functions of quicksort algorithm
# saves input as private vector pointer before sorting
#
# unfinished/working/tested
# forgot to update this. it is working with mo3 now
#
import math

class QuickSort:
	def __init__(self, c):
		self.median_of_three_const = c
		self.array = []

	def sort(self, list):
		self.array = list
		self.qs_recursion(0, len(self.array)-1)
		return self.array

	def swap_arr(self, i , j):
		self.array[i], self.array[j] = self.array[j], self.array[i]

	# quick sort partition
	# partition subself.array so that all elements to left of pivot are less than rest
	# using mo3 to pick a pivot
	def partition(self, part, right):
		pivot = self.array[part]
		leftValue = part

		if right - part >= self.median_of_three_const:
			pivot = self.median_of_three(part, right)

		for ptr in range(part+1,right+1):
			if self.array[ptr] < pivot:
				leftValue += 1
				self.swap_arr(ptr,leftValue)

		self.swap_arr(part, leftValue)
		return leftValue

	#median of three method
	#
	#finds pivot value as median of three values from first last and middle
	#also sorts
	def median_of_three(self, left, right):
		median = math.ceil((right + left) / 2)
		#sort three elements
		leftValue = self.array[left]
		rightValue = self.array[right]
		medianValue = self.array[median]

		if rightValue < leftValue:
			self.swap_arr(left, right)

		if medianValue  < leftValue:
			self.swap_arr(median, left)

		if rightValue < medianValue:
			self.swap_arr(right, median)

		return medianValue

	# single step of QS algorithm which calls partition and then calls
	# itself for both subself.s on both sides of partition
	#
	def qs_recursion(self, left, right):
		if left < right:
			pivot = self.partition(left,right)
			self.qs_recursion(left,pivot)# pivot or pivot-1 ?
			self.qs_recursion(pivot+1,right)
