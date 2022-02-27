lk=(1,2,3,4,5,6)

a,* b, c =lk

print(id(b))

"""
How args works.   args use python slicing technique to position the assignment.    Note in above assignment python uses postive and negative index by position.  
for example position of a is 0 while position of c is -1.   so to get the value of b the poistion should be from 1 to -2
"""
b = lk[1:-2]
print(b)
"""
which means *b instructs python to get the index from tuple or list from postion end and from end in negative count.   extract value of tuple by slicing and then insert into tuples
value of a and b are also assigned in same way.   here a=lk[0]   and c=lk[-1].   please note the *b  means list , tuple , set  or any data type dervied from sequence.  thats why its 
been extract by b = lk[1:-2] as [sindex: stopindex: step] return tuple or list or set.   however,   since a and c are not marked as sequence data types they are extract as 
a=lk[0]

there can by only one *b in a tuple.    * denote data type and extraction by position
"""
a=lk[0]
print(a)
#1

c=lk[-1]
print(c)
#6

"""
same logic is being applied during parameter packing.  here c is packing the parameters.  here no list or tuple exist in function parameter.   however, the position of parameters are 
well know.  so paction is being done based on poistional parameters
"""

def tupletype (a, b, *c):
    print(c)

tupletype(1,2,3,4,5,6)

ls =(1,2,3,4)
def tupetype2(a,b,c,d):
    print(a,b,c,d)

tupetype2(*ls)

"""
 if we take the ls =(1,2,3,4,5)
 TypeError: tupetype2() takes 4 positional arguments but 5 were given.  which is another proof the assignment is done based on position.  in case of extraction the number of variable in
 list must be same as number of arguments in function
"""