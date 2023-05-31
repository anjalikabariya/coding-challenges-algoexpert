# Sum of Linked Lists
# You're given two Linked Lists of potentially unequal length. Each Linked List represents a non-negative
# integer, where each node in the Linked List is a digit of that integer, and the first node in each Linked List
# always represents the least significant digit of the integer. Write a function that returns the head of a new
# Linked List that represents the sum of the integers represented by the two input Linked Lists.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the
# list or to None / null if it's the tail of the list. The value of each LinkedList node is always in the
# range of 0 - 9 .
# Note: your function must create and return a new Linked List, and you're not allowed to modify either of
# the input Linked Lists.
# Sample Input
# linkedListOne = 2 -> 4 -> 7 -> 1
# linkedListTwo = 9 -> 4 -> 5
# Sample Output
# 1 -> 9 -> 2 -> 2
# // linkedListOne represents 1742
# // linkedListTwo represents 549
# // 1742 + 549 = 2291

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    l1 = linkedListOne
    l2 = linkedListTwo
    # create new linkedlist for sum
    newLinkList = LinkedList(0)
    # take pointer for traversing in new list
    l3 = newLinkList
    carry = 0
    # continue till any one list has values or carry is 0
    while l1 or l2 or carry != 0:
        # if any list becomes empty, consider it's value as 0 for further traversal
        num1 = l1.value if l1 is not None else 0
        num2 = l2.value if l2 is not None else 0
        newVal = num1 + num2 + carry
        # carry will always be 1 or 0 as linkedlist will have number < 10
        carry = 1 if newVal > 9 else 0
        # get least significant digit by modular function 
        newVal = newVal % 10
        # create a new node with that value
        newNode = LinkedList(newVal)
        # append it to current pointer of new list
        l3.next = newNode
        # move pointer forward
        l3 = newNode
        # make pointer None if one list is exhausted before other
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    return newLinkList.next
