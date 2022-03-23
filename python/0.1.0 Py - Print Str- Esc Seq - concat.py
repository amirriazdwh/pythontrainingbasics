# is comments in python

"""
-----------------------------------------------
concatenation  in Python using +
-----------------------------------------------

Method 1
----------
s = "String"  " Concatenation"
print(s)

s = 'String'  \
' Concatenation'
print(s)

Method 2
------------
name ="Python"
. Function Style:  "Hello" +name+  "!" .    + is the way concatenation is achieved in python

Method 3
------------
s = 'String'
s += ' Concatenation'
print(s)

Method 4
------------
s1 = 'String'
s2 = 'Concatenation'

s3 = ''.join([s1, s2])
print(s3)

Method 5.
------------
s1, s2, s3 = 'Python', 'String', 'Concatenation'
s = ','.join([s1, s2, s3])
print(s)

Method 6.
------------
s1, s2, s3 = 'Python', 'String', 'Concatenation'
s = '{} {} {}'.format(s1, s2, s3)
print(s)

Method 7.
-----------
s1, s2, s3 = 'Python', 'String', 'Concatenation'
s = f'{s1} {s2} {s3}'
print(s)

-------------------------------------------------
String formatting method in python.
-------------------------------------------------
1. Old style: "Hello %s" %name   - % means replace the latter after s with name variable.   in case of multiple variable
   you can use "Hello Mr %s with %s "%(Firstname, LastName).  s means string.  other formats are specified below.
2. New Style:.   "Hello, {}".format(name)
   Hello {name},  there is a 0x{errorno:x} error!. format(name=name, errorno=errno)
   in case you decided to give position  like {0}, {1} it should always start from 0
3. Literal String interpolation:   f'Hello {name}'.  this is actually a sugar coat version of 'Hello {name}'.format(name)
   here f is equivalent to format function and variable is inside {name}

5. Template Strings:  "Hey, $name!"
     from string import Template
     t=Template('Hey, $name!')
     t.substitute(name=name)

"""


"""
d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Obsolete and equivalent to 'd', i.e. signed integer decimal.
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.
---------
#	Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
0	The conversion result will be zero padded for numeric values.
-	The converted value is left adjusted
 	If no sign (minus sign e.g.) is going to be written, a blank space is inserted before the value.
+	A sign character ("+" or "-") will precede the conversion (overrides a "space" flag).
"""
"""
in case of print statement
d means digits...   2d say digit will have 2 digits
f means fraction... 5.3f says fraction will have 5 digits and 3 will be fraction part and 2 will be digits parts
% means replace values by order.  if %2d and %3d and values are 23 and 25.  then they will be printed in order
"""


# print method argument are of type *argu,  so multiple values can be given as tuple
print("this is first line", "this is second line")

# print(self, *args, sep=' ', end='\n', file=None):
#
# multiple variable example
q=458
p=0.586
print(q, p, p * q, sep=",")

print("this", "is", "the", "line of code ", sep=" ", end="\n\n")

# by default the end character is new line
print("this is the line of code ", end=" ")
print(" this is second line ")

"""
----------------------------------------
Method #1
----------------------------------------
"""

print("Geeks : % 2d, Portal : % 5.1f" %(1, 05.333))
print("\n")
# escape sequence are \n \r
# edit format is : %[flags]5[width]3[.precision]ftype  example,  so its %5.3d
print("c:\\narry")
print("Total students : % 3d, Boys : % 2d" %(240, 120))
print("% 7.3o"% (25))
print("% 10.3E"% (356.08977))


"""
----------------------------------------
Method #2
----------------------------------------
"""
# note here the first argument will always start from 0
print("First argument: {0}, second one: {1}".format(47,11))
# 0 is first position and 1 is the second position and : gives precision,  you can specify position  position:flag:type.
print("Second argument: {1:3d}, first one: {0:7d}".format(47,11))


"""
----------------------------------------
Method #3
----------------------------------------
"""
print(f"Second argument: {q}, first one: {p}, product  {p*q}")

"""
----------------------------------------
Method #5
----------------------------------------
"""


from string import Template
name="Amir"
t=Template('Hey, $name!')
str0=t.substitute(name=name)
print(str0)

"""
Note:  this will not work in python
"""
print("My name is $name")

