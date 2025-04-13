import sys

class DistanceVector:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.INF = sys.maxsize
        self.graph = [[self.INF for _ in range(num_nodes)] for _ in range(num_nodes)]
        self.next_hop = [[-1 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight
        self.next_hop[u][v] = v
        self.next_hop[v][u] = u

    def print_routing_table(self):
        print("Routing Table:")
        for i in range(self.num_nodes):
            print(f"Node {i}: ", end="")
            for j in range(self.num_nodes):
                if self.graph[i][j] != self.INF:
                    print(f"({j}, {self.graph[i][j]})", end=" ")
            print()

    def calculate_shortest_path(self, src, dest):
        distance = [self.INF] * self.num_nodes
        distance[src] = 0

        for _ in range(self.num_nodes - 1):
            for u in range(self.num_nodes):
                for v in range(self.num_nodes):
                    if self.graph[u][v] != self.INF and distance[u] + self.graph[u][v] < distance[v]:
                        distance[v] = distance[u] + self.graph[u][v]

        shortest_path = [dest]
        while dest != src:
            dest = self.next_hop[src][dest]
            shortest_path.append(dest)
        shortest_path.reverse()

        return shortest_path, distance[dest]

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))
    dv = DistanceVector(num_nodes)

    print("Enter the distance matrix:")
    for i in range(num_nodes):
        for j in range(num_nodes):
            weight = int(input(f"Enter the weight between nodes {i} and {j}: "))
            if weight != 0:
                dv.add_edge(i, j, weight)

    dv.print_routing_table()

    src = int(input("Enter the source node: "))
    dest = int(input("Enter the destination node: "))

    shortest_path, cost = dv.calculate_shortest_path(src, dest)
    print(f"Shortest path from node {src} to node {dest}: {' -> '.join(map(str, shortest_path))}")
    print(f"Cost: {cost}")
