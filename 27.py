# euler found that for 0 <= n <= 39, n**2 + n + 41 will give 40 primes. When n= 40 we no
# longer return primes. The formula n**2 - 79n + 1601 produces 80 primes in the same way.
# The product of the coeficients is -126479

# considering the form n**2 + an + b, |a| < 1000 and |b| is <= 1000
# find the product of the coeficients that produces the most consecutive primes, starting
# at n = 0

import math

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

def quadraticForm(n, a, b):
    value = n**2 + n*a + b
    return value

a = 1
b = 41
value = 2
count = 0

while isitPrime(value):
    value = quadraticForm(count, a, b)
    if isitPrime(value):
        count += 1
    else:
        print(count)
        break
