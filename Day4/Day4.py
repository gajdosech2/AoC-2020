
valids = 0
passport = ""
passports = []
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
present = [0, 0, 0, 0, 0, 0, 0]

with open("day4.txt") as day_file:
    line = day_file.readline().strip()
    while True:
        try:
            if line == "":
                dictionary = {}
                for field in passport.split(","):
                    key, value = field.split(":")
                    dictionary[key] = value

                    valid_field = True
                    if key == "byr":
                        if len(value) != 4:
                            valid_field = False
                        else:
                            try:
                                number = int(value)
                                if number < 1920 or number > 2002:
                                    valid_field = False
                            except:
                                valid_field = False
                        
                    elif key == "iyr":
                        if len(value) != 4:
                            valid_field = False
                        else:
                            try:
                                number = int(value)
                                if number < 2010 or number > 2020:
                                    valid_field = False
                            except:
                                valid_field = False
                                
                    elif key == "eyr":
                        if len(value) != 4:
                            valid_field = False
                        else:
                            try:
                                number = int(value)
                                if number < 2020 or number > 2030:
                                    valid_field = False
                            except:
                                valid_field = False
                    
                    elif key == "hgt":
                        try:
                            if value[-2:] == "cm":
                                number = int(value[:-2])
                                if number < 150 or number > 193:
                                    valid_field = False
                                
                            elif value[-2:] == "in":
                                number = int(value[:-2])
                                if number < 59 or number > 76:
                                    valid_field = False
                            else:
                                valid_field = False
                        except:
                            valid_field = False
                        
                    elif key == "hcl":
                        try:
                            if value[0] != "#":
                                valid_field = False
                            else:
                                if len(value[1:]) != 6:
                                    valid_field = False
                                else:
                                    for c in value[1:]:
                                        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] and c not in "abcdef":
                                            valid_field = False
                                            break
                        except:
                            valid_field = False
                            
                    elif key == "ecl":
                        if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                            valid_field = False

                    elif key == "pid":
                        try:
                            if len(value) != 9:
                                valid_field = False
                            else:
                                number = int(value)
                        except:
                            valid_field = False
                    
                    if key in required and valid_field:
                        present[required.index(key)] = 1
                
                passports.append(dictionary)
                if sum(present) == len(required):
                    valids += 1
                
                passport = ""
                present = [0, 0, 0, 0, 0, 0, 0]

            else:
                if passport != "":
                    passport += ","
                passport += ",".join(line.split(" "))   

            line = day_file.readline().strip()
        except:
            break

print(valids)

