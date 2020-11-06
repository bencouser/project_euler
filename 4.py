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
        if originalDigits == reverseDigit: 
                print(number, "is a Palindromic Number")
        else:
                print(number, "is not a Palindromic Number")


is_it_palindromic(9009)
