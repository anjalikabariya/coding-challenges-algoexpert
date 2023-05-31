# Remove Kth Node From End
# Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node
# from the end of the list.
# The removal should be done in place, meaning that the original data structure should be mutated (no new
# structure should be created).
# Furthermore, the input head of the linked list should remain the head of the linked list after the removal is
# done, even if the head is the node that's supposed to be removed. In other words, if the head is the node
# that's supposed to be removed, your function should simply mutate its value and next pointer.
# Note that your function doesn't need to return anything.
# You can assume that the input Linked List will always have at least two nodes and, more specifically, at
# least k nodes.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the
# list or to None / null if it's the tail of the list.
# Sample Input
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // the head node with value
# k = 4
# Sample Output
# // No output required.
# // The 4th node from the end of the list (the node with value 6) is removed.
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    # find out length of list
    length = 0
    node = head
    while node:
        node = node.next
        length += 1
    # get count of element from front using length
    count = length - k
    # if it's first element to be removed, update value of head in place and pointer
    if count == 0:
        head.value = head.next.value
        head.next = head.next.next
    # traverse through list till previous node is reached and update it's pointer
    else:
        i = 1
        node = head
        while i != count:
            node = node.next
            i += 1
        node.next = node.next.next
        