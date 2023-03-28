'''

'''


class Merge:

    def __init__(self, max_size1, max_size2):
        self.__max_size_1 = max_size1
        self.__max_size_2 = max_size2
        self.__max_size_3 = max_size1 + max_size2

        self.__elements1 = [None] * self.__max_size_1
        self.__elements2 = [None] * self.__max_size_2
        self.__elements3 = [None] * self.__max_size_3

        self.__rear1 = -1
        self.__front1 = 0

        self.__rear2 = -1
        self.__front2 = 0

        self.__rear3 = -1
        self.front3 = 0

    def is_full1(self):
        if self.__rear1 == self.__max_size_1 - 1:
            return True
        return False

    def is_full2(self):
        if self.__rear2 == self.__max_size_2 - 1:
            return True
        return False

    def is_empty1(self):
        if self.__front1 > self.__rear1:
            return True
        return False

    def is_empty2(self):
        if self.__front2 > self.__rear2:
            return True
        return False

    def enqueue1(self,data):
        if self.is_full1():
            print("Queue 1 is Full!!")
        else:
            self.__rear1 += 1
            self.__elements1[self.__rear1] = data

    def enqueue2(self,data1):
        if self.is_full2():
            print("Queue 2 is Full !!")
        else:
            self.__rear2 += 1
            self.__elements2[self.__rear2] = data1

    def Execute(self):
        if self.is_empty1():
            print("Queue is empty!!")


