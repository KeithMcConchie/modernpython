from random import *
# providing a seed for the random number generator
# ensures replicable results.
seed(8675309)
random()
### 0.40224696110279223
random()
### 0.5102471779215914
random()
###0.5102471779215914

# uniform distribution all numbers equally likely
uniform(1000, 1100)

# triangular distribution favors points around the mode
# (midpoint by default but can be specified with optional
# 3rd parameter
triangular(1000, 1100)
### 1037.4795077189701
triangular(1000, 1100)
### 1057.65582224645
triangular(1000, 1100)
### 1058.0008067615947

# gauss less angular
# example shows IQ example
# avg IQ 100.  stdev 15
gauss(100, 15)
### 103.38405277270745
gauss(100, 15)
### 123.41436861264779
gauss(100, 15)
### 101.99785389189366

# expovariate - used to simulate arrival times
# distribution centers around reciprical of argument
# so expovariate(20) centers around .05 (1/20)
expovariate(20)
### 0.11416353263962384
expovariate(20)
### 0.0523532783809665

# triangular mean is centered sharply around midpoint
# (smaller stdev)
from statistics import mean, stdev
data = [triangular(1000, 1100) for i in range(1000)]
mean(data)
### 1048.7593107346681
stdev(data)
### 20.13510622686606

# uniform mean is still centered around midpoint
# but larger stdev
data = [uniform(1000, 1100) for i in range(1000)]
mean(data)
### 1051.0406593043674
stdev(data)
### 28.545863280007982

# gauss gives us very close to mean and stdev
# provided in the arguments
data = [gauss(100, 15) for i in range(1000)]
mean(data)
### 100.05158436289322
stdev(data)
### 15.127994378264072

# expovariate(n) delivers a mean around 1/n
# stdev is sometimes larger than expected because
# exponential distribution can create really large outliers
data = [expovariate(20) for i in range(1000)]
mean(data)
### 0.046808845970613015
stdev(data)
### 0.047258431601712725

from random import choice, choices, sample, shuffle
# choice and choices sample with replacement
# so they can have dupes
outcomes = ['win', 'lose', 'draw', 'play again', 'double win']
choice(outcomes)
### 'draw'
choice(outcomes)
### 'draw'
choice(outcomes)
### 'play again'
choice(outcomes)
### 'play again'
choices(outcomes, k=10)
### ['double win', 'lose', 'win', 'double win', 'play again',
### 'play again', 'play again', 'play again', 'draw', 'double win']

# as all choices are equally likely (by default - we can add weights),
# the more times we sample the more likely the counts will converge on the
# same number
from collections import Counter
Counter(choices(outcomes, k=10))
### Counter({'play again': 4, 'draw': 3, 'lose': 2, 'win': 1})
Counter(choices(outcomes, k=10000))
### Counter({'double win': 2013, 'win': 2005, 'play again': 2003, 'lose': 2002, 'draw': 1977})

# this time we will weight the outcomes: 'win' will
# come up about 5 times more than 'double win'
Counter(choices(outcomes, [5, 4, 3, 2, 1], k=10000))
### Counter({'win': 3295, 'lose': 2678, 'draw': 2017, 'play again': 1353, 'double win': 657})

# shuffle works like sort, changing the list in place,
# and randomly shuffles the order of the items
# original outcomes:
outcomes
### ['win', 'lose', 'draw', 'play again', 'double win']
# shuffle them
shuffle(outcomes)
# show new outcomes list
outcomes
### ['lose', 'double win', 'play again', 'draw', 'win']

# again choices samples with replacement, thus allowing
# duplicates:
choices(outcomes, k=5)
### ['lose', 'lose', 'lose', 'double win', 'lose']

# sample samples without replacement, therefore no duplicates:
sample(outcomes, k=4)
### ['double win', 'win', 'play again', 'draw']
sample(outcomes, k=4)
### ['double win', 'lose', 'draw', 'play again']
sample(outcomes, k=4)
### ['win', 'double win', 'play again', 'draw']

# California lottery example.  values are a list from
# 1 to 56 consecutive.  Sample six (no dupes), and display
# in sorted order
sorted(sample(range(1, 57), k=6))
### [5, 17, 20, 42, 44, 46]

# sampling with k=1 yields a list of one item.
# If we index the 0 item of that list:
sample(outcomes, k=1)[0]
### 'draw'
# it is the same thing as if we used choice
choice(outcomes)
### 'draw'

# similarly if we used shuffle on outcomes
shuffle(outcomes); outcomes
### ['lose', 'win', 'play again', 'double win', 'draw']
# it's the same thing as if we used sample with k equal to
# the number of items in outcomes.
sample(outcomes, k=len(outcomes))
### ['win', 'lose', 'draw', 'play again', 'double win']
