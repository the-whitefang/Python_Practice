'''
Program to store Name of People their Age and their Gender and print
all the details of the people of the same Gender as requested by the user
'''


class Node:
    def __init__(self, person_name, age, gender):
        self.person_name = person_name
        self.age = age
        self.gender = gender


class People:
    def __init__(self):
        self.head = None

    def insert_at_end(self, person_name, age, gender):
        pass
