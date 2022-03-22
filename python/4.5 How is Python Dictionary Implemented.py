"""


Here is everything about Python dicts that I was able to put together (probably more than anyone would like to know;
but the answer is comprehensive).

Python dictionaries are implemented as hash tables.

Hash tables must allow for hash collisions i.e. even if two distinct keys have the same hash value, the table's
implementation must have a strategy to insert and retrieve the key and value pairs unambiguously.

Python dict uses open addressing to resolve hash collisions (explained below) (see dictobject.c:296-297).

Python hash table is just a contiguous block of memory (sort of like an array, so you can do an O(1) lookup by index).

Each slot in the table can store one and only one entry. This is important.

Each entry in the table is actually a combination of the three values: < hash, key, value >. This is implemented as a
C struct (see dictobject.h:51-56).

The figure below is a logical representation of a Python hash table. In the figure below, 0, 1, ..., i, ... on the
left are indices of the slots in the hash table (they are just for illustrative purposes and are not stored along
with the table obviously!).

  # Logical model of Python Hash table
  -+-----------------+
  0| <hash|key|value>|
  -+-----------------+
  1|      ...        |
  -+-----------------+
  .|      ...        |
  -+-----------------+
  i|      ...        |
  -+-----------------+
  .|      ...        |
  -+-----------------+
  n|      ...        |
  -+-----------------+
When a new dict is initialized it starts with 8 slots. (see dictobject.h:49)

When adding entries to the table, we start with some slot, i, that is based on the hash of the key.
 CPython initially uses i = hash(key) & mask (where mask = PyDictMINSIZE - 1, but that's not really important). Just
 note that the initial slot, i,
  that is checked depends on the hash of the key.

If that slot is empty, the entry is added to the slot (by entry, I mean, <hash|key|value>). But what if that slot is
occupied!? Most likely because another
 entry has the same hash (hash collision!)

If the slot is occupied, CPython (and even PyPy) compares the hash AND the key (by compare I mean == comparison not
the is comparison)
of the entry in the slot against the hash and key of the current entry to be inserted (dictobject.c:337,
344-345) respectively. If both match, then it thinks the
entry already exists, gives up and moves on to the next entry to be inserted. If either hash or the key don't match,
it starts probing.

Probing just means it searches the slots by slot to find an empty slot. Technically we could just go one by one, i+1,
i+2, ... and use the first available one
(that's linear probing). But for reasons explained beautifully in the comments (see dictobject.c:33-126),
CPython uses random probing. In random probing,
the next slot is picked in a pseudo random order. The entry is added to the first empty slot. For this discussion,
the actual algorithm used to pick the next slot is
not really important (see dictobject.c:33-126 for the algorithm for probing). What is important is that the slots are
probed until first empty slot is found.

The same thing happens for lookups, just starts with the initial slot i (where i depends on the hash of the key). If
the hash and the key both don't match the entry in
 the slot, it starts probing, until it finds a slot with a match. If all slots are exhausted, it reports a fail.

BTW, the dict will be resized if it is two-thirds full. This avoids slowing down lookups. (see dictobject.h:64-65)

NOTE: I did the research on Python Dict implementation in response to my own question about how multiple entries in a
dict can have same hash values. I posted a
slightly edited version of the response here because all the research is very relevant for this question as well.

Share
Improve this answer
Follow
edited Jul 22 '20 at 9:51

Manuel Selva



"""
import functools

# Dictionary of string and int
word_freq = {
        "hello" : 56 ,
        "at" : 23 ,
        "test" : 43 ,
        "hello" : 78
}
key = 'test'
# python check if key in dict using "in"
if key in word_freq :
    print ( f"Yes, key: '{key}' exists in dictionary" )
else :
    print ( f"No, key: '{key}' does not exists in dictionary" )

# dictionary safe method return None if no key found
print ( word_freq.get ( "Hello" ) )

print ( sorted ( word_freq ) )

functools.reduce(lambda (x,y) : x.get("hello")+y.get("hello"), word_freq)