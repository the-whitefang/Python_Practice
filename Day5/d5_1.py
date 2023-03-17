'''

'''
class Vehicles:
    def __init__(self,vehicle_id,vehicle_type,vehicle_cost):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__vehicle_cost = vehicle_cost
        self.__premium_amount =None


    def setter_Id(self,vehicle):
        self.__vehicle_id = vehicle

    def setter_Type(self,vehicle_type):
        self.__vehicle_type = vehicle_type

    def setter_Cost(self,vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def setter_Premium_Amount(self,premium_amount):
        self.__premium_amount = premium_amount

    def getter_Id(self):
        print("Vehicle Id : ",self.__vehicle_id)
        return self.__vehicle_id

    def getter_Type(self):
        print("Vehicle Type: ",self.__vehicle_type)
        return self.__vehicle_type
    def getter_Cost(self):
        print("Vehicle Cost: ",self.__vehicle_cost)
        return self.__vehicle_cost

    def getter_Premium_Amount(self):
        print("Vehicle Premium Amount: ",self.__premium_amount)
        return self.__premium_amount
    def setter_Premium_Amount(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = (2/100.0) * self.__vehicle_cost
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = (6/100.0) * self.__vehicle_cost


c1 = Vehicles(155,"Two Wheeler",50000)
c1.setter_Premium_Amount()
c1.getter_Id()
c1.getter_Type()
c1.getter_Cost()
c1.getter_Premium_Amount()


