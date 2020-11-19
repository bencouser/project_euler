# if n is even n > n / 2
# if n is odd n -> 3n + 1

#if we use 13 as a start: 13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

# there is no proof but we believe all sequences end at 1

# find the longest sequence starting with a number under 1000000

# powers of 2 will be fastest route down

# we dont need to append first and last terms as they are in every list, also i assume it would be odd

def even(number):
    newNumber = number / 2
    return newNumber


def odd(number):
    newNumber = (3 * number) + 1
    return newNumber

largest_term = 0
largest_terms = []

for half_term in range(499999):
    term = (half_term * 2) + 1
    terms = []
    original_term = term
    while term != 1:
        if term % 2 == 0:
            newTerm = even(term)
            terms.append(newTerm)
            term = newTerm
        else:
            newTerm = odd(term)
            terms.append(newTerm)
            term = newTerm
    if len(terms) > len(largest_terms):
        largest_terms = terms
        largest_term = original_term



print(largest_term)

