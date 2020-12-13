# find the sum of all the numbers that can be written as the sum of fifth powers of their digits

# in example case the solutions only went to 4 digits so i will guess for 5th powers
# they will go up to 5 digit (didnt work)s
# upper limit found by doing 9^5 * n and finding what value of n yielded a larger
# number than rhe digits of the results as after that point no more numbers would
# be possible

def digits(number):
    digit = [int(x) for x in str(number)]
    return digit

fourPowerNumbers = []

for i in range(2,413343):
    numberDigits = digits(i)
    powered = []
    powered = [x**5 for x in numberDigits]
    if sum(powered) == i:
        fourPowerNumbers.append(i)

print(fourPowerNumbers, sum(fourPowerNumbers))

