

# Bootstrapping to estimate the confidence interval on a sample of data
# \-> sorted, mean, choices

# Standard error of the mean relies on normal distribution.
# Resampling makes no such assumptions.


from statistics import mean, stddev
from random import choices

timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]
mean(timings)
### 8.377142857142857
stdev(timings)

### 1.4576505256559458

# resample data with replacement for length of data
# result is a new set of data that hopefully has similar
# characteristics to the original
def bootstrap(data)
    return choices(data, k=len(data))
bootstrap(timings)
### [9.06, 6.87, 8.31, 8.16, 10.02, 7.39, 6.87,
### 7.18, 10.02, 9.06, 7.67, 12.24, 7.06, 7.18]
# taking the mean can give us a similar result as the
# original data, but not always.
mean(bootstrap(timings))
### 8.372857142857143
### 7.984285714285714

# let's do it a bunch of times and put the results in a sorted
# list - low to high
n = 10000
means = sorted(mean(bootstrap(timings)) for i in range(n))

# we are looking for a 90% confidence range so we need to chop
# off 5% on either side
round(n * .05)
### 500
means[500]
### 7.804285714285714
means[-500]
### 9.037857142857144

# let's pretty it up.  Note the use of functions and
# indexing within the place holders of the f-strings
print(f'The observed mean of {mean(timings)}')
### The observed mean of 8.377142857142857
print(f'Falls in a 90% confidence interval from {means[500] :.1f} to {means[-500] :.1f}')
###Falls in a 90% confidence interval from 7.8 to 9.0

#============================================================

# Statistical significance of the difference of two means
# \-> shuffle, slicing, mean

# p-value: what is the chance that what we observed is due to chance
# rather than a real effect

drug = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]
from statistics import mean, stdev
mean(drug)
### 7.483333333333333
mean(placebo)
### 6.841666666666667
obs_diff = mean(drug) - mean(placebo)

# assume the null hypothesis - the drug did nothing
# that means we can shuffle the participants, changing
# their label as to whether or not they got the drug.

# if we reshuffle (permuting, relabeling) the participants,
# is the mean diff the same or more extreme than we observed

# get the length of the drug list
# concatenate the lists and shuffle the new combined list
nd = len(drug)
comb = drug + placebo
shuffle(comb)
# the elements at front of the list are the new drug users 
# the rest are placebo users
>>> comb[:nd]
### [7.6, 8.2, 8.5, 7.0, 7.4, 6.9, 8.1, 6.2, 6.1, 6.6, 6.4, 8.4]
>>> comb[nd:]
### [5.1, 4.9, 8.2, 7.1, 8.4, 7.7, 7.1, 7.1, 7.1, 7.4, 8.1, 6.3]

# let's make function that does this and then takes the mean of
# the two new groups and compares the difference of their means to
# the mean diff of the original study. if it's the same or bigger
# we return true
def trial():
    shuffle(comb)
    drug = comb[:nd]
    placebo = comb[nd:]
    new_diff = mean(drug) - mean(placebo)
    return new_diff >= obs_diff

# and do it a bunch of times
n = 10000
sum(trial() for i in range(n)) / n
### 0.0602
# ^---- p-value: likelihood that the outcome was sole due to chance
# usual standard is 5%
# this is pretty low, but high enough to warrant getting more real data

#============================================================

# Single server queue simulation
# \-> expovariate, gauss, mean, median, stdev, conditional expressions

from random import expovariate, gauss
from statistics import mean, median, stdev

average_arrival_interval = 5.6
average_service_time = 5.0
stdev_service_time = 0.5

num_waiting = 0
arrivals = []
starts = []
arrival = service_end = 0.0
for i in range(20000):
    if arrival <= service_end:
        num_waiting += 1
        arrival += expovariate(1.0 /average_arrival_interval)
        arrivals.append(arrival)
    else:
        num_waiting -= 1
        service_start = service_end if num_waiting else arrival
        service_time = gauss(average_service_time, stdev_service_time)
        service_end = service_start + service_time
        starts.append(service_start)

waits = [start - arrival for arrival, start in zip(arrivals, starts)]
print(f'Mean wait: {mean(waits):.1f}.  Stdev wait: {stdev(waits):.1f}.')
print(f'Median wait: {median(waits):.1f}.  Max wait: {max(waits):.1f}.')




