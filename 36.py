# Find the sum of all numbers under one million that are palindromic in both
# bases 10 and 2 (binary)

import MyModule as mm

sum = 0

for baseTen in range(0,1000000):
    if mm.is_it_palindromic(baseTen):
        binaryString = bin(baseTen)[2:]
        if binaryString == binaryString[::-1]:
            sum += baseTen

print(sum)
