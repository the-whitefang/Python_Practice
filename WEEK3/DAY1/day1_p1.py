class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def lisprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval,end="->")
            printval = printval.nextval

    # function to add a new value at the end of a linked list
    def AtEnd(self, newData):
        NewNode = Node(newData)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode




list = SLinkedList()
list.AtEnd(1)
list.AtEnd(2)
list.AtEnd(3)
list.AtEnd(4)
list.AtEnd(5)
list.AtEnd(8)
list.AtEnd(7)
list.AtEnd(6)
# list.headval = Node("1")
# e2 = Node("2")
# e3 = Node("3")
# e4 = Node("4")
# e5 = Node("5")
# e6 = Node("8")
# e7 = Node("7")
# e8 = Node("6")
#
# list.headval.nextval = e2
# e2.nextval = e3
# e3.nextval = e4
# e4.nextval = e5
# e5.nextval = e6
# e6.nextval = e7
# e7.nextval = e8
# e8.nextval = e3


list.lisprint()




#######################################################################


# class Node:
#     def _init_(self, data, next=None):
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def _init_(self):
#         self.head = None
#
#     def insertAtBeginning(self, data):
#         # we will create a node
#         node = Node(data)
#         if (self.head == None):
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#         return node
#
#     def printList(self):
#         copy = self.head
#         while copy is not None:
#             print(copy.data, end='->')
#             copy = copy.next
#
#     def InsertAtEnd(self, ref):
#         copy = self.head
#         while copy.next is not None:
#             copy = copy.next
#         copy.next = ref
#
#     def FindCyclePresentOrNot(self):
#         ptr1 = self.head
#         ptr2 = self.head
#
#         while ptr2.next.next is not None:
#             ptr2 = ptr2.next.next
#             ptr1 = ptr1.next
#             if (ptr2 == ptr1):
#                 print("Cycle found at", ptr1.data)
#                 return ptr1
#         return None
#
#     def findMeetingPoint(self, ptr):
#         if (ptr == None):
#             print("No cycle Found!")
#             return
#         start = self.head
#         while start != ptr:
#             ptr = ptr.next
#             start = start.next
#         print("Cycle started At", ptr.data)
#
#     def removeCycle(self, ptr):
#         if (ptr == None):
#             print("No cycle Found!")
#             return
#         start = self.head
#         while start.next != ptr.next:
#             ptr = ptr.next
#             start = start.next
#         ptr.next = None
#         print("Cycle Removed!")
#
#
# x = LinkedList()
# x.insertAtBeginning(6)
# x.insertAtBeginning(7)
# x.insertAtBeginning(8)
# x.insertAtBeginning(5)
# x.insertAtBeginning(4)
#
# copyNode = x.insertAtBeginning(3)
#
# x.insertAtBeginning(2)
# x.insertAtBeginning(1)
#
# x.InsertAtEnd(copyNode)
# # x.printList()
# ptr = x.FindCyclePresentOrNot()
# x.findMeetingPoint(ptr)
# print()
# x.removeCycle(ptr)
# print()
# x.printList()
