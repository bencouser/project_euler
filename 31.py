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

for pennys in range(0,201):
    for twopennys in range(0,101):
        for fivepennys in range(0,41):
            for tenpennys in range(0, 21):
                for twentypennys in range(0, 11):
                    for fiftypennys in range(0, 5):
                        for onepound in range(0, 3):
                            if pennys*1 + twopennys*2 + fivepennys*5 + tenpennys*10 + twentypennys*20 + fiftypennys*50 + onepound*1 == 2:
                                count += 1

print(count)
