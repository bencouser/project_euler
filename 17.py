small = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

hundredAnd = 10

N = 10

sum = 0

for i in range(1, N+1):
    if i < 10:
        number = small[i].split(",")
        sum += len(number)

    else:
        pass

print(sum)
