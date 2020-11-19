# on a 2 x 2 grind starting at the top left, there are 6 routes to travel by only going right or down to the bottom right corner

# how many routes are there for a 20 x 20 grid

# note: in 2x2 the length of the route is always 4 as we need to move 2 right and 2 bottom regardless
#       there are 3*2 routes 3!

x = 1

for i in range(1,20):
    x *= i

print(x)
