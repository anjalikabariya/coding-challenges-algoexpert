'''Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble
Sort algorithm to sort the array.
If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual Overview section of this
question's video explanation before starting to code.
Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
'''

def bubbleSort(array):
    # Write your code here.
    swaps = True
    skip = 0
    while swaps:
        # marker to check if swaps occured
        swaps = False
        for i in range(len(array)-1-skip):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                # swap occured so update marker
                swaps = True
        # skip last element after one round of traversal
        skip += 1
    return array