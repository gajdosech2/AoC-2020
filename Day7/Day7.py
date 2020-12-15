

class Node:
    def __init__(self):
        self.name = None
        self.parents = []
        self.childs = []

    def exclusive(self):
        exclusive_parents = []
        queue = [self]
        while queue:
            node = queue.pop()
            for p in node.parents:
                if p.name not in exclusive_parents:
                    exclusive_parents.append(p.name)
                    queue.append(p)
        return len(exclusive_parents)

    def count_childs(self):
        count = 0
        for child in self.childs:
            other, c = child
            count += c
            count += c * other.count_childs()
        return count
            

nodes = dict()
with open("day7.txt") as day_file:

    line = day_file.readline().strip()
    
    while line:
        this, rest = line.split("contain")
        node_name = " ".join(this.split(" ")[:-2])
        node = None

        if node_name in nodes.keys():
            node = nodes[node_name]
        else:  
            node = Node()
            node.name = node_name
            nodes[node_name] = node
            
        rest = rest[1:-1]

        if rest != "no other bags":
            for other in rest.split(","):
                other = other.strip()
                count, color1, color2, bag = other.split(" ")
                other_name = color1 + " " + color2

                other_node = None
                if other_name in nodes.keys():
                    other_node = nodes[other_name]
                else:
                    other_node = Node()
                    other_node.name = other_name
                    nodes[other_name] = other_node

                node.childs.append((other_node, int(count)))
                other_node.parents.append(node)
        
        line = day_file.readline().strip()

print(nodes["shiny gold"].exclusive())
print(nodes["shiny gold"].count_childs())




    




