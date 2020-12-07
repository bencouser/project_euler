import math

# function to efficiently get all factors
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

# function reutns true or false depending if it is an abundant number
def isAbundant(number):
    factorsNumber = factors(number)
    sumFactors = sum(factorsNumber)
    return number < sumFactors

abundantNumbers = []
notSumofTwoAN = []

        


