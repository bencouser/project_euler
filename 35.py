# The number 197 is a circular prim as 197, 971 and 719 are all themselves prime
# How many circular primes are there below one million

import MyModule as mm

count = 0
listPrimes = []

def digit_to_number(digits):
    s = ''.join(map(str, digits))
    return int(s)

def find_circular_perms(digits):
    all_perms = []
    all_perms.append(digits)
    for i in range(len(digits)-1):
        new_perm = digits[i+1:] + digits[:i+1]
        all_perms.append(new_perm)
    return all_perms

for i in range(2, 1000001):
    if mm.is_it_prime(i):
        listPrimes.append(i)

for prime in listPrimes:
    digits = mm.find_digits(prime)
    miniCount = 1
    all_perms = find_circular_perms(digits)
    for perm in all_perms:
        if mm.is_it_prime(digit_to_number(perm)) is False:
            miniCount = 0
    if miniCount == 1:
        count += 1

print(count)
