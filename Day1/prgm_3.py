Adult_Passengers = int(input("Enter the number of Adults: \n"))
Child_Passengers = int(input("Enter the number of Children: \n"))
total = ((Adult_Passengers*37750.0)+ (Child_Passengers*37550.0*0.03))
print(total)
total1 = total*0.07
total2 = total1+total
print("with service tax ",total2)
total_amount = total2*0.90
print(total_amount)