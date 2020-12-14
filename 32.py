# a number is pandigital is it makes used of digits 1 to n once eg 15243
# We find that 39 x 186 = 7254, this is multipicand, multiplier and producr is
# 1 through 9 pandigital

# Find the sum of all products whose m/m/p identity can be written as 1 => 9 pandigital
# Note: Some products can be obtained in more than one way

import MyModule as mm

def is_it_pandigital(number):
    digits = mm.find_digits(number)
    return len(set(str(number))) == len(digits)
    
print(is_it_pandigital(123))
print(is_it_pandigital(44123))

