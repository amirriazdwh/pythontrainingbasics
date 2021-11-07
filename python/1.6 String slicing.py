"""
Sequences also support slicing: a[i:j] selects all items with index k such that i <= k < j. When used as an expression,
a slice is a sequence of the same type. This implies that the index set is renumbered so that it starts at 0.

you can find the slice of string by following formula
if k is the index of the array then index slice for that element will be

(i=k)=<k<=(j=k+1)  where i is the slice starting point and j is the slice ending point.  k is array index.  so if we want
to get array for 0 to 6.    the starting slice is lower bound and ending slice is upper bound.
i=0 and j=6+1=7 so

Some sequences also support “extended slicing” with a third “step” parameter: a[i:j:k] selects all items of a with index x
where x = i + n*k, n >= 0 and i <= x < j

in case k is index between 0 and 6 and we want slice array from 0 to 7  i=0 , n=2 and j=7
0<=0<1   0+2=2       i+n=x ( next x)  A
2<=2<3   2+2=4                        C
4<=4<5                                E
6<=6<7                                G
            +
in case index k is from 6 to 0 (k) and n =-2   a[6:0:2]

6    6<=6<7     G    k-n  6-2=k
4    4<=4<5     E         4-2=k
2    2<=2<3     C         2-2=k
0    0<=0<1     A
-----------------------------------
in case the k is from -1 to -6

"""


S = 'ABCDEFGHI'
print(S[2:7])	   #CDEFG
print(S[0:7:2])	   #ACEG
print(S[6:0:-2])   #GEC
print(S[-7:-2:2])  # CEG

print(S[0:7])	# CDEFG


print(S[0:1])	# CDEFG  0=<0<1

print(S[1])