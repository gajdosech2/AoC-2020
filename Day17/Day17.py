import copy


def enlarge(cubes):
    new_size = len(cubes) + 2
    new_cubes = [[[['.' for _ in range(new_size)] for _ in range(new_size)] for _ in range(new_size)] for _ in range(new_size)]
    for i in range(len(cubes)):
        for j in range(len(cubes)):
            for k in range(len(cubes)):
                for l in range(len(cubes)):
                    new_cubes[i+1][j+1][k+1][l+1] = cubes[i][j][k][l]

    return new_cubes

cubes = []
with open("day17.txt") as day_file:
    line = day_file.readline().strip()
    size = len(line)
    cubes = [[[['.' for _ in range(size)] for _ in range(size)] for _ in range(size)] for _ in range(size)]
    z = size // 2
    w = size // 2
    i = 0
    while line:
        for j in range(size):
            cubes[i][j][z][w] = line[j]
        line = day_file.readline().strip()
        i += 1

size = len(cubes)
print(size)


def neighbors(i, j, k, l,  cubes):
    num = 0
    size = len(cubes)
    for o_i in [-1, 0, 1]:
        for o_j in [-1, 0, 1]:
            for o_k in [-1, 0, 1]:
                for o_l in [-1, 0, 1]:
                    if o_i == 0 and o_j == 0 and o_k == 0 and o_l == 0:
                        continue
                    n_i = i + o_i
                    n_j = j + o_j
                    n_k = k + o_k
                    n_l = l + o_l
                    if 0 <= n_i < size and 0 <= n_j < size and 0 <= n_k < size and 0 <= n_l < size and cubes[n_i][n_j][n_k][n_l] == "#":
                        num += 1
    return num


for c in range(6):
    cubes = enlarge(cubes)
    size = len(cubes)

    new_cubes = copy.deepcopy(cubes)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                for l in range(size):
                    num = neighbors(i, j, k, l, cubes)
                    if cubes[i][j][k][l] == "#":
                        if num != 2 and num != 3:
                            new_cubes[i][j][k][l] = "."
                    elif cubes[i][j][k][l] == ".":
                        if num == 3:
                            new_cubes[i][j][k][l] = "#"

    cubes = new_cubes


size = len(cubes)

num = 0
for i in range(size):
    for j in range(size):
        for k in range(size):
            for l in range(size):
                if cubes[i][j][k][l] == "#":
                    num += 1

print(num)