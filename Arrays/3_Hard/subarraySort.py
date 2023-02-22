'''Write a function that takes in an array of at least two integers and that returns an array of the starting and
ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the
entire input array to be sorted (in ascending order).
If the input array is already sorted, the function should return [-1, -1] .

Sample Input
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

Sample Output
[3, 9]'''

def findHit(array, i):
    if i == 0:
        return array[i] > array[i+1]
    if i ==len(array)-1:
        return array[i] < array[i-1]
    return (array[i] > array[i+1]) or (array[i] < array[i-1])

def subarraySort(array):
    # Write your code here.
    minHit = float("inf")
    maxHit = float("-inf")
    left = 0
    right = len(array)-1
    for i in range(len(array)):
        if findHit(array, i):
            minHit = min(minHit, array[i])
            maxHit = max(maxHit, array[i])
    if minHit == float("inf"):
        return [-1, -1]
    else:
        while array[left] <= minHit:
            left += 1
        while array[right] >= maxHit:
            right -= 1 
    return [left, right]