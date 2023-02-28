'''Write a function that takes in an array of at least three integers and, without sorting the input array, returns
a sorted array of the three largest integers in the input array.
The function should return duplicate integers if necessary; for example, it should return [10, 10, 12]
for an input array of [10, 5, 9, 10, 12] .
Sample Input
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample Output
[18, 141, 541]
'''

def findThreeLargestNumbers(array):
    # Write your code here.
    arr = [min(array[0], array[1], array[2]), 0, max(array[0], array[1], array[2])]
    if (array[0] >= array[1] and array[0] <= array[2]) or (array[0] <= array[1] and array[0] >= array[2]):
        arr[1] = array[0]
    elif (array[1] >= array[0] and array[1]<= array[2]) or (array[1] <= array[0] and array[1] >= array[2]):
        arr[1] = array[1]
    else:
        arr[1] = array[2]
    minN = arr[0]
    midN = arr[1]
    maxN = arr[2]
    for i in range(3, len(array)):
        if array[i] >= maxN:
            minN = midN
            midN = maxN
            maxN = array[i]
        elif array[i] >= midN and array[i] < maxN:
            minN = midN
            midN = array[i]
        elif array[i] > minN and array[i] < midN:
            minN = array[i]
    arr = [minN, midN, maxN]
    return arr