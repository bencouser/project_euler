# find the value of d < 1000 for which 1/d contains the longest recurring cycle in its
# decimal fraction part

# % for remainder, // for devision without remain

#function to check length of a remainder 

# in example 7 is largest and is prime, lets find the primes from 1-1000

import math

primeList = []

def getFactors(number):
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

def isitPrime(number):
    return len(getFactors(number)) == 2    

for i in range(1,1001):
    if isitPrime(i):
        primeList.append(i)

def find_period(d):
    z = x = 1 * 9
    k = 1
    while z % d:
        z = z * 10 + x
        k += 1
    return k

maxPeriod = 0
maxPrime = 0

for i in range(5, (len(primeList))+ 1):
    print("Checking: ", primeList[i])
    period = find_period(i)
    if period > maxPeriod:
        maxPeriod = period 
        maxPrime = i
    else:
        pass

print(maxPrime)
