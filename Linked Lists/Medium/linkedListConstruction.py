# Linked List Construction
# Write a DoublyLinkedList class that has a head and a tail , both of which point to either a linked list Node or None / null . The
# class should support:
# Setting the head and tail of the linked list.
# Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1 ).
# Removing given nodes and removing nodes with given values.
# Searching for nodes with given values.
# Note that the setHead , setTail , insertBefore , insertAfter , insertAtPosition , and remove methods all take in actual
# Node s as input parameters—not integers (except for insertAtPosition , which also takes in an integer representing the position); this
# means that you don't need to create any new Node s in these methods. The input nodes can be either stand-alone nodes or nodes that are
# already in the linked list. If they're nodes that are already in the linked list, the methods will effectively be moving the nodes within the linked
# list. You won't be told if the input nodes are already in the linked list, so your code will have to defensively handle this scenario.
# If you're doing this problem in an untyped language like Python or JavaScript, you may want to look at the various function signatures in a typed
# language like Java or TypeScript to get a better idea of what each input parameter is.
# Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node or None /
# null .
# Sample Usage
# // Assume the following linked list has already been created:
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# // Assume that we also have the following stand-alone nodes:
# 3, 3, 6
# setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as th
# setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with valu
# insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node wit
# insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone
# insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a s
# removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value
# remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
# containsNodeWithValue(5): true




# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isAlone(self, node):
        if node.prev is None and node.next is None:
            return True
        return False
        
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if node is None:
            return
        if not self.isAlone(nodeToInsert):
            self.remove(nodeToInsert)
        # insert in new position, by updating pointers of prev node 
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if not node.prev:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
            
    def insertAfter(self, node, nodeToInsert):
        if node is None:
            return
        if not self.isAlone(nodeToInsert):
            self.remove(nodeToInsert)
        # insert in new position, by updating pointers of next node
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if not node.next:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
            
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        curr = 1
        while curr < position:
            node = node.next
            curr += 1
        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.insertAfter(self.tail, nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            toRemove = node
            node = node.next
            if toRemove.value == value:
                self.remove(toRemove)

    def remove(self, node):
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
        
    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False
