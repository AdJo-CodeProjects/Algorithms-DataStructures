'''
Description:
Bubble Sort works by swapping the adjacent elements over and over again
until they are all in the right order

Pseudocode:
for(n=length(array), n>1, n=n-1):
    for(i=0, i < n-1 , i=i+1):
        if array[i] > array[i+1]:
            array.swap(array[i],array[i+1])

Optimized Bubblesort:
n = length(array)
while(n > 1):
    ntmp = 1
    for(i=0,i<n-1,++i):
        if array[i] > array [i+1]:
            array.swap(array[i],array[i+1])
            ntmp = ntmp+1
    n=ntmp

Expamles:


Complexity:
At least one execution through whole array, so in optimal (already sorted) case O(n)
In any other case O(n^2) as he has to run through the swaps and then one time again for checking/hitting the ending case
'''
#implemented straight on reading the algorithms description and one visual example
def my_bubblesort(array):
    sorted = array
    was_swapped = True
    while(was_swapped):
        counter = 0
        was_swapped = False
        while(counter < len(sorted)-1):
            if sorted[counter] > sorted[counter+1]:
                tmp = sorted[counter]
                sorted[counter] = sorted[counter+1]
                sorted[counter+1]=tmp
                was_swapped = True
            counter += 1
    return sorted

#optimization 1:  working directly on parameter array as we don't need it afterwards but sorted
#optimization 2:  working more efficiently on for loops seeing how many swaps occured and counting them
#                 in case no other swap occured than one you can assume the new array is optimal
def optimized_bubblesort(array):
    n = len(array)
    while(n>1):
        ntmp = 1
        #start, stop, step
        for i in range (0, n-1):
            if (array[i] > array [i+1]):
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1]=tmp
                ntmp = ntmp+1
        n=ntmp