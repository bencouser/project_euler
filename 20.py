import math

number = math.factorial(100)

def digits(number):
    digit = [int(x) for x in str(number)]
    return digit

print(sum(digits(number)))
