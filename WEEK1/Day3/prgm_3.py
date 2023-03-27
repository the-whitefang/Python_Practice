'''
program to check for the stopwords from a given list of sentences
and then remove them and print the final list of sentences.
'''

sentences = ["a new world record was set",
             "in the city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with', 'was']

# using regular for loop method
result = []
for i in sentences:
    result1 = []
    for j in i.split():
        if j not in stopwords:
            result1.append(j)
    result.append(result1)
print(result)

#using List Comprehension
print([[
    j for j in i.split()
    if j not in stopwords]
    for i in sentences
])
