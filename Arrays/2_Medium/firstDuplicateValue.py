'''Given an array of integers between 1 and n , inclusive, where n is the length of the array, write a
function that returns the first integer that appears more than once (when the array is read from left to
right).
In other words, out of all the integers that might occur more than once in the input array, your function
should return the one whose first duplicate value has the minimum index.
If no integer appears more than once, your function should return -1 .
Note that you're allowed to mutate the input array.

Sample Input #1
array = [2, 1, 5, 2, 3, 3, 4]

Sample Output #1
2 // 2 is the first integer that appears more than once.
// 3 also appears more than once, but the second 3 appears after the second 2.


Sample Input #2
array = [2, 1, 5, 3, 3, 2, 4]

Sample Output #2
3 // 3 is the first integer that appears more than once.
// 2 also appears more than once, but the second 2 appears after the second 3.'''

def firstDuplicateValue(array):
    # Write your code here.
  
# we can mutate the array and values are going to be between 1 & n at max where n=len(array)
# so mark the values in array at their indices with -1(visited)
# if we encounter -1 while continuing through array traversal, that means value is duplicated
    # [1,2,4,2,4,5] n=6
    for value in array:
        posValue = abs(value)
        # posValue = 1, 2, 4, 2, 4, 5
        if array[posValue-1] < 0:
            # array[1-1] is not < 0 
            # array[2-1] is not < 0
            # array[4-1] is not < 0
            # array[2-1] is < 0
            # so posValue will be returned i.e. 2
            return posValue
        # array[0] = -1
        # array[1] = -2
        # array[3] = -2
        array[posValue-1] *= -1
    return -1