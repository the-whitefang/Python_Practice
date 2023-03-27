'''
Queue(linear data structure)
It is a double ended data structure.
It uses First IN First Out(FIFO)
Typical operstions in Queue:
    1. isempty()-> determines the queue is empty
    2. isfull()-> determines if the queue is full in case of a bounded size queue
    3. front-> returns the element at front of the queue
    4. enqueue-> inserts an element at the rear
    5. dequeue-> delete an element from the front
'''

class Queue:

    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear == self.__max_size-1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue is Full!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data


    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size


q=Queue(4)
print("Is it full",q.is_full())
print("Is it empty",q.is_empty())
q.enqueue(100)
q.display()
q.enqueue(200)
q.enqueue(300)
q.enqueue(400)
q.display()
q.enqueue(500)
q.display()
print("Element deleted",q.dequeue())
q.display()

