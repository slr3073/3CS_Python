import unittest
from collections import deque

def arcToListe(ListeArc: list):
    Graphe = dict()
    Poids = dict()

    for arc in ListeArc:
        if arc[0] in Graphe:
            Graphe[arc[0]].append(arc[1])
        else:
            Graphe[arc[0]] = [arc[1]]
        Poids[(arc[0], arc[1])] = arc[2]

    return Graphe, Poids

def Dijkstra(Graphe: dict, Poids: dict, Sommet: int):
    Distance = dict()
    Peres = dict()
    File = deque([Sommet])

    Peres[Sommet] = Sommet
    Distance[Sommet] = 0

    while File:
        sommet = File.popleft()
        for successeur in Graphe[sommet]:
            if successeur not in Peres or Poids[(sommet, successeur)] + Distance[sommet] < Distance[successeur]:
                File.append(successeur)
                Peres[successeur] = sommet
                Distance[successeur] = Poids[(sommet, successeur)] + Distance[sommet]

    return Distance, Peres

def arcToListe2(ListeArc: list):
    Pred = dict()
    Graphe = dict()
    Poids = dict()

    for arc in ListeArc:
        if arc[0] not in Graphe:
            Graphe[arc[0]] = [arc[1]]
        else:
            Graphe[arc[0]].append(arc[1])

        Poids[(arc[0], arc[1])] = arc[2]

        if arc[1] not in Pred:
            Pred[arc[1]] = [arc[0]]
        else:
            Graphe[arc[1]].append(arc[0])

        Poids[(arc[0], arc[1])] = arc[2]

    return Pred, Graphe, Poids

class GrapheTest(unittest.TestCase):

    def setUp(self):
        self.listArcs = [[1, 2, 10], [1, 3, 3], [1, 5, 6], [2, 1, 0], [3, 2, 4], [3, 5, 2], [4, 3, 1], [4, 5, 3],
                         [5, 2, 0], [5, 6, 1], [6, 1, 2], [6, 2, 1]]

    def testArcToListe(self):
        (G, M) = arcToListe(self.listArcs)
        self.assertEqual(G, {
            1: [2, 3, 5], 2: [1], 3: [2, 5],
            4: [3, 5], 5: [2, 6], 6: [1, 2]})
        self.assertEqual(M, {
            (1, 2): 10, (1, 3): 3, (1, 5): 6, (2, 1): 0,
            (3, 2): 4, (3, 5): 2, (4, 3): 1, (4, 5): 3,
            (5, 2): 0, (5, 6): 1, (6, 1): 2, (6, 2): 1})

    def testDijkstra(self):
        G, M = arcToListe(self.listArcs)
        dist, pere = Dijkstra(G, M, 1)
        self.assertEqual(pere, {1: 1, 2: 5, 3: 1, 5: 3, 6: 5})
        self.assertEqual(dist, {1: 0, 2: 5, 3: 3, 5: 5, 6: 6})

    def testDijkstra2(self):
        G, M = arcToListe(self.listArcs)
        dist, pere = Dijkstra(G, M, 4)
        self.assertEqual(pere, {4: 4, 3: 4, 5: 4, 2: 5, 6: 5, 1: 2})
        self.assertEqual(dist, {4: 0, 3: 1, 5: 3, 2: 3, 6: 4, 1: 3})

if __name__ == '__main__':
    unittest.main()
