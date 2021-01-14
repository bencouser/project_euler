# 49/98 = 4/8 and it looks as if the 9's cancel.
# Consider 30/50 = 3/5 to be a trivial solution

# There are 4 non-trivial cases, where its value is less than 1,
# and containing two digits in the numerator and denominator

# If the produc of these four fractions is given in its lowest common terms,
# find the value of the denominator

import MyModule as mm

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

num = 1
dom = 1

for i in range(len(numerators)):
    num *= numerators[i]
    dom *= denominators[i]

print(num, "/", dom, "=",  num/dom) # num / dom is 0.01 so i tried 100 and it worked lol
