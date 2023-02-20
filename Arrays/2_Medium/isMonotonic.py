'''Write a function that takes in an array of integers and returns a boolean representing whether the array is
monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely
non-decreasing.
Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly,
non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.
Note that empty arrays and arrays of one element are monotonic.

Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output
true
'''

def isMonotonic(array):
    # Write your code here.
    inc = 0
    dec = 0
    if len(array) <= 1:
        return True
    for i in range(0, len(array)-1):
        if (array[i+1] > array[i]):
            inc += 1
        elif (array[i+1] < array[i]):
            dec += 1
        else:
            inc += 1
            dec += 1
    if (inc == len(array)-1) or (dec == len(array)-1):
        return True
    else:
        return False
