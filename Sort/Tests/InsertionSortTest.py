from Sort.Algorithms.InsertionSort import insertion_sort

def test_is(unsorted):
    return  insertion_sort(unsorted)


print(test_is([1,0,4,1,2,3,6]))
