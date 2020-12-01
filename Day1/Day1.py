
array = []
with open("day1.txt") as day1_file:
    line = day1_file.readline().strip()
    while line:
        try:
            array.append(int(line))
        except:
            pass
        line = day1_file.readline().strip()

print(array)


flag = False
for i in range(len(array)):
    for j in range(len(array)):
        for k in range(len(array)):
            if i != j and j != k:
                if array[i] + array[j] + array[k] == 2020:
                    print(array[i] * array[j] * array[k])
                    flag = True
                    break
        if flag:
            break
    if flag:
        break
