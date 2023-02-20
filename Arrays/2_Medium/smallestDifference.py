'''
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each
array) whose absolute difference is closest to zero, and returns an array containing these two numbers,
with the number from the first array in the first position.
Note that the absolute difference of two integers is the distance between them on the real number line. For
example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference

sample input:
arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,17]

sample op: [28,26]
'''
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    a1 = 0
    a2 = 0
    min = float("inf")
    curr = float("inf")
    pair = []
    while a1 < len(arrayOne) and a2 < len(arrayTwo):
        one = arrayOne[a1]
        two = arrayTwo[a2]
        if one > two:
            # print("before increment condition 1:",arrayTwo[a2], arrayOne[a1])
            curr =  one - two
            a2 += 1
            # print("after increment condition 1:",arrayTwo[a2], arrayOne[a1])
        elif one < two:
            # print("before increment condition 2:",arrayTwo[a2], arrayOne[a1])
            curr =  two - one
            a1 += 1
            # print("after increment condition 2:",arrayTwo[a2], arrayOne[a1])    
        else:
           return [one, two]
        if curr < min:
            min = curr
            pair = [one, two]
    return pair
    