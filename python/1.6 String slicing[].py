"""
Please note that slicing is only supported on sequence.   this is because for slicing the ordering has to be maintained
slicing can be defined as : a[i:j] selects all items with index k such that i <= k < j. When used as an expression,
a slice is a sequence of the same type. This implies that the index set is renumbered so that it starts at 0.
this is because a sequence is
S = x0, x1, x2, x3... xn.

for any sequence.   if your slice is   slice[i : k]  where k is any element by i and j   then i<=k<j
for example,   s =[0, 1,2,3,4,5]   if we want to slice from 0 to 3  the interval will be    [0 : 4]  this can be call left open internal.
k<j  is needed as this need to maintain the ordering.

(i=k)=<k<=(j=k+1)  where i is the slice starting point and is equal to index k and j is the slice ending point and is equal
to k+1.

Rules  -- Above definitiion sets the following rules for slice[Start(i): End(j) : Step]
-------.

1.  "Start" describes the start value from where string has to be slice.  default is from begining.
2.  "Stop"  describes the value where we have to stop. the result will not include the stopping value.  to include the
      stop values you have to move next index thats why we mathematically represent it as   i<=k<j
3.   "Step" describe the direction and increment or decrement size.  in case of +ive its a straight and in of -ive it will
      reverse.
4.    an index will return the single element without sequence slicing notation means S[0] = A
5.    an slice notation will give output as a list , tuple or sequence  etc.   for example. S[0:1]=[]
6.    please note that start is not the lower bound and end is not always the upper bound.  they are just values whose direction
      is controlled by step.
7.    i<=k <j means step values must be between i and j otherwise not result will be shown


the indexes are arranged as under:

S[Start: End: Step] so for S
-----------------------------
       0   1    2   3   4   5   6   7   8
S = '  A    B    C   D   E   F   G   H   I'
      -9   -8   -7  -6  -5  -4  -3  -2  -1

negative number are achieved as:  k-len(S).   thats why  8-9 =-1  we
Using the above formula slicing system can convert -ive start and stop value +ive values.  but it cannot change the
Step value.


"""

# Example of list,  how index and slice change the output.
num =[10, 20, 30]
print(num[0:1])
print(num[0])


##################
S = 'ABCDEFGHI'

print("############  default Start value is start of sequence ############")
print(S[0:7:2])	   #ACEG
print(S[:7:2])	   #ACEG

print("############  default end value is end of sequence ############")
print(S[0::2])

print("############  default step value is 1 of sequence ############")
print(S[0:6:])

print("############  default start & end value with step 2 of sequence ############")
# default start value ,  default end value but step is 2
print(S[::2])

print("############  default start & end value with step -2 of sequence ############")
print(S[::-2])

print("############  default start value is not lower bound and End value is not upper bound ############")

# here 6 to 0 is internal with step -2   means     6, 4, 2  0   since 0 is stop so 6 4 2
print(S[6:0:-2])

print("###########   right implementation        #########")

# stop is -2 so -1 means
print(S[6:-10:-2])  #GECA

# instead use default start of string notation
# here -2 is converted to 7
print(S[6::-2])     #GECA

print("")
print(S[-7:-1:2])  # CEG     between i and j   -7 =< [-7 -5. -3. ] <-1
print(S[-7::2])  # CEG    -5 -3 -2 0   k>j stop

print("###### -k + leng(s)##########")
print(S[-5::-1])	# EDCBA
print(S[4::-1])	    # EDCBA
