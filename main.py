class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, start_vertex):
        distances = [float('inf')] * self.V
        distances[start_vertex] = 0

        # Основной цикл алгоритма
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Граф содержит отрицательный цикл")

        return distances

g = Graph(4)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, -2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)

start_vertex = 0
try:
    distances = g.bellman_ford(start_vertex)
    print(f"Расстояния от вершины {start_vertex}: {distances}")
except ValueError as e:
    print(e)