#categories based on functions
#based on arguments
#1: positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(1,2,3,4)
print()

#2. Kewword arguments
def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4 =20,num1=20,num3=90,num2=50)
print()

#datas are always sent from right to left in an argument
#default arguments
def function3(name,rollno,branch="CSE",clgname="GIET"):
    print(name,rollno,branch,clgname)
function3("Abhilash",182,"CSE")
function3("Ayush",147,"ECE")
function3("Tanay",190,"Nursing")
print()

def function4(*var):#tuple
    for i in var:
        print(i,end=' ')
    print()
function4(10,20)
function4(10,20,30,40)
function4(10,20,30,40,50,60)
print()

def add(*var):#tuple
    sum=0
    for i in var:
        sum = sum + i
    print(sum)

add(10,20)
add(10,20,30,40)
add(10,20,30,40,50,60)
