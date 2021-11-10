"""
Sequences also support slicing: a[i:j] selects all items with index k such that i <= k < j. When used as an expression,
a slice is a sequence of the same type. This implies that the index set is renumbered so that it starts at 0.

(i=k)=<k<=(j=k+1)  where i is the slice starting point and is equal to index k and j is the slice ending point and is equal
to k+1.

Rules  -- Above definitiion sets the following rules for slice[Start(i): End(j) : Step]
-------
1.  "Start" describes the start value from where string has to be slice.  default is from begining.
2.  "Stop"  describes the value where we have to stop. the result will not include the stopping value.  to include the
      stop values you have to move next index thats why we mathematically represent it as   i<=k<j
3.   "Step" describe the direction and increment or decrement size.  in case of +ive its a straight and in of -ive it will
      reverse.
4.    an index will return the single element without sequence slicing notation means S[0] = A
5.    an slice notation will give output as a list , tuple or sequence  etc.   for example. S[0:1]=[]
6.    please note that start is not the lower bound and end is not always the upper bound.  they are just values whose direction
      is controlled by step.


the indexes are arranged as under:

S[Start: End: Step] so for S
-----------------------------
       0    1    2   3   4   5   6   7   8
S = '  A    B    C   D   E   F   G   H   I'
      -9   -8   -7  -6  -5  -4  -3  -2  -1

negative number are achieved as:  k-len(S).   thats why  8-9 =-1  we
Using the above formula slicing system can convert -ive start and stop value +ive values.  but it cannot change the
Step value.


"""


S = 'ABCDEFGHI'
print(len(S))
print(S[2:7])	   #CDEFG
print(S[0:7:2])	   #ACEG
print(S[0:6:2])	   #ACEG
print(S[6:0:-2])   #GEC   -ive means start is either a bigger +ive value or bigger -ive values.
print(S[6::-2])   #GECA
print(S[-7:-1:2])  # CEG    -5 -3 -2 0   k>j stop
print(S[-7::2])  # CEG    -5 -3 -2 0   k>j stop
print(S[0:7])	# ABCDEFG

print("################")
print(S[-5::-1])	# EDCBA
print(S[4::-1])	    # EDCBA

# Example of list,  how index and slice change the output.
num =[10, 20, 30]
print(num[0:1])
print(num[0])