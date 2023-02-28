'''Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a
function that returns a new string obtained by shifting every letter in the input string by k positions in the
alphabet, where k is the key.
Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns
the letter a .
Sample Input
string = "xyz"
key = 2
Sample Output
"zab"
'''

def caesarCipherEncryptor(string, key):
    # Write your code here.
    # traverse through string, use ord to get int of letter
    # ord(a) = 97, ord(z) = 122. put condition for encountering z
    # return chars from index using chr(index)
    newStr = ""
    key = key % 26
    for i in range(len(string)):
        index = ord(string[i])
        if index + key > 122:
            index = 96 + (index + key) % 122
            # index = shift(key, index)
        else:
            index += key
        newStr += chr(index)
    return newStr


# def shift(index, key):
#     if key > 26:
#         key -= (key//26) * 26
#         index += key
#     else:
#         index = index + key - 122 + 96
#     if index > 122:
#         index = index - 122 + 96
#     return index