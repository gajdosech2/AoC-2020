
valid = 0
with open("day2.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        count, letter, password = line.split(" ")

        first, second = count.split("-")
        letter = letter[:-1]

        count = 0

        if password[int(first)-1] == letter:
            count += 1

        if password[int(second)-1] == letter:
            count += 1
            
        #for l in password:
        #    if l == letter:
        #        count += 1

        if count == 1:
            valid += 1
            
        line = day_file.readline().strip()

print(valid)

