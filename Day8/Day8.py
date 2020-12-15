import copy

commands = []

with open("day8.txt") as day_file:
    line = day_file.readline().strip()
    
    while line:
        command, argument = line.split(" ")
        commands.append([command, argument])
        line = day_file.readline().strip()


def change(commands):
    og = copy.deepcopy(commands)
    for i in range(len(og)):
        copya = copy.deepcopy(og)
        if og[i][0] == "nop":
            copya[i][0] = "jmp"
        elif og[i][0] == "jmp":
            copya[i][0] = "nop"

        if og[i][0] == "nop" or og[i][0] == "jmp":
            res, c = execute(copya)
            if res:
                print(c)
                return

def execute(commands):
    executed_lines = []
    current = 0
    global_counter = 0

    success = False
    
    while True:
        if current == len(commands):
            success = True
            break

        if current in executed_lines:
            break
        
        current_command, argument = commands[current]
        executed_lines.append(current)
          
        if current_command == "nop":
            current += 1

        elif current_command == "acc":
            current += 1
            if argument[0] == "-":
                global_counter -= int(argument[1:])
            else:
                global_counter += int(argument[1:])

        elif current_command == "jmp":
            if argument[0] == "-":
                current -= int(argument[1:])
            else:
                current += int(argument[1:])


    return success, global_counter

change(commands)



    




