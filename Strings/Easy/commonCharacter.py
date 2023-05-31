# Common Characters
# Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are
# common to all strings in the list, ignoring multiplicity.
# Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can
# be in any order.
# Sample Input
# strings = ["abc", "bcd", "cbaccd"]
# Sample Output
# ["b", "c"] // The characters could be ordered differently

def commonCharacters(strings):
    # Write your code here.
    charCounts = {}
    for s in strings:
        unique = set(s)
        for c in unique:
            if c not in charCounts:
                charCounts[c] = 0
            charCounts[c] += 1
    res = []
    for char, count in charCounts.items():
        if count == len(strings):
            res.append(char)
    return res

