'''
Testing the selection sort functionality
'''
import unittest

from Sort.Algorithms.SelectionSort import selection_sort



unsorted = [0,1,3,2,4,1]
sorted = selection_sort(unsorted)
print(sorted)

unsorted = [1,3,4,5,8,9,3,0,0,3,4,6,5,1,7,8,9,10,11,15,200,9,18,14,102,202,3,495,1,5,6]
sorted = selection_sort(unsorted)
print(unsorted)
