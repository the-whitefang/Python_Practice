'''
Program to insert the student marks of 10 student marks (scored out of 100) and perform the following operations.
1. to insert a mark of a student at a particular position/ index
2. to display the mark of two student from a particular index
'''

class Node:

    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None

class Teacher:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return None
        return False

    def StudentMarks(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

