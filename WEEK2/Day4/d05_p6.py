'''
program to find the unknown words from a given set of known words
'''

text = input()
vocab = ["sun","in","east","doctor","day"]
unknown_words = set()
for i in text.split():
    if i not in vocab:
        unknown_words.add(i)
print(unknown_words)