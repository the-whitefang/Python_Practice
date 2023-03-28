'''
**Linked List**

Linked List is a collection of 'nodes'
A Single Linked list can traverse only in one direction.
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

    def atBegining(self,newdata):
        NewNode = Node(newdata)
        #update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# link first node to second node
list.headval.nextval = e2

# link second node to third node
e2.nextval = e3
list.atBegining("Sun")
list.lisprint()