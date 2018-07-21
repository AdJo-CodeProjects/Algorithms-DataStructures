'''
Explanation of the Selection Sort:
Selection sort on every iteration searches for the smallest element in the array
Once it is found it is put to the "sorted" part of the array (in this code the left side)
So basically you just iterate through the array on every step and mark the current item
and then compare it to any other item right of it. So once you reached a smaller one, which turns out to be
the smallest available item in the remaining list, you swap it with your current item.

Pseudocode:
A as Array containing the items to be sorted

for i = 0 to size(A) - 1:
    for j=i+1 to size(A):
        if A[i] > A[j]:
            Swap entries:
            Tmp = A[i]
            A[i] = A[j]
            A[j] = Tmp
Example:
Initial array:
[1;0;3;2;4;1]

Step 1:
[0;1;3;2;4;1]
Step 2:
[0;1;1;2;4;3]
Step 3:
[0;1;1;2;4;3]
Step 4:
[0;1;1;2;3;4]

Complexity:
In any case selection sort has a n^2 complexity as it runs through the whole array and remaining array
in any case.
'''

'''
Function sorting an array with the selection sort method
Input: Array
Output: Sorted Array
'''
def selection_sort(array):
    sorted = array
    for i in range(0,len(sorted)-1):
        for j in range(i+1,len(sorted)):
            if sorted[i] > sorted[j]:
                #Swap items:
                tmp =  sorted[i]
                sorted[i] = sorted[j]
                sorted[j] = tmp
    return sorted