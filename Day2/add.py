'''
program to input a string and add ing at the end of a string, if ing already present then add less ly,
and if lenght < 3 leave it like that
'''
def Characters(str):
    Len = len(str)
    if Len < 3:
        print(str)
    elif str[-3:] == "ing":
        print(str+"ly")
    else:
        print(str+"ing")
Characters("amazing")