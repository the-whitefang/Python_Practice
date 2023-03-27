'''
Given a number n, write a program to find the sum of the largest prime factors of each of
nine cosecutive numbers starting from n.
g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8)
where, g(n) is the sum and f(n) is the largest prime factor of n
For example,
g(10) = f(10) + f(11) +f(12) + f(13) + f(14) + f(15) + f(16) + f(17) + f(18)
      = 5 + 11 + 3 + 13 + 7 + 5 + 2 + 17 + 3
      = 66
'''




def Check_Largest_Prime_Factor(n):#10
    Factor_list = []
    for i in range(1,n+1):#1 2 3 4 5 6 7 8 9 10
        if n%i == 0:
            Factor_list.append(i)
    Factor_list.sort()
    Largest_factor = Factor_list[-1]
    flag = 0
    for i in range(1,Largest_factor+1):
        if Largest_factor%i==0:
            flag += 1
    if flag == 2:
        return Largest_factor


def main():
    n = int(input("Enter any number: \n"))#10
    sum =0
    for i in range(n,n+19):#10 11 12 13 14 15 16 17 18
        sum = sum + Check_Largest_Prime_Factor(n)#10
    print("Sum of the Largest Prime Factors: ", sum)


main()