"""
Python Strings Pattern
Quotes:

Single: 'Single quotes'
Double: "Double quotes"
Escape Quotes: \' or \"
String Creation:

Single Line: 'Text' or "Text"
Multi-line: '''Text''' or double qoute
variable assess:  "this is variable $var"

Concatenation Patterns
Adjacent Strings with single space:
s = "Part1" "Part2"   -- python automaticall adds join method.   "Part1".join"Part2"

+ Operator:
s = "Part1" + "Part2"

+= Operator:
s = "Part1"
s += " Part2"

join() Method:
s = ''.join([s1, s2])

join() with Separator:
s = ','.join([s1, s2, s3])

format() Method:
s = '{} {} {}'.format(var1, var2, var3)
var1 is replaced with first {} and so on
first {} is actually {0} so replaced with var1 in tuple


f-strings:
s = f'{var1} {var2} {var3}'
its another way to represent format Method.

Formatting Patterns
Old Style (%):
print("Text %s" % value)
format() Method:

print("Text {}".format(value))
{0} for position

f-strings:
print(f"Text {value}")

Template Strings:
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