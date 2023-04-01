'''
from a given linked list find the maximum mumber
and replace it with a new one.
'''


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class maximum_replacement:

    def __init__(self):
        self.headval = None

    def printLink(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end="->")
            printval = printval.nextval

    def insert_at_begining(self, newdata):
        newnode = Node(newdata)
        newnode.nextval = self.headval
        self.headval = newnode

    def max_num(self,newval):
        if self.headval is None:
            return None

        current = self.headval
        max_val = current.dataval
        max_node = current
        prev_node = None

        while current is not None:
            if current.dataval > max_val:
                max_val = current.dataval
                max_node = current
                prev_node = prev
            prev = current
            current = current.nextval
        max_node.dataval = newval


obj = maximum_replacement()
obj.headval = Node(10)
a1 = Node(28)
a2 = Node(39)
a3 = Node(99)
a4 = Node(100)
a5 = Node(150)
obj.headval.nextval = a1
a1.nextval = a2
a2.nextval = a3
a3.nextval = a4
a4.nextval = a5

print(" Before Replacement: ")
obj.printLink()

obj.max_num(250)
print("\n After Replacement: ")
obj.printLink()




