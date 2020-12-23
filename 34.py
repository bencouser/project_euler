# Find the sum of all numbers which are equal to the sum of the factorial of 
# their digits

import MyModule as mm

totalSum = 0


for number in range(10, 1000000):
    digits = mm.find_digits(number)
    factorial_sum = 0
    for digit in digits:
        factorial_sum += mm.find_factorial(digit)
    if factorial_sum == number:
        totalSum += number

print(totalSum)
