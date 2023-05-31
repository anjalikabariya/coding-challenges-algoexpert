# Min Max Stack Construction
# Write a MinMaxStack class for a Min Max Stack. The class should support:
# Pushing and popping values on and off the stack.
# Peeking at the value at the top of the stack.
# Getting both the minimum and the maximum values in the stack at any given point in time.
# All class methods, when considered independently, should run in constant time and with constant space.
# Sample Usage
# // All operations below are performed sequentially.
# MinMaxStack(): - // instantiate a MinMaxStack
# push(5): -
# getMin(): 5
# getMax(): 5
# peek(): 5
# push(7): -
# getMin(): 5
# getMax(): 7
# peek(): 7
# push(2): -
# getMin(): 2
# getMax(): 7
# peek(): 2
# pop(): 2
# pop(): 7
# getMin(): 5
# getMax(): 5
# peek(): 5

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        
    def peek(self):
        return self.stack[-1]["elem"] if self.stack else -1

    def pop(self):
        return self.stack.pop()["elem"] if self.stack else -1

    def push(self, number):
        self.stack.append({
            "elem": number,
            "min": number if not self.stack else min(number, self.getMin()),
            "max":number if not self.stack else max(number, self.getMax())
        })

    def getMin(self):
        return self.stack[-1]["min"] if self.stack else -1

    def getMax(self):
        return self.stack[-1]["max"] if self.stack else -1
