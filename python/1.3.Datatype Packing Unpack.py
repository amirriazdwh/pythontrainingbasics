# theory,  *args converts to args[0], args[1]..
# the indexes values is taken from list, tuple and set run time. in short * is
#for i in list :
#    args[i] =list[i]
################################
# Examples
###############################
def fun(a, b, c, d):
    print(a, b, c, d)
tuple
# Driver Code
my_list = [1, 2, 3, 4]
# here at run time the actual values passed are :
# fun(args[0], args[1],args[3],args[4])
# *my_list is means tuples or sequence is passed as arguments,  **my_list means dictory is passed
fun(*my_list)

# A Python program to demonstrate use
# of packing

# This function uses packing to sum
# unknown number of arguments
# the same things is being done by parameter level.
# the below call is translated as :
# def mySum(args[0], args[1],args[2],args[4]) of tuple types
# since mySum(1,2,3,4,5) the tuple is (1,2,3,4,5)
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


# A Python program to demonstrate both packing and
# unpacking.

# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)

# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
#   in case of *args are tuples ('Hello', 'beautiful', 'world!')
    print(args)
    print(type(args))
    # Convert args tuple to a list so we can modify it
    args = list(args)

    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'

# UNPACKING args and calling fun1()
    fun1(*args)

# Driver code
fun2('Hello', 'beautiful', 'world!')


##################
# swap values
##################
a=2
b=3

a,b =b, a

print(a)
print(b)

#########
# use of _ in unpacking,  its similar to scala
##########

test =(1,2000,3)
_, x, _ =test
print(x)
##########################################
# unpacking arbiltary number of tuples
###########################################
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

#from collections import deque
#def search(lines, pattern, history=5):
#    previous_lines = deque(maxlen=history)
#    for line in lines:
#        if pattern in line:
#            yield line, previous_lines
#        previous_lines.append(line)

# Example use on a file
#if __name__ == '__main__':
#    with open('somefile.txt') as f:
#        for line, prevlines in search(f, 'python', 5):
#            for pline in prevlines:
#                print(pline, end='')
#        print(line, end='')
#        print('-'*20)

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}


rows= [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)