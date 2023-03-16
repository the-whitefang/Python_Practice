'''
Output of the Code
'''

class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material

s1 = Shoe(1000, "Canvas")
print("The Unique Id of the object = ",id(s1))
