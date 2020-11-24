months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0
sundays = 0

for year in range(1901, 2001):
    for m in range(len(months)):
        day += months[m]
        if year % 4 == 0 and m == months[1]:
            day += 1
        if day % 7 == 0:
            sundays += 1

print(sundays)
