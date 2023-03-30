'''
remove duplicate values from a given linked list
'''

class Node:
    def __init__(self,value):
        self.previous = None
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def Duplicate(self):
        prev = None
        current = self.head
        while current.next is not None:
            if current.next.data == current.data:
                current.data = current.next.data
            current.next = current.next.next


