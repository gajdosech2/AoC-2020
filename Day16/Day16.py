import copy


class Rule:
    def __init__(self, r1, r2, name):
        rule1 = r1.split("-")
        self.r1 = (int(rule1[0]), int(rule1[1]))
        rule2 = r2.split("-")
        self.r2 = (int(rule2[0]), int(rule2[1]))
        self.name = name

    def isFrom(self, value):
        return (value >= self.r1[0] and value <= self.r1[1]) or (value >= self.r2[0] and value <= self.r2[1])


error = 0
rules = []
tickets = []
your_ticket = None

names_p = []
with open("day16.txt") as day_file:
    mode = "rules"
    line = day_file.readline().strip()

    while line:
        if line == "your ticket:":
            mode = "your"
        elif line == "nearby tickets:":
            mode = "nearby"
        else:
            if mode == "rules":
                split1 = line.split(": ")
                if split1[0] not in names_p:
                    names_p.append(split1[0])
                split2 = split1[1].split(" or ")
                rules.append(Rule(split2[0], split2[1], split1[0]))
            elif mode == "nearby":
                values = line.split(",")
                values = [int(i) for i in values]

                invalid = False
                for v in values:
                    belongs = False
                    for rule in rules:
                        if rule.isFrom(v):
                            belongs = True
                            break
                    if belongs == False:
                        invalid = True
                        error += v

                if invalid == False:
                    tickets.append(values)

            elif mode == "your":
                values = line.split(",")
                values = [int(i) for i in values]
                your_ticket = values

        line = day_file.readline().strip()

print(error)
#print(names_p)

### PART-2 ####

possible = dict() #value position: [possible_rules]

for i in range(len(tickets[0])):
    vals = []
    possible_names = copy.deepcopy(names_p)
    for ticket in tickets:
        for rule in rules:
            if not rule.isFrom(ticket[i]):
                possible_names.remove(rule.name)
    print(len(possible_names))
    possible[i] = possible_names


possible_c = copy.deepcopy(possible)
given = dict() #value position: given_name

min_len = 1
while True:
    taken = None
    for i in range(len(tickets[0])):
        if len(possible_c[i]) == 1:
            given[i] = possible_c[i][0]
            taken = possible_c[i][0]
            break

    if taken == None:
        print("err")
        break

    new_possible = copy.deepcopy(possible_c)
    for i in possible_c.keys():
        if taken in possible_c[i]:
            new_possible[i].remove(taken)

    possible_c = new_possible

print(given)
print(your_ticket)

final = 1
count = 0
for i in given.keys():
    if "departure" in given[i]:
        count += 1
        final = final * your_ticket[i]

print(count)
print(final)

