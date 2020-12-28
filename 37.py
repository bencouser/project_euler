# Find the sum of the only eleven primes that are both truncatable from left to right
# and right to left

import MyModule as mm

countTruncatableBoth = 0
sumTruncatableBoth = 0
counter = 13

while countTruncatableBoth < 12:
    if is_it_prime(counter):
        digits = mm.find_digits(counter)
        for digit in range(len(digits) - 1):
            

        

