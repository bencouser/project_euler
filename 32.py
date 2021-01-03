# a number is pandigital is it makes used of digits 1 to n once eg 15243
# We find that 39 x 186 = 7254, this is multipicand, multiplier and producr is
# 1 through 9 pandigital

# Find the sum of all products whose m/m/p identity can be written as 1 => 9 pandigital
# Note: Some products can be obtained in more than one way

import math

def is_it_pandigital(listDigits):
    return "".join(sorted(listDigits)) == "123456789"

def find_pandigital_product(number):
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            possible_pp = str(number) + str(i) + str(number // i)
            print(possible_pp)
            if is_it_pandigital(possible_pp):
                print(possible_pp)
                return True
    return False

sum = 0

for j in range(10, 10001):
    if find_pandigital_product(j):
        sum += j
        
print(sum)
