x = int(input("Enter the number of 1Rs coin you have: \n"))
y = int(input("Enter the number of 5Rs coin you have: \n"))
z = int(input("Enter the Amount to be made: \n"))
def Product(one,five,amt_made):
    req = 0
    if (five * 5 ) <= amt_made and abs((five * 5) - amt_made) <= one:
        print("1Rs coins needed = ",abs((five * 5) - amt_made))
        print("5Rs coins needed = ",five)
    else:
        print(-1)


Product(x,y,z)

