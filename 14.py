# if n is even n > n / 2
# if n is odd n -> 3n + 1

#if we use 13 as a start: 13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

# there is no proof but we believe all sequences end at 1

# find the longest sequence starting with a number under 1000000

def even(number):
    newNumber = number / 2
    return newNumber


def odd(number):
    newNumber = (3 * number) + 1
    return newNumber

term = 13
terms = []
terms.append(term)

while term != 1:
    if term % 2 == 0:
        newTerm = even(term)
        terms.append(newTerm)
        term = newTerm
    else:
        newTerm = odd(term)
        terms.append(newTerm)
        term = newTerm

print(terms, len(terms))

