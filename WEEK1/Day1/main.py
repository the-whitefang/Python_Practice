a = int(input())
if a%3 ==0 and a%5 ==0:
    print("Multiple of both")
elif a%3==0:
    print("Multiple of 3")
elif a%5 ==0:
    print("Multiple of 5")
else:
    print("Invalid Input")