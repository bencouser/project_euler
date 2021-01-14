# 49/98 = 4/8 and it looks as if the 9's cancel.
# Consider 30/50 = 3/5 to be a trivial solution

# There are 4 non-trivial cases, where its value is less than 1,
# and containing two digits in the numerator and denominator

# If the produc of these four fractions is given in its lowest common terms,
# find the value of the denominator

# note: All numbers can be written as number = n_10 + n_1

import MyModule as mm

count = 0

numerators = []
denominators = []

for denominator in range(10, 100):
    for numerator in range(10, denominator): # we want it to be less than one
        digits_num = mm.find_digits(numerator)
        digits_dom = mm.find_digits(denominator)
        if (digits_num[0] == digits_dom[1] and digits_num[1] * denominator == numerator * digits_dom[0]) or (digits_num[1] == digits_dom[0] and digits_num[0] * denominator == numerator * digits_dom[1]):
            numerators.append(numerator)
            denominators.append(denominator)

for i in range(len(numerators)):
    print(numerators[i] / denominators[i])


