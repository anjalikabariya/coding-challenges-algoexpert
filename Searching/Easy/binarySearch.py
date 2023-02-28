'''Write a function that takes in a sorted array of integers as well as a target integer. The function should use
the Binary Search algorithm to determine if the target integer is contained in the array and should return
its index if it is, otherwise -1 .
If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of this
question's video explanation before starting to code.
Sample Input
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
Sample Output
3'''

def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1
        else:
            return mid
    return -1
