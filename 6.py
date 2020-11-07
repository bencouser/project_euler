# The sum of the squares of the first ten natural numbers is, 1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)**2 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_of_squares(N):
        squares = []
        for i in range(N+1):
                square = i**2
                squares.append(square)
        return sum(squares)

def square_of_sum(N):
        numbers = []
        for i in range(N+1):
                numbers.append(i)
        summ = sum(numbers)
        return summ**2

sumOfSquares = sum_of_squares(100)

squareOfSums = square_of_sum(100)

difference = squareOfSums - sumOfSquares

print(difference)
