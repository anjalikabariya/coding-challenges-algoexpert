# Middle Node
# You're given a Linked List with at least one node. Write a function that returns the middle node of the
# Linked List. If there are two middle nodes (i.e. an even length list), your function should return the second
# of these nodes.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the
# list or to None / null if it's the tail of the list.
# Sample Input
# linkedList = 2 -> 7 -> 3 -> 5
# Sample Output
# 3 -> 5
# // The middle could be 7 or 3,
# // we return the second middle node

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    count = 0
    curr = linkedList
    while curr:
        count += 1
        curr = curr.next
    mid = linkedList
    for _ in range(count//2):
        mid = mid.next
    return mid