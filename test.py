from main import Graph

import unittest
class TestGraph(unittest.TestCase):
    def test_no_edges(self):
        g = Graph(5)
        distances = g.bellman_ford(0)
        self.assertEqual(distances, [0, float('inf'), float('inf'), float('inf'), float('inf')])

    def test_positive_weights(self):
        g = Graph(4)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 3, 1)

        distances = g.bellman_ford(0)
        self.assertEqual(distances, [0, 1, 3, 2])

    def test_negative_weights(self):
        g = Graph(4)
        g.add_edge(0, 1, -1)
        g.add_edge(0, 2, 1)
        g.add_edge(2, 1, -2)
        g.add_edge(1, 3, 1)
        g.add_edge(2, 3, 5)

        distances = g.bellman_ford(0)
        self.assertEqual(distances, [0, -1, 1, 0])

    def test_negative_cycle(self):
        g = Graph(4)
        g.add_edge(0, 1, -1)
        g.add_edge(1, 2, -1)
        g.add_edge(2, 0, -1)

        with self.assertRaises(ValueError) as context:
            g.bellman_ford(0)

        self.assertEqual(str(context.exception), "Граф содержит отрицательный цикл")