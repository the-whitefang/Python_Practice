'''program to enter a string and print concatenated form of first two chracters and the last two characters if
 length is greater than 2, if length == 2 then print new string with same characters twice and
 if length < 2 print -1
 Sample Input: w3resource     Expected output:  w3ce
 Sample Input: w3             Expected output: w3w3
 Sample Input: A              Expected output:  -1
 '''
def Characters(str):
    Len = len(str)
    if Len < 2:
        print(-1)
    elif Len ==2:
        str1 = str+str
        print(str1)
    elif Len > 2:
        str2 = str[0]+str[1]+str[Len-2]+str[Len-1]
        print(str2)

Characters("w3")