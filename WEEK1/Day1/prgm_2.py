#Currency Calculator
Traveller_currency = int(input("Input the amount you have"))
Traveller_Country_Currency = input("Enter the Country currency you have")

def Currency_Calculator(Traveller_currency,Traveller_Country_Currency):
    if Traveller_Country_Currency == "Euro":
        print(round((Traveller_currency / 0.01417),2))
    elif Traveller_Country_Currency == "British Pound":
        print(round((Traveller_currency / 0.0100),2))
    elif Traveller_Country_Currency == "Australian Dollar":
        print(round((Traveller_currency / 0.02140),2))
    elif Traveller_Country_Currency == "Canadian Dollar":
        print(round((Traveller_currency / 0.02027),2))
    else:
        print("Invalid Country name")


Currency_Calculator(Traveller_currency,Traveller_Country_Currency)



#Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveler has. The program should identify and display the amount the traveler should provide in the currency he has, to get the specified amount in INR.

#Note: Use the forex information provided in the table below for the calculation. Consider that only the currency names mentioned in the table are valid.


