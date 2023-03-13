Traveller_currency = int(input("Input the amount you have"))
Traveller_Country_Currency = input("Enter the Country currency you have")

def Currency_Calculator(Traveller_currency,Traveller_Country_Currency):
    if Traveller_Country_Currency == "Euro":
        print(Traveller_currency * 0.01417)
    elif Traveller_Country_Currency == "British Pound":
        print(Traveller_currency * 0.0100)
    elif Traveller_Country_Currency == "Australian Dollar":
        print(Traveller_currency * 0.02140)
    elif Traveller_Country_Currency == "Canadian Dollar":
        print(Traveller_currency * 0.02027)
    else:
        print("Invalid Country name")


Currency_Calculator(Traveller_currency,Traveller_Country_Currency)