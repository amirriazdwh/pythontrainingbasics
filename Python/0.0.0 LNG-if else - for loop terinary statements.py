"""
value = 3.14
if isinstance(value, (int, float)):
    print(f"{value} is either an integer or a float.")  # Output: 3.14 is either an integer or a float.

"""
"""

generator = (expression for item in iterable if condition)
[expression for item in iterable if condition]

This is known as a ternary conditional operator or conditional expression in Python.
It allows you to write an if-else statement in a single line. The general syntax is:
<expression1> if <condition> else <expression2>

The ternary conditional operator is used for concise, inline conditional expressions.
 It’s particularly useful when you want to assign a value based on a condition in a single line

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult


def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(check_even_odd(4))  # Output: Even
print(check_even_odd(5))  # Output: Odd

my_list = [1, 2, 3, 4, 5]
new_list = [(x * 2 if x % 2 == 0 else x / 2) for x in my_list]
print(new_list)  # Output: [0.5, 4, 1.5, 8, 2.5]


score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # Output: B


for loop ternary or composition. 
generator = (expression for item in iterable if condition)


"""

"""
The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression. This can make your code more concise and readable by combining assignment and expression evaluation in a single line.

Syntax
Python

variable := expression
AI-generated code. Review and use carefully. More info on FAQ.
Examples
Using in a while loop:
Python

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())
AI-generated code. Review and use carefully. More info on FAQ.
In this example, n is assigned the length of numbers and used in the loop condition.
Using in an if statement:
Python

if (n := len(numbers)) > 3:
    print(f"List is too long: {n} elements")
AI-generated code. Review and use carefully. More info on FAQ.
Here, n is assigned the length of numbers and checked if it’s greater than 3.
Using in list comprehensions:
Python

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data = [y for x in data if (y := x * 2) > 10]
print(filtered_data)  # Output: [12, 14, 16, 18, 20]
AI-generated code. Review and use carefully. More info on FAQ.
In this example, y is assigned x * 2 and only included in filtered_data if y > 10.
Using in a function call:
Python

def process(value):
    print(f"Processing {value}")

if (result := process(10)) is not None:
    print("Function executed")
AI-generated code. Review and use carefully. More info on FAQ.
Here, result is assigned the return value of process(10) and checked if it’s not None.
Benefits
Reduces redundancy: Avoids repeating expressions.
Improves readability: Combines assignment and condition checking in one line.
Enhances performance: Reduces the number of evaluations of the same expression.
Considerations
Readability: While it can make code more concise, overuse or misuse can reduce readability.
Compatibility: Only available in Python 3.8 and later.
"""