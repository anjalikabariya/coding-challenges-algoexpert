'''You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
Write a function that returns a modified version of the Linked List that doesn't contain any nodes with
duplicate values. The Linked List should be modified in place (i.e., you shouldn't create a brand new list),
and the modified Linked List should still have its nodes sorted with respect to their values.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the
list or to None / null if it's the tail of the list.

Sample Input
linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 // the head node with value 1
{
  "head": "1",
  "nodes": [
    {"id": "1", "next": "1-2", "value": 1},
    {"id": "1-2", "next": "1-3", "value": 1},
    {"id": "1-3", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 3},
    {"id": "3", "next": "3-2", "value": 4},
    {"id": "3-2", "next": "3-3", "value": 4},
    {"id": "3-3", "next": "4", "value": 4},
    {"id": "4", "next": "5", "value": 5},
    {"id": "5", "next": "5-2", "value": 6},
    {"id": "5-2", "next": null, "value": 6}
  ]
}
Sample Output
1 -> 3 -> 4 -> 5 -> 6 // the head node with value 1
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    node = linkedList
    # traverse till end
    while node is not None:
        next = node.next
        # traverse and update next pointer till you encounter same value
        while next is not None and next.value == node.value:
            next = next.next
        # when treaversed through, update current node's next to be new next
        node.next = next
        # continue cycle by updating current node to be next node
        node = next
    return linkedList
