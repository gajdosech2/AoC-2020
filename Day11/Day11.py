import copy

grid = []
with open("day11.txt") as day_file:
    line = day_file.readline().strip()
    
    while line:
        row = []
        for c in line:
            row.append(c)

        grid.append(row)
        line = day_file.readline().strip()


def neigh(grid, x, y):
    occupied = 0
    for o_x in [-1, 0, 1]:
        for o_y in [-1, 0, 1]:
            if o_x == 0 and o_y == 0:
                continue

            m_x = x + o_x
            m_y = y + o_y

            #print(str(m_x) + " , " + str(m_y), end=" ::: ")

            while m_x >= 0 and m_y >= 0 and m_x < len(grid[0]) and m_y < len(grid):
                if grid[m_y][m_x] == "#":
                    occupied += 1
                    break
                if grid[m_y][m_x] == "L":
                    break
                m_x = m_x + o_x
                m_y = m_y + o_y

            #print(occupied)
            
            #if m_x < 0 or m_y < 0 or m_x >= len(grid[0]) or m_y >= len(grid):
                #continue

    return occupied

            


def simulate(grid):
    change = True
    while change:

        new_grid = copy.deepcopy(grid)
        change = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                c = grid[i][j]
                #print(c, end="")
                if c == "L":
                    occ = neigh(grid, j, i)
                    if occ == 0:
                        new_grid[i][j] = "#"
                        change = True
                    
                elif c == "#":
                    occ = neigh(grid, j, i)
                    if occ >= 5:
                        new_grid[i][j] = "L"
                        change = True

            #print()
            
        #print()
        grid = new_grid


    occupied = 0
    for row in grid:
        for c in row:
            if c == "#":
                occupied += 1
    return occupied

print(simulate(grid))
#print(neigh(grid, 6, 0))



    




