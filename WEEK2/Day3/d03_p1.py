'''
***Double Linked List***
'''


class Node:
    def __init__(self, value):
        self.previous = None
        self.data = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def Length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def InsertAtTheBegining(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def InsertAtPosition(self, value, position):
        temp = self.head
        count = 0
        while temp is not None:
            if count == position - 1:
                break
            count += 1
            temp = temp.next
            if position == 1:
                self.InsertAtTheBegining(value)
            elif temp is None:
                print("There are less than {}-1 elements in the linked list")
            elif temp.next is None:
                self.InsertAtTheEnd(value)
            else:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.previous = temp
                temp.next.previous = new_node
                temp.next = new_node

    def InsertAtTheEnd(self, value):  # function to insert an element at the end of the double linked list.
        new_node = Node(value)
        if self.isEmpty():
            self.InsertAtTheBegining(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp

    def DeleteFromBegining(self):  # function to delete an element from the begining of a double linked list
        if self.isEmpty():
            print("Linked list is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def DeleteFromLast(self):  # function to delete an element from the last of a double linked list
        if self.isEmpty():
            print("Linked list is empty. Cannot delete elements")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.previous.next = None
            temp.previous = None

    def DeleteFromASpecificPosition(self,position):
        if self.isEmpty():
            print("linked lis is empty. cannot delete elements")
        elif position == 1:
            self.DeleteFromBegining()
        else:
            temp = self.head
            count = 1
            while temp is None:
                if count == position:
                    break
                temp = temp.next
                count = count +1
            if temp is None:
                print("There are less than {} elements in linked list")
                return
            elif temp.next is None:
                self.DeleteFromLast()
                return
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            temp.next = None
            temp.previous = None

    def printLinkedList(self):  # function to print the double linkec list
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


new = DoublyLinkedList()
print(new.isEmpty())
new.InsertAtTheBegining(5)
new.InsertAtTheBegining(10)
new.InsertAtTheEnd(99)
new.InsertAtTheBegining(20)
new.InsertAtTheBegining(30)
new.InsertAtTheBegining(50)
new.DeleteFromASpecificPosition(3)
new.DeleteFromBegining()
new.DeleteFromLast()

new.printLinkedList()
print()
print(new.Length())
