'''
***Double Linked List***
'''
class Node:
    def __init__(self,value):
        self.previous = None
        self.data= value
        self.next =None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def Length(self):
        temp = self.head
        count =0
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    def InsertAtTheBegining(self,value):
        new_node =Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head =new_node
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

new = DoublyLinkedList()
print(new.isEmpty())
new.InsertAtTheBegining(5)
new.InsertAtTheBegining(10)
new.InsertAtTheBegining(20)
new.InsertAtTheBegining(30)
new.InsertAtTheBegining(50)
new.printLinkedList()
print()
print(new.Length())