import math
# function to efficiently get all factors
def getFactors(number):
    half_factors = []
    factors = []
    for potentialFactor in range(1, int(math.sqrt(number)) + 1):
        if number % potentialFactor == 0:
            half_factors.append(potentialFactor)
    size = len(half_factors)
    for i in range(size):
        factors.append(half_factors[i])
    for factor in range(size):
        fact = number / half_factors[factor]
        if fact in factors:
            pass
        else:
            factors.append(fact)
    return factors

abundantNumbers = []
numbers = {}
for i in range(1,28124):
    numbers[i] = i

for i in range(1,28124):
    if (sum(getFactors(i))-i) > i:
        abundantNumbers.append(i)
    else:
        pass

for abNumberA in abundantNumbers:
    for abNumberB in abundantNumbers:
        total = abNumberA + abNumberB
        if total in numbers:
            numbers.pop(total)

print(sum(numbers))
