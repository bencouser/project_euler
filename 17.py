small = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def words(n):
    if 0 <= n < 20:
        return small[n]
    elif 20 <= n < 100:
        return tens[n // 10] + (small[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return small[n // 100] + "hundred" + (("and" + words(n % 100)) if (n % 100 != 0) else "")
    elif n == 1000:
        return "onethousand"

sum = 0
for i in range(1, 1001):
    sum += len(words(i))

print(sum)

