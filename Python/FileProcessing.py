str1='this is a               string'

def splitfile(str1):
    str1 =str1.split('|')
    id=str1[0]
    str2=str1[1]
    list1=str2.split(' ')
    for x in list1:
        if (x.isidentifier()):
            print(id+"|"+x)



setOfFruits={'Apple','Orange','Banana'}
print("set of Fruits:",setOfFruits)
listOfFruits=list(setOfFruits)
print("listOfFruits:",listOfFruits)


":".join([str(x) for x in (1,2,3)])


#from os import listdir
#from os.path import isfile, join
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#import os

#file = [x for x in os.listdir('.') if (os.path.isfile(x))]

def myfunc(a, b):
    return a + b

x = map(myfunc(_,_), ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)


def closure_gen():
    x = 5566
    while True:
        x += 1
        yield x


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer()

# We execute the function
# Output: Hello
print_msg("Hello")


from functools import reduce



