# is comments in python
"""
for muliple line comments we use 3 quotations
this is multiline comments
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

q=458
p=0.586
print(q, p, p * q, sep=",")

print("this is first line", "this is second line")

# by default the end character is new line
print("this is the line of code ", end=" ")
print(" this is second line ")
"""
in case of print statement
d means digits...   2d say digit will have 2 digits
f means fraction... 5.3f says fraction will have five digits and 3 will be fraction part and 2 will be digits parts
% means replace values by order.  if %2d and %3d and values are 23 and 25.  then they will be printed in order
"""
print("Geeks : % 2d, Portal : % 5.1f" %(1, 05.333))
print("\n")
# escape sequence are \n \r
#    %[flags][width][.precision]type
print("c:\\narry")
print("Total students : % 3d, Boys : % 2d" %(240, 120))
print("% 7.3o"% (25))
print("% 10.3E"% (356.08977))

print("First argument: {0}, second one: {1}".format(47,11))
# 0 is first position and 1 is the second position and : gives precision
print("Second argument: {1:3d}, first one: {0:7d}".format(47,11))

