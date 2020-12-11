# find the sum of all the numbers that can be written as the sum of fifth powers of their digits

def digits(number):
    digit = [int(x) for x in str(number)]
    return digit

fourPowerNumbers = []

for i in range(2,10001):
    numberDigits = digits(i)
    powered = []
    powered = [x**4 for x in numberDigits]
    if sum(powered) == i:
        fourPowerNumbers.append(i)

print(fourPowerNumbers, sum(fourPowerNumbers))
