import copy

starting_numbers = [0,8,15,2,12,1,4]
#starting_numbers = [0,3,6]
#spoken = []

turn = 1

dict_spoken = dict()
last_number = None

while turn <= 30000000:
    if turn % 1000000 == 0:
        print(turn / 30000000)

    if turn <= len(starting_numbers):
        index = turn - 1
        #spoken.append(starting_numbers[index])
        dict_spoken[starting_numbers[index]] = [turn]
        last_number = starting_numbers[index]
    else:
        #last_number = spoken[-1]
        if len(dict_spoken[last_number]) == 1:
            if 0 not in dict_spoken.keys():
                dict_spoken[0] = [turn]
            else:
                dict_spoken[0].append(turn)
            last_number = 0
        else:
            #previous_index = spoken[:-1][::-1].index(last_number)
            #previous_index = len(spoken) - previous_index - 1
            previous_index = dict_spoken[last_number][-2]
            #spoken.append((turn-1) - previous_index)
            new_num = (turn-1) - previous_index
            if new_num not in dict_spoken.keys():
                dict_spoken[new_num] = [turn]
            else:
                dict_spoken[new_num].append(turn)
            last_number = new_num

    turn += 1

print(last_number)

#with open("day15.txt") as day_file:
#    line = day_file.readline().strip()

#    while line:
         
#        line = day_file.readline().strip()




    




