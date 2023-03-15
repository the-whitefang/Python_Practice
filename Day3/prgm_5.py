'''

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