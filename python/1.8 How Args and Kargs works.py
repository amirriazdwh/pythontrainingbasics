lk=(1,2,3,4,5,6)

a,* b, c =lk

print(id(b))

"""
How args works.   args use python slicing technique to position the assignment.    Note in above assignment python uses 
postive and negative index by position.  
for example position of a is 0 while position of c is -1.   so to get the value of b the poistion should be 
from 1 to -1
"""
lk = (1, 2, 3, 4, 5, 6)
a, *b, c = lk

# Equivalent slicing
a = lk[0]      # 1
b = lk[1:-1]   # [2, 3, 4, 5]
c = lk[-1]     # 6

print("a:", a)  # Output: 1
print("b:", b)  # Output: [2, 3, 4, 5]
print("c:", c)  # Output: 6

"""
*b indicate the interpreter that its a sequence which is a based type of tuple so slice can be performed to extract values
The *b syntax in tuple unpacking tells the interpreter that b should capture all the remaining elements in the sequence,
allowing it to be treated as a list. This is why slicing can be performed on b

which means *b instructs python interpreter to get the index from tuple or list from postion end and from end in negative count.  
extract value of tuple by slicing and then insert into tuples

value of a and b are also assigned in same way.   here a=lk[0]   and c=lk[-1].   please note the *b  means list , 
tuple , set  or any data type dervied from sequence.  thats why its 
been extract by b = lk[1:-1] as [sindex: stopindex: step] return tuple or list or set.   however,   
since a and c are not marked as sequence data types they are extract as a=lk[0]

there can by only one *b in a tuple.    * denote sequence data type and therefore extraction by position
"""
a=lk[0]
print(a)
#1

c=lk[-1]
print(c)
#6

"""
same logic is being applied during parameter packing.  here c is packing the parameters.  here no list or tuple exist 
in function parameter.   however, the position of parameters are well know.  
so compaction is being done based on position parameters
"""

def tupletype (a, b, *c):
    print(c)

tupletype(1,2,3,4,5,6)

ls =(1,2,3,4)
def unpack(a,b,c,d):
    print(a,b,c,d)

unpack(*ls)

"""
 if we take the ls =(1,2,3,4,5)
 TypeError: tupetype2() takes 4 positional arguments but 5 were given.  which is another proof the assignment is done
  based on position.  in case of extraction the number of variable in
 list must be same as number of arguments in function
"""

"""
* means tuple.  so function will receive a variable of type tuple.  however,  its been passed value of type int. 
  
"""
def pack(*args):
    print(type(args))
    print(len(args))
    print(args)

pack(1,2,3,4,5)