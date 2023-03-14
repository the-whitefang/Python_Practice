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
    print(count)

frequency("Ifosys 123")
frequency("ABCDEFG")