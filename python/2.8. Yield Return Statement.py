
"""
The return statement in a generator
In Python 2:

In a generator function, the return statement is not allowed to include an expression_list. In that context, a bare
return indicates that the generator is done and will cause StopIteration to be raised.

An expression_list is basically any number of expressions separated by commas - essentially, in Python 2, you can stop
the generator with return, but you can't return a value.

In Python 3:

In a generator function, the return statement indicates that the generator is done and will cause StopIteration to be
raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the
StopIteration.value attribute.

In an asynchronous generator function, an empty return statement indicates that the asynchronous generator is done and
will cause StopAsyncIteration to be raised. A non-empty return statement is a syntax error in an asynchronous
generator function.



yield was originally introduced as a statement, meaning that it could only appear at the beginning of a line in a code
 block. Now yield creates a yield expression. https://docs.python.org/2/reference/simple_stmts.html#grammar-token-yield_stmt
 This change was proposed to allow a user to send data into the generator just as one might receive it. To send data,
 one must be able to assign it to something, and for that, a statement just won't work.

 some times you notice that by end of generator method there is no return statement given.  why?
 this is because python add return statement at the end of method implicitly if return is not given.
 however,  adding return statement at the end of a generator method gives you control to pass a values which you
 can read from excep
"""

# Yield will not raise StopIteration exception.  i will just create a generator object and pass it to outer system.
#  in generators method return will generate stopiteration exception.

def str_gen():
    yield 'I am'
    yield 'a generator!'
    return -1

for x in str_gen():
    print(x)

values_iter =str_gen()
try:
    while True:
        i = next(values_iter)
        print(i)
except StopIteration as e:
    values_summary = e.value
    print("The value returned from the return statement is:",values_summary)


def my_generator0(n):
    for i in range(n):
        yield i
        if i >= 5:
            return -1

values_iter =my_generator0(6)
try:
    while True:
        i = next(values_iter)
        print(i)
except StopIteration as e:
    values_summary = e.value
    print("The value returned from the return statement is:",values_summary)


def my_generator1(n):
    for i in range(n):
        yield i
        if i >= 5:
            raise StopIteration

values_iter =my_generator1(6).__iter__()
try:
    while True:
        i = next(values_iter)
        print(i)
except StopIteration as e:
    values_summary = e.value
    print("The value returned from the StopIteration statement is:",values_summary)
except RuntimeError as err:
    print("The value returned from the StopIteration statement is:",err)


"""
how generator function works under the hood

Generator Object: 
When you call a generator function, it returns a generator object. This object acts as an intermediary between the generator function and the caller.

State Management: 
The generator function’s state (local variables, execution point) is saved within the generator object. 
This allows the function to pause and resume execution.

Yielding Values: 
When the generator function encounters a yield statement, it:
Saves its current state.
Yields the specified value to the caller.
Pauses execution, transferring control back to the caller.

Caller Interaction: 
The caller interacts with the generator object using the next() function (or a loop). When next() is called:
The generator function resumes execution from where it left off.
It continues until it hits the next yield statement or completes execution.

Control Transfer: This back-and-forth control transfer continues until the generator function either:
Yields another value.
Completes execution, raising a StopIteration exception to signal the end of the iteration.

Key Points
yield: Produces a value and pauses the function, saving its state.
return: Terminates the generator function and raises StopIteration. 
If a value is provided, it becomes the value attribute of the StopIteration exception.
Using yield allows the generator to produce a sequence of values lazily, while return can be used to signal 
the end of the sequence explicitly

def my_generator():
    yield (1, 2, 3)

gen = my_generator()
print(next(gen))  # Output: (1, 2, 3)

"""