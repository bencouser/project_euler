# Find the sum of the only eleven primes that are both truncatable from left to right
# and right to left

import MyModule as mm

countTruncatableBoth = 0
sumTruncatableBoth = 0
number = 13

while countTruncatableBoth < 12:
    if mm.is_it_prime(number):
        digits = mm.find_digits(number)
        length = len(digits)
        if is_it_prime(digits[0]) and is_it_prime(digits[length - 1]):
            for i in range(length):
                
    number += 1

        

