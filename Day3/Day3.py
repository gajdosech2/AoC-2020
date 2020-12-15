
mapa = list()
with open("day3.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        mapa.append(line)
        line = day_file.readline().strip()

width = len(mapa[0])
height = len(mapa)


y = 0
x = 0
count1 = 0
while y < height:
    if mapa[y][x % width] == '#':
        count1 += 1
    y += 1
    x += 1

y = 0
x = 0
count2 = 0
while y < height:
    if mapa[y][x % width] == '#':
        count2 += 1
    y += 1
    x += 3

y = 0
x = 0
count3 = 0
while y < height:
    if mapa[y][x % width] == '#':
        count3 += 1
    y += 1
    x += 5

y = 0
x = 0
count4 = 0
while y < height:
    if mapa[y][x % width] == '#':
        count4 += 1
    y += 1
    x += 7

y = 0
x = 0
count5 = 0
while y < height:
    if mapa[y][x % width] == '#':
        count5 += 1
    y += 2
    x += 1

  
print(count1 * count2 * count3 * count4 * count5)
