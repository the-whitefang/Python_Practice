#program to count the frequency of letters and digits using built in methods
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
#program to count the frequency of letters and digits without using built in methods
def frequency(Str):
    count = []
    letter_freq = 0
    digit_freq = 0
    for i in Str:
        if ord(i) >= 65 and ord(i) <= 90 and ord(i) >= 97 and ord(i) <= 122:
            letter_freq = letter_freq + 1
        elif ord(i) >=48 and ord(i) <= 57:
            digit_freq = digit_freq + 1
        else:
            continue
    count.append(letter_freq)
    count.append(digit_freq)
    return count

frequency("Ifosys 123")
frequency("ABCDEFG")