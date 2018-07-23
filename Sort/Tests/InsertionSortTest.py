from Sort.Algorithms.InsertionSort import insertion_sort
from Sort.Algorithms.InsertionSort import insertion_sort_rec

def test_is(unsorted):
    return  insertion_sort(unsorted)


print(test_is([1,0,4,1,2,3,6]))

def test_is_rec():
    arr = [4,1,3,4,2,1,9,0,7,5]
    insertion_sort_rec(arr,len(arr))
    print(arr)

test_is_rec()