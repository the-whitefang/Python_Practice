class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref =None

new =LinkedList()
new.insert_at_end(5)
new.insert_at_end(10)
new.insert_at_end(15)
new.insert_at_end(20)
new.insert_at_end(25)
new.traverse_list()
new.delete_at_start()
print("After deletion at the begining")
new.traverse_list()
new.delete_at_end()
print("After deletion at the end")
new.traverse_list()
