'''
program to take a list of marks of 10 students and
(1) find the average of their marks and find how many students have scored more than the average marks
(2) find how many students have scored the same marks for example, how many have scored 0, how many have scored
1...,how many have scored 25
(3) sort the marks in increasing order from 0 to 25
'''

def find_more_than_average(list_Marks):#to find the percentage of students who have marks more than average
    avg = sum(list_Marks)/ len(list_Marks)
    c =0
    for i in list_Marks:
        if i>avg:
            c += 1
    percentage = ((c/len(list_Marks))*100.0)
    print(percentage)

def generate_Frequency(list_Marks):
    freq_List = []

    for i in range(0,26):
        ctr = 0
        for j in list_Marks:
            if j == i:
                ctr += 1
        freq_List.append(ctr)
    print(freq_List)

def sort_Marks(list_Marks):
    list_Marks1 = list(list_Marks)
    list_Marks1  = sorted(list_Marks)
    print(list_Marks1)


list_Marks = (12,18,25,24,2,5,18,20,20,21)
find_more_than_average(list_Marks)
generate_Frequency(list_Marks)
sort_Marks(list_Marks)








