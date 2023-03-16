'''
String rotation
Input: rhdt:246, ghftd:1246
1 -> if sum of the square of the digits is even then rotate the string by 1.
2 -> if sum of the squares of the digits is odd then rotate the string left by 2 position

'''

s = input().split(",")
stt = []
num = []
for i in s:
    s1,n =i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(ss,n):
    n = str(n)
    s =0
    for i in n:
        s += int(i)**2
    if s%2  == 0:
        return ss[-1]+ss[:1]
    else:
        return ss[2:]+ ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))