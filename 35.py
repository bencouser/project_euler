# The number 197 is a circular prim as 197, 971 and 719 are all themselves prime
# How many circular primes are there below one million

import MyModule as mm
import itertools

count = 0
listPrimes = []

def digit_to_number(digits):
    s = ''.join(map(str, digits))
    return int(s)

for i in range(2, 1000001):
    if mm.is_it_prime(i) == True:
        listPrimes.append(i)

for prime in listPrimes:
    digits = mm.find_digits(prime)
    all_perms = itertools.permutations(digits)
    for perm in all_perms:
        if mm.is_it_prime(digit_to_number(perm)) == False:
            break
    

print(count)
