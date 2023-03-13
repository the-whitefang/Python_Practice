Adult_Passengers = int(input("Enter the number of Adults: \n"))
Child_Passengers = int(input("Enter the number of Children: \n"))
print((((Adult_Passengers*37550.0)+(Child_Passengers*37550.0/3))*1.07)*0.90)

'''total = ((Adult_Passengers*37750.0)+ (Child_Passengers*37550.0/3))
print(total)
total1 = total*0.07
total2 = total1+total
print("with service tax ",total2)
total_amount = total2*0.90
print(total_amount)'''