# prime factors of 13195 are 5,7,13,29

# what is the largest prime factpr of 600851475143?

import numpy as np

number = 600851475143

def all_factors(N):
        factors = []
        for i in range(1, int(np.sqrt(N) + 1)): #we only need to check up to the root of ur number
                if N % i == 0:
                        factors.append(i)
        factors.append(N)
        return factors

def is_it_prime(n):
        return len(all_factors(n)) == 2

allFactors = all_factors(number)

largestPrime = 0

for i in range(len(allFactors)):
        if is_it_prime(allFactors[i]):
                largestPrime = allFactors[i]

print(largestPrime)
