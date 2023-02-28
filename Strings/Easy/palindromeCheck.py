'''Write a function that takes in a non-empty string and that returns a boolean representing whether the
string is a palindrome.
A palindrome is defined as a string that's written the same forward and backward. Note that singlecharacter strings are palindromes.
Sample Input
string = "abcdcba"
Sample Output
true // it's written the same forward and backward
'''

def isPalindrome(string):
    # Write your code here.
    l = 0
    r = len(string)-1
    while l <= r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True