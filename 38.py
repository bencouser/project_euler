# If p is the parimeter of a right hand triangle with sides {a, b, c}. There are 3 
# solutions for p = 120
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}

# For which value of p <= 1000, is the number of solutions maximised

# Note: a**2 + b**2 = c**2
# Started at p = 500 as I didn't think it could be less than that

maxCount = 0
maxP = 0

for p in range(500,1001):
    count = 0
    for a in range(1, p-2):
        for b in range(a, p-1):
            if (a**2 + b**2)**(0.5) == p - a - b:
                count += 1
    if count > maxCount:
        maxCount = count
        maxP = p

print(maxP)
