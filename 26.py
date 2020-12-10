# find the value of d < 1000 for which 1/d contains the longest recurring cycle in its
# decimal fraction part

# % for remainder, // for devision without remain

#function to check length of a remainder 

# in example 7 is largest and is prime, lets find the primes from 1-1000

import math
import itertools

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

maxPeriod = 0
maxPrime = 0

for i in range(1, len(primeList)):
    seenNumbers = {}
    n = primeList[i-1]
    term = 1
    for j  in itertools.count():
        if term in seenNumbers:
            if len(seenNumbers) > maxPeriod:
                maxPeriod = len(seenNumbers)
                maxPrime = primeList[i-1]
            else:
                break
        else:
            seenNumbers[term] = i
            term  = term * 10 % n
            
print(maxPrime)
