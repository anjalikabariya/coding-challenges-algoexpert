# Balanced Brackets
# Write a function that takes in a string made up of brackets ( ( , [ , { , ) , ] , and } ) and other optional
# characters. The function should return a boolean representing whether the string is balanced with regards
# to brackets.
# A string is said to be balanced if it has as many opening brackets of a certain type as it has closing brackets
# of that type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding
# closing bracket that comes before it, and similarly, a closing bracket can't match a corresponding opening
# bracket that comes after it. Also, brackets can't overlap each other as in [(]) .
# Sample Input
# string = "([])(){}(())()()"
# Sample Output
# true // it's balanced

def balancedBrackets(string):
    stack = []
    open = ['(','[','{']
    close = [']',')','}']
    def push(char):
        stack.append(char)
    def pop():
        stack.pop() if stack else -1
    def peek():
        return stack[-1] if stack else -1
    for char in string:
        if char in open:
            push(char)
        elif char in close:
            top = peek()
            if (char == ')' and top == '(') or (char == ']' and top == '[') or (char == '}' and top == '{'):
                pop()
            else:
                return False
        else:
            pass
    if len(stack) > 0:
        return False
    return True
    
