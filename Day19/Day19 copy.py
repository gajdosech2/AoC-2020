import copy
import sys

sys.setrecursionlimit(20000)
print(sys.getrecursionlimit())

rules = dict()
msgs = []

class Rule:
    def __init__(self, letter, subrules):
        self.letter = letter
        self.subrules = subrules

    def match(self, index, msg):
        if self.letter:
            if index < len(msg):
                return self.letter == msg[index], {index + 1}
            return False, set()

        flag = False
        offsets = set()
        for p in self.subrules:
            starts = {index}
            whole = True

            for r in p:
                temp = set()
                for loc in starts:
                    subres, lo = rules[r].match(loc, msg)
                    if subres:
                        temp = temp | lo
                starts = temp
                whole = whole and len(starts) > 0

            if whole:
                flag = True

            offsets = offsets | starts

        return flag, offsets

with open("day19.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        split1 = line.split(": ")
        num = int(split1[0])
        if split1[1][0] == '"':
            rules[num] = Rule(split1[1][1], [])

        else:
            split2 = split1[1].split(" | ")
            subrules = []
            for r in split2:
                subrules.append([int(i) for i in r.split(" ")])
            rules[num] = Rule(None, subrules)

        line = day_file.readline().strip()

    line = day_file.readline().strip()
    while line:
        msgs.append(line)
        line = day_file.readline().strip()


rules[8] = Rule(None, [[42], [42, 8]])
rules[11] = Rule(None, [[42, 31], [42, 11, 31]])

count = 0
for msg in msgs:
    res, length = rules[0].match(0, msg)

    if res and len(msg) in length:
        count += 1

print(count)


