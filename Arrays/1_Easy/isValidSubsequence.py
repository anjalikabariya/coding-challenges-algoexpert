'''Given two non-empty arrays of integers, write a function that determines whether the second array is a
subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in
the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence
of the array [1, 2, 3, 4] , and so do the numbers [2, 4] . Note that a single number in an array and
the array itself are both valid subsequences of the array.

sample input
a = [5, 1, 22, 25, 6, -1, 8, 10]
s = [1,6,-1,10]

sample output
True'''

def isValidSubsequence(array, sequence):
    # Write your code here.
    # Write your code here.
    count = 0
    # when subsequence is greater than array
    if len(sequence) > len(array):
        # print("False. sequence is greater than array")
        return False
    else:
        for i in array:
            if count == len(sequence):
                return True
            # print(sequence[count], i)
            # if value matches
            if sequence[count] == i:
                # check if it's last value, if not increment pointer
                if count < len(sequence):
                    count += 1
                else:
                    # print(count)
                    break
        return count == len(sequence)