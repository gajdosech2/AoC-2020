from collections import Counter

jolts = []

with open("day10.txt") as day_file:
    line = day_file.readline().strip()
    
    while line:
        jolts.append(int(line))
        line = day_file.readline().strip()

#jolts.append(0)
jolts.sort()
jolts.append(jolts[-1] + 3)

#diff3 = 0
#diff1 = 0
#print(jolts)

#dp = Counter()

#print(jolts)

dp = [0 for _ in range(jolts[-1] + 1)]
dp[0] = 1
for jolt in jolts:
    dp[jolt] = dp[jolt - 1]
    if jolt - 2 >= 0:
        dp[jolt] += dp[jolt - 2]
    if jolt - 3 >= 0:
        dp[jolt] += dp[jolt - 3]

print(dp[jolts[-1]])
    
    
    

#print(diff1)
#print(diff3)
#print(diff1 * diff3)




    




