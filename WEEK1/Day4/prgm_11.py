'''
output of the following code .
'''
class Mobile:

    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details ")

    def purchase(self):
        self.display()
        print("Calculating Price")

Mobile().purchase()
