'''
Write a Python program to Display all the common characters between two strings.
Return -1 if there are no matching characters.

Note Ignore blank spaces if any present.
Perform Case sensitive string comparison whereever necessary.

             Sample input                                    Expected Output
            "I like Python"
        "Java is a very popular language"                        lieyon
'''

sentence1 = input("Enter String 1: \n ")
sentence2 = input("Enter String 2 \n")
word = ""

for i in sentence1:
    if i in sentence2 and i!= " ":
        word += i
print(word)