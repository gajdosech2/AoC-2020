
numbers = []

with open("day9.txt") as day_file:
    line = day_file.readline().strip()
    
    while line:
        numbers.append(int(line))
        line = day_file.readline().strip()



def issum(number, partnumbers):
    for i in range(len(partnumbers)):
        for j in range(i):
            if partnumbers[i] + partnumbers[j] == number:
                return True

    return False

final = 0
for i in range(25, len(numbers)-1):
    partnumbers = numbers[(i-25) : i]
    num = numbers[i]
    res = issum(num, partnumbers)
    if res == False:
        final = num
        break
    
print(final)

def minmax(rangenum):
    minimal = min(rangenum)
    maximal = max(rangenum)
    return minimal + maximal

found = False
i = 0
print(len(numbers))
while i < len(numbers) and found == False:        
    rangenum = [numbers[i]]
    j = i + 1
    while j < len(numbers):
        rangenum.append(numbers[j])
        total = sum(rangenum)
        if total == final:
            print(minmax(rangenum))
            found = True
            break
        if total > final:
            break
        j = j + 1

    i = i + 1




    




