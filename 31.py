# how many ways can you make 2 pounds

# 200 pennys = 2 pounds
# 100 2ps = ..
# 40 5ps = ..
# 20 10ps = ..
# 10 20ps = ..
# 4 50ps = ..
# 2 1pounds = ..
# suprisingly 2 pound = 2 pound

count = 1 # 2 pound
coinValues = [1, 2, 5, 10, 20, 50, 100]
currentTotal = 0
goal = 200

def combinations(count, coinValues, currentTotal, goal):
    for i in range(len(coinValues)):
        newTotal = currentTotal + coinValues[i]
        if newTotal == goal:
            count += 1
        elif newTotal > goal:
            return count
        else:
            count = combinations(count, coinValues[i:], newTotal, goal)
    return count

print(combinations(count, coinValues, currentTotal, goal))
