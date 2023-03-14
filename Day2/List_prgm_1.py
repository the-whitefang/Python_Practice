List_str = input("Enter a Sentence")
count = []
lt_ct = 0
d_ct = 0
for i in List_str:
    if i.isalpha():
        lt_ct = lt_ct + 1
    elif i.isdigit():
        d_ct = d_ct + 1
count.append(lt_ct)
count.append(d_ct)
print(count)