'''Write a function that takes in a non-empty array of distinct integers and an integer representing a target
sum. The function should find all quadruplets in the array that sum up to the target sum and return a twodimensional array of all these quadruplets in no particular order.
If no four numbers sum up to the target sum, the function should return an empty array.

Sample Input
array = [7, 6, 4, -1, 1, 2]
targetSum = 16

Sample Output
[[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently'''


def findPair(arr, target):
    left = 0
    right = len(arr)-1
    res = []
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            res.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif curr > target:
            right -= 1
        else:
            left += 1
    return res


def fourNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    quads = []
            
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            rem = targetSum - array[i] - array[j]
            pairs = findPair(array[j+1:len(array)], rem)
            for p in pairs:
                quads.append([array[i], array[j]] + p)
    return quads