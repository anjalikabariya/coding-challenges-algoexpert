'''
  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.'''
def sortedSquaredArray(array):
# Write your code here.
# square and sort/ square and place in sorted position
    left = 0
    n = len(array)-1
    right = n
    res = [0] * len(array)
    while (left <= right) & (n >= 0):
        l = array[left]
        r = array[right]
        if abs(l) > abs(r):
            res[n] = l**2
            n -= 1
            left += 1
        else:
            res[n] = r**2
            n -=1
            right -= 1    
            
    return res
    
A=[1, 2, 3, 5, 6, 8, 9]

sortedSquaredArray(A)

[1, 4, 9, 25, 36, 64, 81]