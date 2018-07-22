'''
Testing the selection sort functionality
'''
from Sort.Algorithms.SelectionSort import selection_sort

def test_ss(unsorted):
    return  selection_sort(unsorted)


print(test_ss([1,0,4,1,2,3,6]))
