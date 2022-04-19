#Parte 1: Alexandro
class Node:
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))

#Parte 2: Carlos

class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

#Parte 3: Harold
# A* search
def astar_search(graph, heuristics, start, end):

    open = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)

    while len(open) > 0:

        open.sort()

        current_node = open.pop(0)

        closed.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Return reversed path
            return path[::-1]

        #Cristopher

        neighbors = graph.get(current_node.name)

        for key, value in neighbors.items():

            neighbor = Node(key, current_node)

            if(neighbor in closed):
                continue
            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            if(add_to_open(open, neighbor) == True):

                open.append(neighbor)
    return None

def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

#Hansel
def main():
    # Create a graph
    graph = Graph()
    # Create graph connections (Actual distance)
    graph.connect('Azua', 'Bahoruco', 12)
    graph.connect('Azua', 'San Juan', 9)
    graph.connect('Bahoruco', 'Sánchez Ramírez', 4)
    graph.connect('Bahoruco', 'Valverde', 4)
    graph.connect('San Juan', 'Puerto Plata', 7)
    graph.connect('San Juan', 'Pedernales', 14)
    graph.connect('Sánchez Ramírez', 'Valverde', 6)
    graph.connect('Sánchez Ramírez', 'San Pedro de Macorís', 8)
    graph.connect('Valverde', 'San Pedro de Macorís', 6)
    graph.connect('Valverde', 'Monte Plata', 8)
    graph.connect('Puerto Plata', 'Pedernales', 11)

    graph.make_undirected()
    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['Monte Plata'] = 6
    heuristics['Sánchez Ramírez'] = 0
    heuristics['Azua'] = 5
    heuristics['Bahoruco'] = 11
    heuristics['San Juan'] = 5
    heuristics['Valverde'] = 6
    heuristics['Puerto Plata'] = 11
    heuristics['San Pedro de Macorís'] = 5
    # Run the search algorithm
    path = astar_search(graph, heuristics, 'Valverde', 'San Pedro de Macorís')
    print(path)
    print()
# Tell python to run main method
if __name__ == "__main__": main()
