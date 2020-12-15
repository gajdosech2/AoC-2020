
early_ts = 0
busses = []
schedule = []
with open("day13.txt") as day_file:
    line = day_file.readline().strip()
    early_ts = int(line)
    line = day_file.readline().strip() 
    busses = [int(i) for i in line.split(",") if i != "x"]
    schedule = line.split(",")

#########

from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
  
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

#########

#m_o = 99999999
#b_id = -1

#for bus in busses:
#    i = 1
#    while i * bus < early_ts:
#        i += 1

#    if i * bus < m_o:
#        m_o = i * bus
#        b_id = bus

#print((m_o - early_ts) * b_id)

#########

def brute(t = 100000000000000):
    holds = False
    print()
    print("BRUTE:")
    while not holds:
        if t % 1000000 == 0:
            print(t)
        t += 1
        holds = True
        for i, bus in enumerate(schedule):
            if bus != "x":
                time = int(bus)
                if (t + i) % time != 0:
                     holds = False
            if not holds:
                break
    return t

#########

n = []
a = []
for i, bus in enumerate(schedule):
    if bus != "x":
        n.append(int(bus))
        #a.append(int(bus)-i)
        a.append((-i) % int(bus))

print(chinese_remainder(n, a))
ans = 905694340256752
print(brute(ans-10000000))

