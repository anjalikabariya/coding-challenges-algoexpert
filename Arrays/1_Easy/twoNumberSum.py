 
'''  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.
  
  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum. 
  You can assume that there will be at most one pair of numbers summing up to
  the target sum. 
  
  sample input
  A = [3, 5, -4, 8, 11, 1, -1, 6]
  t = 10

  sample output
  [11, -1]
  '''

def twoNumberSum(array, targetSum):
    plft = 0
    prght = len(array)-1
    array.sort()
    res = []
    while plft <= prght:
        currSum = array[plft] + array[prght]
        if currSum > targetSum:
            prght -= 1
        elif currSum < targetSum:
            plft += 1
        else:
            return [array[prght], array[plft]]
    return []