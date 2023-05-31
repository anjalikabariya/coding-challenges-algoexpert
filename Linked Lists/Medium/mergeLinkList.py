# Merging Linked Lists
# You're given two Linked Lists of potentially unequal length. These Linked Lists potentially merge at a shared
# intersection node. Write a function that returns the intersection node or returns None / null if there is
# no intersection.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the
# list or to None / null if it's the tail of the list.
# Note: Your function should return an existing node. It should not modify either Linked List, and it should
# not create any new Linked Lists.
# Sample Input
# linkedListOne = 2 -> 3 -> 1 -> 4
# linkedListTwo = 8 -> 7 -> 1 -> 4
# Sample Output
# 1 -> 4 // The lists intersect at the node with value 1

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    setOfNodes = set()
    node1 = linkedListOne
    node2 = linkedListTwo
    while node1 is not None:
        setOfNodes.add(node1)
        node1 = node1.next
    while node2 is not None:
        if node2 in setOfNodes:
            return node2
        node2 = node2.next
    return None


# solution 2
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    node1 = linkedListOne
    node2 = linkedListTwo
    
    l1 = getLength(linkedListOne)
    l2 = getLength(linkedListTwo)
    # difference of length
    d = abs(l1 - l2)
    # assign pointers as per length
    bigList = linkedListOne if l1 > l2 else linkedListTwo
    smallList = linkedListTwo if bigList == linkedListOne else linkedListOne
    # traverse from start to difference in node in the bigger list
    for i in range(d):
        bigList = bigList.next
        
    # compare each node in both list till you find common node
    while bigList is not None and smallList is not None:
        if bigList is smallList:
            return bigList
        bigList = bigList.next
        smallList = smallList.next
        
            

def getLength(linkedList):
    node = linkedList
    count = 0
    while node is not None:
        count += 1
        node = node.next
    return count
