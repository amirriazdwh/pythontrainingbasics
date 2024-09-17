"""
 Strings Pattern

1. String format:
print (f"this is stirng with {value:2d}")

2. Quotes:
Single: 'Single quotes'
Double: "Double quotes"
Escape Quotes: \' or \"

3.String Creation:
Single Line: 'Text' or "Text"
Multi-line: '''Text''' or double qoute
variable assess through $ will not work:  "this is variable $var"

4.Concatenation Patterns
Adjacent Strings with single space:
s = "Part1" "Part2"   --  automaticall adds join method.   "Part1".join"Part2"

+ Operator:
s = "Part1" + "Part2"

+= Operator:
s = "Part1"
s += " Part2"

join() Method:
s = ''.join([s1, s2])

join() with Separator:
s = ','.join([s1, s2, s3])

5. format() Method:
s = '{} {} {}'.format(var1, var2, var3)
var1 is replaced with first {} and so on
first {} is actually {0} so replaced with var1 in tuple


f-strings:
s = f'{var1} {var2} {var3}'
its another way to represent format Method.


6. format() Method:
print("Text {}".format(value))
{0} for position

7. f-strings:
print(f"Text {value}")

8.Template Strings:
from string import Template
t = Template('Text $variable')
t.substitute(variable=value)
Print Method Patterns
Basic Print:

print("Text1", "Text2")
sep and end Parameters:

print(value1, value2, sep=",")
print("Text", end=" ")
print("Next Line")
"""

"""
9 digit, number, string space format

1. Signed Integer Decimal (d)
value = 5
print(f"{value:2d}")  # Ensures the integer has at least 2 digits
# Output: " 5"

2. Unsigned Octal (o)
value = 8
print(f"{value:o}")  # Converts the integer to octal
# Output: "10"


3. Unsigned Hexadecimal (x and X)
value = 255
print(f"{value:x}")  # Lowercase hexadecimal
# Output: "ff"
print(f"{value:X}")  # Uppercase hexadecimal
# Output: "FF"

4. Floating Point Exponential Format (e and E)
value = 12345.6789
print(f"{value:e}")  # Lowercase exponential format
# Output: "1.234568e+04"
print(f"{value:E}")  # Uppercase exponential format
# Output: "1.234568E+04"

5. Floating Point Decimal Format (f and F)
value = 3.14159
print(f"{value:5.3f}")  # Ensures the number has 5 digits in total, with 3 digits after the decimal point
# Output: "3.142"

6. Single Character (c)
value = 65
print(f"{value:c}")  # Converts the integer to a character (ASCII)
# Output: "A"

7. String (s)
name = "Alice"
print(f"{name:s}")  # Converts the object to a string
# Output: "Alice"

8. Percentage (%)
value = 0.75
print(f"{value:.0%}")  # Converts the number to a percentage
# Output: "75%"

9. Flags
Zero Padding (0)
value = 5
print(f"{value:02d}")  # Zero-padded to 2 digits
# Output: "05"

Left Adjusted (-)
value = 5
print(f"{value:<2d}")  # Left-adjusted within 2 spaces
# Output: "5 "

Sign Character (+)
value = 5
print(f"{value:+d}")  # Sign character will precede the conversion
# Output: "+5"

Blank Space ( )
value = 5
print(f"{value: d}")  # A blank space is inserted before the value
# Output: " 5"
"""

"""
################
for date time
#################
%A: Day of the week
%D: Date 
%T: Time
%Y: Year with century (e.g., 2024)
%m: Month as a zero-padded decimal number (e.g., 09)
%d: Day of the month as a zero-padded decimal number (e.g., 17)
%H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 18)
%M: Minute as a zero-padded decimal number (e.g., 40)
%S: Second as a zero-padded decimal number (e.g., 13)

from datetime import datetime as d

now = d.now()
print(now)
formatted_date = f"{now:%T}"
"""