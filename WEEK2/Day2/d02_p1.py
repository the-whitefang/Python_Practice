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

#function to add a new value at the begining of the linked list
    def atBegining(self, newdata):
        NewNode = Node(newdata)
        # update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

#function to add a value in between 2 nodes of a linked list
    def InBetween(self,middel_node,newdata):
        if middel_node is None:
            print("The mentioned Node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middel_node.nextval
        middel_node.nextval = NewNode

#function to add a new value at the end of a linked list
    def AtEnd(self,newData):
        NewNode= Node(newData)
        if self.headval is None:
            self.headval = NewNode
            return
        laste= self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval =NewNode


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# link first node to second node
list.headval.nextval = e2

# link second node to third node
e2.nextval = e3
list.atBegining("Sun")
list.InBetween(list.headval.nextval.nextval.nextval,"Fri")
list.AtEnd("Thu")
list.lisprint()
