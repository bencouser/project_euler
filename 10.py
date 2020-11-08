#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

#Find the sum of all the primes below two million

import numpy as np

def all_factors(N):
        factors = []
        for i in range(1, int(np.sqrt(N) + 1)): #we only need to check up to the root of ur number
                if N % i == 0:
                        factors.append(i)
        factors.append(N)
        return factors

def is_it_prime(n):
        return len(all_factors(n)) == 2

primes = []

for i in range(2000000):
        if is_it_prime(i):
                primes.append(i)

print(sum(primes))
