# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20


# done through logic rather than code, the number will be the combination of the fewest prime numbers

# we need a number to divide by 20,19,...,2 but for example 10 = 5*2 and thus we do
nt need to include it.

# we need to account that 16 = 2**4 and therefore our answer must be divisable by 1
6 and we dont need to use 2,4 or 8 (same logic for 9)

answer = (2**4) * (3**2) * 5 * 7 * 11 * 13 * 17 * 19

print(answer)
