'''

'''
class Stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if self.__top==self.__max_size-1:
            return True
        return False

    def is_empty(self):
        if self.__top==-1:
            return True
        return False

    def push(self,data):
        if self.is_full():
            print("The Stack is full!!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if self.is_empty():
            print("The Stack is Empty!!")
        else:
            data =self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if self.is_empty():
            print("The Stack is empty!!")
        else:
            index=self.__top
            while index>=0:
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size


ball_stack = Stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of the Stack",ball_stack.get_max_size())
print("The element deleted",ball_stack.pop())
print("After deleteing the element")
ball_stack.display()
print("Size of the Stack",ball_stack.get_max_size())
