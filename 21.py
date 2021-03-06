# d(n) is the sum of divisors of n
# if d(a) = b and d(b) = a, where a != b
# this is an amicable pair
# d(220) = 284 and d(284) = 220 for example

# evaluate the sum of all amicable numbers under 10000.
import math

def factors(number):
    half_factors = []
    factors = []
    for potentialFactor in range(1, int(math.sqrt(number)) + 1):
        if number % potentialFactor == 0:
            half_factors.append(potentialFactor)
    size = len(half_factors)
    for i in range(size):
        factors.append(half_factors[i])
    for factor in range(size):
        fact = number / half_factors[factor]
        if fact in factors:
            pass
        else:
            factors.append(fact)
    return factors


def dFunction(number):
    return (sum(factors(number)) - number)

amicableNumbers = []

def isAmicable(a, b, amicableNumbers):
    if dFunction(a) == b and dFunction(b) == a:
        amicableNumbers.append(a)
        amicableNumbers.append(b)

for i in range(1,10001):
#    print(i, amicableNumbers)
    for j in range(i + 1, 10001):
        isAmicable(i,j,amicableNumbers)


print(sum(amicableNumbers))
