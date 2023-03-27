'''
Write a Python function, nearest_palindrome() which accepts a number
and returns the nearest palindrome greater than the given number

        Sample Input             Sample Output
         99                         101
         1221                      1331
'''
import sys


# regular for loop
def nearest_palindrome(num):
    for i in range(num + 1, sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i


print(nearest_palindrome(1221))


def Check_prime(n):
    return True if (str(n)[::-1] == str(n)) else False


# using lambda function
check_prm = lambda n: str(n)[::-1] == str(n)
n = 99 + 1
while (not check_prm(n)):
    n += 1
print(n)
