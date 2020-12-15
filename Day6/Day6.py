

counts = []
group = []

with open("day6.txt") as day_file:

    group = []
    line = day_file.readline()
    
    while line:
        #print(line)
        if len(line) == 1:
            counts.append(len(set.intersection(*group)))
            group = []
        else:
            group.append(set(line.strip()))
        line = day_file.readline()

    counts.append(len(set.intersection(*group)))

print(sum(counts))

    




