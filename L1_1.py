# old style formatting: %d is integer %s is string.
# values go in a tuple to the right of the string
x = 10
y = 20
print('The answer is %d today, %d %s' % (x, y, 'tomorrow'))
### The answer is 10 today, 20 tomorrow

# newer style format.  Place holders are positional.  Values are positional
# arguments to the .format() function of the string.
print('The answer is {0} today {1} tomorrow'.format(x, y))
### The answer is 10 today 20 tomorrow

# newer style format with aliases.  This form uses keywords for the place
# holders and aliases them in the arguments to format.  Place holders use
# the aliases to refer to the arguments.
print('The answer is {y} today {x} tomorrow'.format(x=x, y=y))
### The answer is 20 today 10 tomorrow

# newest style f-strings.  Place holders no how to reach into the python
# environment to get the values of actual python variables
print(f'The answer is {x} today {y} tomorrow')
### The answer is 10 today 20 tomorrow

# No runtime eval - secure.  Supports formatting:
print(f'The answer is {x :08d} today')
### The answer is 00000010 today

# Also supports small expressions - not really recommended.
print(f'The answer is {x ** 2 :08d} today')
### The answer is 00000100 today

# Delivers the name of the data type
type(x).__name__
### 'int'

# Within a placeholder in an f-string x!r gives the __repr__ of the object
# This doesn't seem to work on the command line, though
raise ValueError(f"Expected {x!r} to be a float not a {type(x).__name__}")

# Counter is a dictionary-like item, but when you refer to an item not in the
# Counter e.g. c['purple'], it returns 0.  If you add an entry and it exists
# it increments the item's count, otherwise it adds the key and inits it's count
# to zero.  The constructor can accept a list of items to count.
from collections import Counter
c = Counter('red green red blue red blue green'.split())
c
### Counter({'red': 3, 'green': 2, 'blue': 2})

# most_common
c.most_common(1)  
### [('red', 3)]
c.most_common(2)
### [('red', 3), ('green', 2)]

list(c.elements())
### ['red', 'red', 'red', 'green', 'green', 'blue', 'blue']

list(c)
### ['red', 'green', 'blue']

list(c.values())
### [3, 2, 2]

list(c.items())
### [('red', 3), ('green', 2), ('blue', 2)]

# Statistics module
# Designed for accuracy to prevent amplification of small errors
from statistics import mean, median, mode, stdev, pstdev

# mean (sum of items) / num items
mean([50, 52, 53])
### 51.666666666666664

# median: middle value.  If two middle values (num items even) average
# of the two
median([50, 52, 53])
### 52
median([51, 50, 52, 53])
### 51.5

# mode - item that occurs most often
>>> mode([51, 50, 52, 53, 51, 51])		     
51

# Standard Deviation - divides by N-1
stdev([51, 50, 52, 53, 51, 51])
### 1.0327955589886444

# Population Standard Deviation - divides by N
pstdev([51, 50, 52, 53, 51, 51])  
### 0.9428090415820634

# See Transcripts for explanation of difference between Population Std Dev and
# Std dev

#  list concatenation 
s = [10, 20, 30]
t = [40, 50, 60]
u = s + t
u		     
### [10, 20, 30, 40, 50, 60]  numpy would do an element by element addition

# Slicing - first two items
u[:2]
### [10, 20]

# last two
u[-2:]     
### [50, 60]

# slap them together
u[:2] + u[-2:]     
[10, 20, 50, 60]

# all sequences (strings, lists, sets) have count() and index()
s = 'abracadabra'
i = s.index('c') #location of first 'c'
i     
### 4
s.count('c') # count of occurences     
### 1
s.count('a')		     
### 5

# sort list in place
s = [10, 5, 70, 2]     
s.sort()
s	     
### [2, 5, 10, 70]

# create a new sorted list
s = [10, 5, 70, 2]
t = sorted(s)
s
### [10, 5, 70, 2]
t
### [2, 5, 10, 70]

# because sorted creates a new list, it can be used on any iterable -
# even unmutable ones.
sorted('cat')

# lambda -> partial, itemgetter, attrgetter, ...
# should just be called makefunction()
# create a function
lambda x: x**2
### <function <lambda> at 0x7fc31a07a840>
# call a function with (5)
(lambda x: x**2)(5)
### 25
100 + (lambda x: x**2)(5) + 50
### 175		     

# lambda can take multiple arguments
f = lambda x, y: 3*x + y
f(3, 8)
### 17

# defer a computation - useful for async situations
# aka - Freeze and thaw, promises, thunks
x = 10
y  = 20
# note no arguments to this func
f = lambda : x ** y

# chained comparisons
x = 15
6 < x < 20
### True
