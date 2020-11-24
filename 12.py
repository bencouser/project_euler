# finally completed, realised i didnt have to find all terms but just double alf the terms to find the number of divisors
import math

def triangleN(term):
    numbers = []
    for i in range(1, term):
        numbers.append(i)
    return sum(numbers)

def nFactors(number):
    half_factors = []
    for i in range(1, math.ceil(number ** (1/2))):
        if number % i == 0:
            half_factors.append(i)
    nOfFactors = 2 * len(half_factors)
    return nOfFactors

n = 2

while True:
    if nFactors(triangleN(n)) > 500:
        print(triangleN(n))
        break
    else:
        n += 1

