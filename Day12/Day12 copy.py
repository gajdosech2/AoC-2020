import copy

ew = 0
ns = 0
current_dir = 0 #E


with open("day12.txt") as day_file:
    line = day_file.readline().strip()
    
    while line:
        direction = line[0]
        amount = int(line[1:])
        if direction == "N":
            ns += amount
        elif direction == "S":
            ns -= amount
        elif direction == "E":
            ew += amount
        elif direction == "W":
            ew -= amount
        elif direction == "L":
            for i in range(amount//90):
                current_dir -= 1
                if current_dir < 0:
                    current_dir = 3
                    
        elif direction == "R":
            for i in range(amount//90):
                current_dir += 1
                if current_dir > 3:
                    current_dir = 0
                    
        elif direction == "F":
            if current_dir == 0:
                ew += amount
            elif current_dir == 1:
                ns -= amount
            elif current_dir == 2:
                ew -= amount
            elif current_dir == 3:
                ns += amount

        #print("NS: " + str(ns))
        #print("EW: " + str(ew))
        line = day_file.readline().strip()



print("NS: " + str(ns))
print("EW: " + str(ew))
print(abs(ns) + abs(ew))



    




