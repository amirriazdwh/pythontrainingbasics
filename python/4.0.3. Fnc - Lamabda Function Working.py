from functools import reduce

# iterator and generators are two ways to get the objects

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]

# Use lambda function with `filter()`_ under score are throw away
# variables
filtered_list = list(filter(lambda _: (_ * 2 > 10), my_list))
filtered_list = [filter(lambda _: (_ * 2 > 10), my_list)]

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x * 2, my_list))
print('.... this is list ...')
genobj=map(lambda x: x * 2, my_list)
mapped_list = [x for x in genobj]
print(mapped_list)

# generator can be queried only once after generation they are created by
# yield key word
# list, set,
print("___________________________________")
for x in genobj:
    print(x)
print("___________________________________")

gen = list(genobj)
print(gen)

mapped_list = list(map(lambda _: _ * 2, my_list))
mapped_list = list(map(lambda _: _ + 2, my_list))

# Use lambda function with `reduce()`
reduced_list = [reduce(lambda x, y: x + y, my_list)]
reduced_list = [reduce(lambda x, y: x + y, my_list)]

# its seems in python for two arguments _ does not work.
# reduced_list1= reduce(lambda _,_: (_+_) , my_list)
print(filtered_list)
print(mapped_list)
print(reduced_list)


def myfunc(a, b):
    return a + b

aa = ('apple', 'banana', 'cherry')
bb = ('orange', 'lemon', 'pineapple')
x11 = list(map(lambda x, y: x + y, aa, bb))
print(x11)

a = [1, 2, 3]
b = [4, 5, 6]

add_list = ''.join(list(map(lambda x, y: str(x + y), a, b)))
print(add_list)
print(type(add_list))

add_list = [map(lambda x, y: x + y, a, b)]
print(add_list)
add_list = list(map(lambda x, y: x + y, a, b))
print(add_list)

add_list = set(map(lambda x, y: x + y, a, b))
print(add_list)

add_list = dict(map(lambda x, y: (x, x + y), a, b))
print(add_list)

def generate_power(number):
    """
    Examples of use:

    >>> raise_two = generate_power(2)
    >>> raise_three = generate_power(3)
    >>> print(raise_two(7))
    128
    >>> print(raise_three(5))
    243
    """

    # Define the inner function ...
    def nth_power(power):
        return number ** power
    # ... that is returned by the factory function.

    return nth_power

raise_two = generate_power(2)
print(raise_two(7))

def generate_pow(exponent):
  -  def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return decorator

aa=[1,2,3,4,5]
bb=[4,5]
cc=[*aa, *bb]
print(cc)

cc=[aa,bb]
print(cc)