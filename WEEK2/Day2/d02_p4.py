'''
Python program to reverse a linked list
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head =None

    def reverse(self):
        prev =None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev =current
            current = next
        self.head = prev
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

new = LinkedList()
new.push(84)
new.push(15)
new.push(4)
new.push(20)
print("Given Linked List")
new.printList()
new.reverse()
print("\nReversed Linked List")
new.printList()