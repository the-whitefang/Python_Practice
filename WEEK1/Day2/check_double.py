def check_double(num):
    Double = num*2
    temp = Double
    ld =0
    Len = len(str(Double))
    count1  = 0
    str1 = str(Double)
    while(temp > 0):
         ld = temp %10
         count =0
         for i in range(0,Len):
             if  str1[i]== ld:
                 count += 1
             else:
                 continue
         count1 += count
         temp /= 10
    if count1 == Len :
        print("True")
    else:
        print("False")

check_double(125874)