'''
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

  If no three numbers sum up to the target sum, the function should return an
  empty array.

  sample input:
   array = [12, 3, 1, 2, -6, 5, -8, 6] 
   targetSum = 0
  sample op: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''

def threeNumberSum(array, targetSum):
    # Write your code here.
    triplets = []
    array.sort()
    for i in range(0, len(array)):
        first = i + 1
        last = len(array) - 1
        remainingSum = targetSum - array[i]
        while first < last:
            currentSum = array[first] + array[last]
            if currentSum == remainingSum:
                triplets.append([array[i], array[first], array[last]])
                first += 1
                last -= 1
            elif currentSum > remainingSum:
                last -= 1
            elif currentSum < remainingSum:
                first += 1
    return triplets