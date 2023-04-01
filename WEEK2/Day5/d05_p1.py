'''
Program to find the Odd and Even numbers form a given list and
store and print the odd numbers in Odd Queue and the Even numbers
in Even Queue.
'''


class Odd_Queue:

    def __init__(self, max_size):

        self.max_size = max_size
        self.elements = [None] * self.max_size
        self.rear = -1
        self.front = 0

    def isfull(self):
        if self.rear == self.max_size - 1:
            return True
        return False

    def isEmpty(self):
        if self.front > self.rear or self.rear == -1:
            return True
        return False

    def enqueue(self, data):
        if self.isfull():
            print("Odd Queue is full")
        else:
            self.rear += 1
            self.elements[self.rear] = data

    def display_odd(self):
        for i in range(self.front, self.rear + 1):
            print("Odd Queue: ",self.elements[i],end="->")


class Even_Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = [None] * self.max_size
        self.rear = -1
        self.front = 0

    def isFull(self):
        if self.rear == self.max_size - 1:
            return True
        return False

    def isEmpty(self):
        if self.front > self.rear or self.rear == -1:
            return True
        return False

    def enqueue(self, data1):
        if self.isFull():
            print("Even Queue is full: ")
        else:
            self.rear += 1
            self.elements[self.rear] = data1

    def display_odd(self):
        for i in range(self.front, self.rear + 1):
            print("Even Queue: ",self.elements[i],end="->")


num = [2, 7, 9, 4, 6, 5, 10]
obj = Odd_Queue(10)
obj1 = Even_Queue(10)
for i in num:
    if i % 2 == 0:
        obj1.enqueue(i)
    else:
        obj.enqueue(i)
