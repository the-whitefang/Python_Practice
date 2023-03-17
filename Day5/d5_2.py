'''

'''
class Students:
    def __init__(self,id,age,marks,fees):
        self.__student_id = id
        self.__student_age = age
        self.__student_marks = marks
        self.__studen_fees = fees

    def setter_Id(self,Id):
        self.__student_id = Id

    def setter_Age(self,age):
        self.__student_age = age

    def setter_Marks(self,marks):
        self.__student_marks = marks

    """def setter_Fees(self,fees):
        self.__student_fees = fees"""

    def Validate_Age(self):
        if self.__student_age > 20:
            return True
        else:
            return False

    def Validate_Marks(self):
        if self.__student_marks >= 0 and self.__student_marks<=100:
            return True
        else:
            return False

    def Qualification(self):
        if self.Validate_Marks() and self.Validate_Age():
            if self.__student_marks >= 65:
                print(self.Discount())
                return "Elligible"
            else:
                return "Not Elligible"
        else:
            return "Not Elligible"

    def Discount(self):
        if self.__student_marks > 85:

            return self.__studen_fees-((25/100.0)*self.__studen_fees)
        else:
            return "No Discount"

    def getter_Id(self):
        print("Student Id: ",self.__student_id)
        return self.__student_id

    def getter_Age(self):
        print("Student Age: ",self.__student_age)
        return self.__student_age

    def getter_Marks(self):
        print("Student Marks: ",self.__student_marks)
        return self.__student_marks

    def getter_Fees(self):
        print("Student Fees: ",self.__studen_fees)
        return self.__studen_fees

obj = Students(311,22,88,10000)
#obj.Validate_Age()
#obj.Validate_Marks()
obj.getter_Id()
obj.getter_Age()
obj.getter_Marks()
print(obj.Qualification())
#obj.Discount()
