import copy


class Tile:
    def __init__(self, data, id):
        self.data = data
        self.id = id

    def all(self):
        configs = [self]

        for i in range(3):
            configs.append(configs[-1].rotate())

        configs.append(self.fliph())
        for i in range(3):
            configs.append(configs[-1].rotate())

        configs.append(self.flipv())
        for i in range(3):
            configs.append(configs[-1].rotate())

        return configs

    def rotate(self):
        new_data = list(zip(*self.data[::-1]))
        new_data = [list(c) for c in new_data]
        return Tile(new_data, self.id)

    def fliph(self):
        new_data = []
        for row in self.data:
            new_data.append(row[::-1])
        return Tile(new_data, self.id)

    def flipv(self):
        new_data = []
        for row_i in range(len(self.data)):
            new_data.append(copy.deepcopy(self.data[len(self.data)-row_i-1]))
        return Tile(new_data, self.id)

    def check_right_border(self, right_tile):
        for row in range(len(self.data)):
            if self.data[row][-1] != right_tile.data[row][0]:
                return False
        return True

    def check_bottom_border(self, bottom_tile):
        for col in range(len(self.data[0])):
            if self.data[-1][col] != bottom_tile.data[0][col]:
                return False
        return True


tiles = []
with open("day20.txt") as day_file:
    line = day_file.readline().strip()
    id = line[:-1][5:]
    while line:
        tile_data = []
        line = day_file.readline().strip()
        while line:
            tile_data.append(list(line))
            line = day_file.readline().strip()


        tiles.append(Tile(tile_data, id))
        line = day_file.readline().strip()
        id = line[:-1][5:]

print(len(tiles))
done = False
final_img = []


def assemble(img, used):
    global done, final_img

    if done:
        return
    if len(img) > 0 and len(used) == len(tiles)-1:
        done = True
        final_img = img
    for i in range(len(tiles)):
        if done:
            return

        if i not in used:
            new_used = copy.deepcopy(used)
            new_used.append(i)
            added = False

            all_configs = tiles[i].all()
            for config in all_configs: #next col
                if img[-1][-1].check_right_border(config):
                    new_img = copy.deepcopy(img)
                    new_img[-1].append(config)
                    assemble(new_img, new_used)
                    added = True

            if done or added:
                return

            for config in all_configs: #next row
                if img[-1][0].check_bottom_border(config):
                    new_img = copy.deepcopy(img)
                    new_img.append([config])
                    assemble(new_img, new_used)
                    added = True

            if done or added:
                return


for i in range(len(tiles)):
    print(i)
    configs = tiles[i].all()
    for config in configs:
        assemble([[config]], [i])
    if done and len(final_img) > 0:
        break

for i in range(len(final_img)):
    for j in range(len(final_img[i])):
        print(final_img[i][j].id, end=",")
    print()

