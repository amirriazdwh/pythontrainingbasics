"""
value = 3.14
if isinstance(value, (int, float)):
    print(f"{value} is either an integer or a float.")  # Output: 3.14 is either an integer or a float.

"""
"""
This is known as a ternary conditional operator or conditional expression in Python.
It allows you to write an if-else statement in a single line. The general syntax is:
<expression1> if <condition> else <expression2>

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult


def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(check_even_odd(4))  # Output: Even
print(check_even_odd(5))  # Output: Odd

my_list = [1, 2, 3, 4, 5]
new_list = [x * 2 if x % 2 == 0 else x / 2 for x in my_list]
print(new_list)  # Output: [0.5, 4, 1.5, 8, 2.5]


score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # Output: B


for loop ternary or composition. 
generator = (expression for item in iterable if condition)


"""