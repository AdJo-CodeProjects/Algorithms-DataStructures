'''
Insertion Sort:
Description:
Loop over the array to be sorted and move each and every item to its position
For finding the right spot after moving the item to the left you compare every
upcoming item in the array with the current item until you found the next bigger one

Example:
Starting:
[3, 1, 9, 1, 0, 5, 6]

[3, 1, 9, 1, 0, 5, 6]
[1, 3, 9, 1, 0, 5, 6]
[1, 3, 9, 1, 0, 5, 6]
[1, 1, 3, 9, 0, 5, 6]
[0, 1, 1, 3, 9, 5, 6]
[0, 1, 1, 3, 5, 9, 6]
[0, 1, 1, 3, 5, 6, 9]

Pseudocode:
for i = 0 to length(array):
    tmp = array[i]
    pos = i
    while j > 0 array[j-1] > tmp 
        array[j] = array[j-1]
        j=j-1
    array[j] = tmp
'''

def insertion_sort(array):
    sorted = array
    for i in range (0,len(sorted)):
        tmp = sorted[i]
        pos = i          
        #Moving elements from array [0...i-1]
        #greater than key to one pos ahead (right)
        while pos > 0 and sorted[pos-1] > tmp:
            sorted[pos] = sorted[pos-1]
            pos = pos-1
        sorted[pos] = tmp
    return sorted

def insertion_sort_rec(array,n):
    #base case
    if n <= 1:
        return
    insertion_sort_rec(array,n-1)
    #Inserting last element at correct position in sorted array
    last = array[n-1]
    j=n-2
    #Move elements from array [0...i-1]
    #greater than key to one pos ahead (to the right)
    while j>=0 and array[j]>last:
        array[j+1] = array [j]
        j=j-1
    array[j+1]=last
