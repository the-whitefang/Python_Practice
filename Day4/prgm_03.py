'''

'''

sentence1 = input("Enter String 1: \n ")
sentence2 = input("Enter String 2 \n")
word = ""

for i in sentence1:
    if i in sentence2 and i!= " ":
        word += i
print(word)