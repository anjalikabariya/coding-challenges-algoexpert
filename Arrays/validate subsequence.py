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
        
a = [5, 1, 22, 25, 6, -1, 8, 10]
s = [1,6,-1,10]

isValidSubsequence(a,s)
True