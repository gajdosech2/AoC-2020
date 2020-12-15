import copy


memory = dict()
mask = ""

def write_mem(mem, index, value):
    #print("index: " + str(index))
    #print("value: " + str(value))
    #print("mask: " + mask)
    
    binary_val = list('{:036b}'.format(value))
    #print("binary: " + str(binary_val))
    for i in range(36):
        if mask[36 - i - 1] == "1":
            binary_val[36 - i - 1] = "1"
        elif mask[36 - i - 1] == "0":
            binary_val[36 - i - 1] = "0"
            
    #print("binary: " + str(binary_val))

    mem[index] = int("".join(binary_val), 2)

def write_mem2(mem, index, value):   
    binary_index = list('{:036b}'.format(index))
    num_xes = 0
    ind_xes = []

    for i in range(36):
        if mask[36 - i - 1] == "1":
            binary_index[36 - i - 1] = "1"
        elif mask[36 - i - 1] == "X":
            num_xes += 1
            ind_xes.append(i)
            binary_index[36 - i - 1] = "X"

    binaries = []
    max_bin = int("0b" + (num_xes * "1"), 2)
    bin_len = len(bin(max_bin)) - 2
    for i in range(max_bin + 1):
        binaries.append(('{:0' + str(bin_len) + 'b}').format(i))

    indices = []
    for i in range(len(binaries)):
        bin_vals = binaries[i]
        new_mask = copy.deepcopy(binary_index)
        for j in range(len(ind_xes)):
            new_mask[36 - ind_xes[j] - 1] = bin_vals[len(bin_vals) - j - 1]
        indices.append(new_mask)
        
    for new_indexos in indices:
        int_index = int("".join(new_indexos), 2)
        mem[int_index] = value
            

with open("day14.txt") as day_file:
    line = day_file.readline().strip()

    while line:
        pos, value = line.split(" = ")

        if pos == "mask":
            mask = value
        else:
            mem, index = pos.split("[")
            index = index[:-1]
            index = int(index)
            value = int(value)
    
            write_mem2(memory, index, value)
         
        line = day_file.readline().strip()


print(sum(list(memory.values())))


    




