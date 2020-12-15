
seats= []

def get_row(seat):
    interval = list(range(128))
    this = seat[:7]
    for letter in this:
        half = len(interval) // 2
        if letter == "F":
            interval = interval[:half]
        elif letter == "B":
            interval = interval[half:]
    return interval[0]

def get_col(seat):
    interval = list(range(8))
    this = seat[7:]
    for letter in this:
        half = len(interval) // 2
        if letter == "L":
            interval = interval[:half]
        elif letter == "R":
            interval = interval[half:]
    return interval[0]


maximal = 0

with open("day5.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        row = get_row(line)
        col = get_col(line)
        idecko = row * 8 + col
        maximal = max(maximal, idecko)
        seats.append(idecko)
        line = day_file.readline().strip()

#print(maximal)

vsetky = []
for row in range(128):
    for col in range(8):
        vsetky.append(row * 8 + col)

result = set(vsetky) - set(seats)

print(seats)
    




