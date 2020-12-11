# starting at 1 and moving right and out in a clockwise direction gives the form #seewebsite
# the sum of the diagonals is 101

# what is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed by the same
# way

# top right corner of square is always the dimension of the square, squared
# 1 = 1**2, 9 = 3**2, 25 = 5**2
# we can work out other corners from this fact and knowing the dimensions

sum = 1

size = 1001

for i in range(3, size+1, 2):
    for j in range(4):
        sum += (i**2) - j*(i-1)

print(sum)
