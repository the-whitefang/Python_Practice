class Node: # Node Class to create a node in a single linked list that stores the seat type, number of reserved seats and total number of seats.
    def __init__(self, seat_type, reserved, capacity):
        self.seat_type = seat_type
        self.reserved = reserved
        self.capacity = capacity
        self.next = None


class Compartment: # Compartment Class to create the linked list that stores the nodes of the train compartment.

    def __init__(self):
        self.head = None

    def insert_at_end(self, seat_type, reserved, capacity): # function to add the datas at the specific nodes
        newnode = Node(seat_type, reserved, capacity)
        if self.head is None:
            self.head = newnode
            return
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = newnode


class Train:
    def __init__(self, train_name, compartment_list):
        self.train_name = train_name
        self.compartment_list = compartment_list

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        if self.compartment_list is None:
            print("List is Empty")
        else:
            a = self.compartment_list
            while a is not None:
                print(a.seat_type, a.reserved, a.capacity)
                a = a.next

    def count_compartments(self):
        if self.compartment_list is None:
            print("There are 0 compartments present in the list")
        else:
            a = self.compartment_list
            ctr = 0
            while a:
                ctr += 1
                a = a.next
            return ctr

    def check_vacancy(self):
        if self.compartment_list is None:
            print("List is Empty")
        else:
            a = self.compartment_list
            ctr = 0
            while a is not None:
                if a.reserved < a.capacity * 0.5:
                    ctr += 1
                a = a.next
            print("Vacancy =", ctr)


new = Compartment()
new.insert_at_end("SL", 250, 100)
new.insert_at_end("2AC", 125, 280)
new.insert_at_end("3AC", 120, 300)
new.insert_at_end("FC", 160, 300)
new.insert_at_end("1AC", 100, 210)

train = Train("Dhanbaad Allepy \n", new.head)

print("Name of the Train is :", train.get_train_name())
train.get_compartment_list()
print("\nThere are ", train.count_compartments(), "no. of compartments")

train.check_vacancy()
