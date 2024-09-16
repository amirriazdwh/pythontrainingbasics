"""
Relational operators compare two values and give a result of either True or False.

== (Equal to):
Checks if two values are the same.
Example: 5 == 5 → True
(Five is the same as five.)

!= (Not equal to):
Checks if two values are different.
Example: 5 != 3 → True
(Five is not the same as three.)

> (Greater than):
Checks if the value on the left is bigger than the one on the right.
Example: 7 > 3 → True
(Seven is greater than three.)

< (Less than):
Checks if the value on the left is smaller than the one on the right.
Example: 3 < 7 → True
(Three is less than seven.)

>= (Greater than or equal to):
Checks if the value on the left is bigger or the same as the one on the right.
Example: 5 >= 5 → True
(Five is greater than or equal to five.)

<= (Less than or equal to):
Checks if the value on the left is smaller or the same as the one on the right.
Example: 4 <= 5 → True
(Four is less than or equal to five.)

##################################
Python operators for String
##################################

Actually, relational operators in Python can be used for strings as well, not just for integers (int) and floating-point numbers (float).
Here’s how they work with strings:

For strings, comparison is based on the lexicographical order (like in a dictionary), meaning it compares the 
strings character by character based on their ASCII/Unicode values.

Examples with Strings:
== (Equal to):
Example: "apple" == "apple" → True
It checks if two strings are exactly the same.
!= (Not equal to):

Example: "apple" != "banana" → True
It checks if two strings are different.
> (Greater than):

Example: "banana" > "apple" → True
It checks if one string comes after another in lexicographical order (here, "b" comes after "a").
< (Less than):

Example: "apple" < "banana" → True
It checks if one string comes before another in lexicographical order.
>= (Greater than or equal to):

Example: "apple" >= "apple" → True
It checks if one string is either greater than or the same as another.
<= (Less than or equal to):

Example: "apple" <= "banana" → True
It checks if one string is either less than or the same as another.
Note:
Comparisons are case-sensitive, meaning "Apple" and "apple" are different because of the capital "A".
So, you can use these relational operators for strings, integers, floats, and even other objects, 
depending on how Python defines the comparison for those objects!



How == Works for Strings in Python:
When you write something like "apple" == "apple", Python sees this and translates it to:

python
"apple".__eq__("apple")
This calls the __eq__() method from the string class, which is responsible for checking if the two strings are equal.

Similarly, for relational operators like >, Python uses the __gt__() method (greater than), and for <, 
it uses __lt__() (less than).

String Comparison Methods:
__eq__(self, other): Called when == is used to check if two strings are equal.
__ne__(self, other): Called when != is used to check if two strings are not equal.
__gt__(self, other): Called when > is used to check if one string is greater than another.
__lt__(self, other): Called when < is used to check if one string is less than another.
__ge__(self, other): Called when >= is used to check if one string is greater than or equal to another.
__le__(self, other): Called when <= is used to check if one string is less than or equal to another.

Example:
python
# When you do this:
result = "apple" == "banana"

# Python does this internally:
result = "apple".__eq__("banana")
Runtime, Not Compile Time:
Python is an interpreted language, so this translation happens at runtime, meaning when the code is executed, 
Python determines which method to call based on the operator you use.

In short, the ==, >, <, etc., operators are translated into their respective special methods 
(__eq__(), __gt__(), etc.) at runtime, and these methods belong to the string class (or any other class 
for that matter).
"""