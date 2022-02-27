'''
Point to remember.   This defines the whole structure of the python.
1.  Python Architecture is made up of three layers scope.
        1.1   Builin scope
        1.2   Global scope
        1.3   local scope.
 2. Everything in python is an object.   class,  data types,  functions,  import ,  modules,   anything which is either a scope or an object has directionary where they store data.
 3. .


 []: Lists and indexing/lookup/slicing

Lists: [], [1, 2, 3], [i**2 for i in range(5)]
Indexing: 'abc'[0] → 'a'
Lookup: {0: 10}[0] → 10
Slicing: 'abc'[:2] → 'ab'

(): Tuples, order of operations, generator expressions, function calls and other syntax.
Tuples: (), (1, 2, 3)
Although tuples can be created without parentheses: t = 1, 2 → (1, 2)
Order of operations: (n-1)**2
Generator expression: (i**2 for i in range(5))
Function or method calls: print(), int(), range(5), '1 2'.split(' ')
with a generator expression: sum(i**2 for i in range(5))

{}: Dictionaries and sets, as well as string formatting
Dicts: {}, {0: 10}, {i: i**2 for i in range(5)}
Sets: {0}, {i**2 for i in range(5)}
Inside f-strings and format strings, to indicate replacement fields: f'{foobar}' and '{}'.format(foobar)
All of these brackets are also used in regex. Basically, [] are used for character classes, () for grouping, and {} for repetition. For details, see The Regular Expressions FAQ.

 in addition,  you use
__call__(self[, args...]) for ()
__getitem__(self, key) for []
'''

help('modules')
