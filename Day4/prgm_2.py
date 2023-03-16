'''

'''


def specialty_Ward(n3):
    freq_p=0
    freq_o=0
    freq_e=0
    for i in n3:
        if i == 'P':
            freq_p += 1
        elif i =='O':
            freq_o += 1
        elif i == 'E':
            freq_e += 1
    if freq_p>freq_o and freq_p>freq_e:
        print("Pediatrics")
    elif freq_e>freq_o and freq_e>freq_p:
        print("ENT")
    elif freq_o>freq_e and freq_o>freq_p:
        print("Orthopedics")

specialty_Ward([101 ,'O', 102, 'E' ,302 ,'E' ,305, 'E'])
specialty_Ward([101,'O',102,'O',302,'P',305,'E',401,'O',656,'O'])