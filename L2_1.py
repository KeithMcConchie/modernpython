# Big Idea:
# Statistics modeled in a probram are easier to
# get right and understand than using a formulaic
# approach.

# See:
# Jake Vanderplas: Statistics for Hackers
# Peter Norvig: A Concrete Introduction to Probability

# Examples
# ========
#============================================================

# Six roulette wheel spins
# \-> choices with weighting
# Six roulette wheel spins
# first model the wheel -- 18 red 18 black 2 green

# small example first 3 red 3 black one green
choice(['red', 'red', 'red', 'black', 'black', 'black', 'green'])
### 'black'
choice(['red', 'red', 'red', 'black', 'black', 'black', 'green'])
### 'red'

# Typing is for the birds - use multiply to condense our list
# creation.
['red'] * 18
### ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2)
### 'red'

# we don't want to build the list every time - store it in population
population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
choice(population)
### 'green'

# spin the wheel 6 times
[choice(population) for i in range(6)]
### ['red', 'red', 'red', 'black', 'red', 'black']
# put a counter on it to count the choices - results will be different
# because we are re-doing the spins
Counter([choice(population) for i in range(6)])
###Counter({'black': 4, 'red': 2})

# we can do better, using choices allows us to eliminate
# the for loop
choices(population, k=6)
### ['black', 'black', 'black', 'black', 'black', 'red']

# again we can put a counter on it
Counter(choices(population, k=6))
### Counter({'black': 4, 'red': 2})

# but wait we can do even better - we can avoid constructing
# population altogether by using weights.  we are down to
# one line of code!
Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
### Counter({'red': 4, 'black': 2})

#============================================================

# deal 20 playing cards without replacement (16 tens, 36 low)
# \-> Counter, elements, sample, list.count

# Instead of a list, the Counter constructor can also take initial values
# for each item
>>> deck = Counter(tens=16, low=36)
# elements gives us the individual elements
>>> list(deck.elements())
### ['tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens',
###  'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens',
###  'tens', 'tens', 'low', 'low', 'low', 'low', 'low', 'low',
###  'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low',
###  'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low',
###  'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low']

# create the deck - deck is currently in the order above
# need to mix them up with sample - why didn't he just use
# shuffle??
deck = list(deck.elements())
deal = sample(deck, 52)
remainder = deal[20:]
# looking for a high proportion of tens in the remaining deck
# to have a better chance of winning.  Better luck next time.
Counter(remainder)
### Counter({'low': 20, 'tens': 12})

#============================================================

# 5 or more heads from 7 spins of a biassed coin
# \-> lambda, choices, list.count

# heads is weighted to come up 60% of the time
choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7)
### ['heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads']

# let's count how many times heads comes up
choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads')
### 3

# Now let's use a conditional to count figure out whether we got at least 5
# or more heads
choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >=5
### False

# let's make a function with lambda with no args
trial = lambda : choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >=5
# now we can execute it repeatedly by just calling trial()
trial()
### False
trial()
### False
trial()
### True

# now run it a whole bunch of times and take the mean
# (True has an integer value of one, so we can sum it)
n = 100000
sum(trial() for i in range(n)) / n
### 0.421

# Compare to the analytic approach
from math import factorial as fact
# 4 * 3 * 2 * 1
fact(4)
### 24

# the combinations of n things taken r at a time
def comb(n, r):
	return fact(n) // fact(r) // fact(n - r)
comb(10, 3)
### 120
comb(10, 2)
### 45

ph = 0.6
ph ** 5 * (1 - ph) **2 * comb(7, 5)
### 0.2612736
ph ** 6 * (1 - ph) ** 1 * comb(7, 6)
### 0.13063679999999997
ph ** 7 * (1 - ph) ** 0 * comb(7, 7)
### 0.027993599999999993
0.2612736 + 0.13063679999999997 + 0.027993599999999993
### 0.419904  # theoretical result
### 0.421     # empirical result
# theoretical method involves researching formula and implemnting
# factorials can become unmanageably large
# empirical observation from simulation method scales much better
# and is at most 3 lines of code:
trial = lambda : choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >=5
n = 100000
sum(trial() for i in range(n)) / n
### 0.42207

#============================================================

# Probablility that the median of 5 samples falls in a middle quartile
# \-> chained comparison, choices from a range

#============================================================

# how big is my population
n = 100000
# where do the middle quartiles start and end?
n // 4
25000
n * 3 // 4
75000

# set up a trial testing to see if the median of the population falls in
# the middle quartiles.  low end of the range is not inclusive but top of
# range is inclusive.
trial = lambda : n // 4 < median(sample(range(100000), 5)) <= n * 3 // 4
# take the mean the n here does not HAVE to be the same
# as the n in the trial statement.  It can be any sufficiently large value
# using the same n was just convenient.
sum(trial() for i in range(n)) / n

# so the whole thing boils down to three lines of code 
n = 100000
trial = lambda : n // 4 < median(sample(range(100000), 5)) <= n * 3 // 4
sum(trial() for i in range(n)) / n
### 0.79124
