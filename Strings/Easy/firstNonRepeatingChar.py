'''Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the
string's first non-repeating character.
The first non-repeating character is the first character in a string that occurs only once.
If the input string doesn't have any non-repeating characters, your function should return -1 .
Sample Input
string = "abcdcaf"
Sample Output
1 // The first non-repeating character is "b" and is found at index 1
'''

def firstNonRepeatingCharacter(string):
    # Write your code here.
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in string:
        if dict[i] == 1:
            return string.index(i)
    return -1
