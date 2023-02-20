'''You're given an array of integers and an integer. Write a function that moves all instances of that integer in
the array to the end of the array and returns the array.
The function should perform this in place (i.e., it should mutate the input array) and doesn't need to
maintain the order of the other integers.

Sample Input
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently'''

def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left < right:
        if array[right] == toMove:
            right -= 1
        if array[left] != toMove:
            left += 1
        if (array[left] == toMove) and (array[right] != toMove):
            array[right], array[left] = array[left], array[right]
            left += 1
            right -= 1
    return array