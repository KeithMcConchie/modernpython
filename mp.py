timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]
from statistics import mean, stddev
mean(timings)
# 8.377142857142857

stdev(timings)

# 1.4576505256559458

from random import choices
def bootstrap(data)
    return choices(data, k=len(data))
bootstrap(timings)
    
