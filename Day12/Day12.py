import copy

ew = 0
ns = 0
#current_dir = 0 #E
wp_ew = 10
wp_ns = 1

with open("day12.txt") as day_file:
    line = day_file.readline().strip()
    
    while line:
        direction = line[0]
        amount = int(line[1:])
        
        if direction == "N":
            wp_ns += amount
        elif direction == "S":
            wp_ns -= amount
        elif direction == "E":
            wp_ew += amount
        elif direction == "W":
            wp_ew -= amount
            
        elif direction == "L":
            for i in range(amount//90):
                new_ns = 0
                new_ew = 0
                
                if wp_ns > 0:
                    new_ew = -wp_ns
                else:
                    new_ew = -wp_ns

                if wp_ew > 0:
                    new_ns = wp_ew
                else:
                    new_ns = wp_ew

                wp_ns = new_ns
                wp_ew = new_ew
                    
        elif direction == "R":
            for i in range(amount//90):
                new_ns = 0
                new_ew = 0
                
                if wp_ns > 0:
                    new_ew = wp_ns
                else:
                    new_ew = wp_ns

                if wp_ew > 0:
                    new_ns = -wp_ew
                else:
                    new_ns = -wp_ew

                wp_ns = new_ns
                wp_ew = new_ew
                
                    
        elif direction == "F":
            for i in range(amount):
                ew += wp_ew
                ns += wp_ns

        #print("NS: " + str(ns))
        #print("EW: " + str(ew))
        line = day_file.readline().strip()



print("NS: " + str(ns))
print("EW: " + str(ew))
print(abs(ns) + abs(ew))





    




