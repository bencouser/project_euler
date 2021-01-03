# 49/98 = 4/8 and it looks as if the 9's cancel.
# Consider 30/50 = 3/5 to be a trivial solution

# There are 4 non-trivial cases, where its value is less than 1,
# and containing two digits in the numerator and denominator

# If the produc of these four fractions is given in its lowest common terms,
# find the value of the denominator

import MyModule as mm

count = 0

numerators = []
denominators = []

for numeratorCount in range(40, 1000):
    if numeratorCount % 10 == 0:
        pass
    else:
        for denominatorCount in range(80, 1000):
                digitsNum = mm.find_digits(numeratorCount)
                digitsDom = mm.find_digits(denominatorCount)
                for digit in digitsNum:
                    if digit in digitsDom:
                        digitsNum.remove(digit)
                        digitsDom.remove(digit)
                if len(digitsNum) == 1 and len(digitsDom) == 1 and digitsDom[0] != 0:
                    if numeratorCount / denominatorCount == digitsNum[0] / digitsDom[0]:
                        numerators.append(numeratorCount)
                        denominators.append(denominatorCount)
    

print(numerators, denominators)
