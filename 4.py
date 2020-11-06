# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# 999 * 999 = 998001


def digits(number):
        digit = [int(x) for x in str(number)]
        return digit
        
def is_it_palindromic(number):
        digit = digits(number)
        originalDigits = digit
        digit.reverse()
        reverseDigit = digit
        return originalDigits == reverseDigit 

is_it_palindromic(9009)

largest_palindromic = 0

for i in range(101, 1000):
        for j in range(101, 1000):
                possible_pal = i * j
                if is_it_palindromic(possible_pal) and possible_pal > largest_palindromic:
                        largest_palindromic = possible_pal

print(largest_palindromic)
