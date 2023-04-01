'''

'''


class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class List1:

    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end="-> ")
            printval = printval.nextval

    def InBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def insert_at_index(self,index):
        pass

class List2:

    def __init__(self):
        self.headval = None

    def listPrint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end ="->")
            printval = printval.nextval

    def atBegining(self, newdata):
        New_Node = Node(newdata)
        New_Node.nextval = self.headval
        self.headval = New_Node




new = List1()
new.headval = Node(1)
e2 = Node(2)
e3 = Node(4)
e4 = Node(3)
e5 = Node(5)
new.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
new.listprint()

print()

obj = List2()
obj.headval = Node(9)
a2 = Node(8)
a3 = Node(11)
obj.headval.nextval = a2
a2.nextval = a3
obj.listPrint()
print()

n = int(input("Enter the Position"))
new.insert_at_index(n)