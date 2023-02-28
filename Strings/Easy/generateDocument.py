'''You're given a string of available characters and a string representing a document that you need to
generate. Write a function that determines if you can generate the document using the available
characters. If you can generate the document, your function should return true ; otherwise, it should
return false .
You're only able to generate the document if the frequency of unique characters in the characters string is
greater than or equal to the frequency of unique characters in the document string. For example, if you're
given characters = "abcabc" and document = "aabbccc" you cannot generate the document
because you're missing one c .
The document that you need to create may contain any characters, including special characters, capital
letters, numbers, and spaces.
Note: you can always generate the empty string ( "" ).
Sample Input
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
Sample Output
true
'''

def generateDocument(characters, document):
    # Write your code here.
    if len(document) == 0:
        return True
    c_dict = createDict(characters)
    d_dict = createDict(document)
    for key in d_dict:
        if d_dict[key] > c_dict.get(key, 0):
            return False
    return True


def createDict(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict