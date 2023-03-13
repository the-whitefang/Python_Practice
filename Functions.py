#Functions
def functions():
    print("Its a function")
functions()

def functions2(num1,num2):
    print("num1",num1,"num2",num2)
functions2(10,20)

#print()_str_ => magical object to convert everything to string and pass the vlue as parameter

def functions3(num1,num2):
    num3 = num1 + num2
    return num3
print("Number returned = ",functions3(10,20.5),end=' ')
print()

def functions4(num1,num2):
    num3 = float(num1) + num2
    return num3
print("Number returned = ",functions4('10',20.5),end=' ')
print()

def functions5(num1,num2):
    num3 = num1 + str(num2)
    return num3
print("Number returned = ",functions5('10',20.5),end=' ')
print()