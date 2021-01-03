# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112...

# It can be seen that the 12th term is a 1

# is d_n is the nth digit then find:
# d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000

# Note: this is an example of a non-computable number

import MyModule as mm

nonComputable = []
count = 0

while len(nonComputable) < 1000002:
    digits = mm.find_digits(count)
    nonComputable = nonComputable + digits
    count += 1

product = 1

for i in range(7):
    term = 10**i
    product *= nonComputable[term]

print(product)
