'''

'''


class Evenly_divisible:

    def __int__(self, max_size):

        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__elements2 = [None] * self.__max_size

        self.__rear = -1
        self.__front = 0

        self.__rear1 = -1
        self.__front1 = 0

    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def execute(self, data):
        for i in range(self.__elements, self.__elements + 1):
            ctr = 0
            for i in range(1, 6):
                if self.__elements[i] % i == 0:
                    ctr += 1
            if ctr == 6:
                self.__elements2[self.__rear1] = self.__elements[i]

    def display(self):
        for index in range(self.__front1, self.__rear1):
            print(self.__elements2[index])


q = Evenly_divisible(5)
q.enqueue(13983)
q.enqueue(10080)
q.enqueue(7113)
q.enqueue(2520)
q.enqueue(2500)
q.display()
