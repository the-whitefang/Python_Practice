'''
Linked List
'''


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __int__(self):
        self.headval = None

    def lisprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# link first node to second node
list.headval.nextval = e2

# link second node to third node
e2.nextval = e3
list.lisprint()
