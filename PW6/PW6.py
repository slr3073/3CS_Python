import unittest
from PW1_Graphe_Represantations.tp1_partie1 import nbSommets, ajoutArete, enleveArete
from PW3_Search_Algorithms_Applications.tp3 import cyclicRec, isCyclic
import math

def areteToListe(ListeArr):
    Poids = dict()
    Graphe = dict()

    for arrete in ListeArr:
        Poids[(arrete[0], arrete[1])] = arrete[2]
        Poids[(arrete[1], arrete[0])] = arrete[2]

        if arrete[0] not in Graphe:
            Graphe[arrete[0]] = [arrete[1]]
        else:
            Graphe[arrete[0]].append(arrete[1])

        if arrete[1] not in Graphe:
            Graphe[arrete[1]] = [arrete[0]]
        else:
            Graphe[arrete[1]].append(arrete[0])

    return Graphe, Poids

def Kruskal(nbSommet, ListeArr):
    result = dict()
    poid = 0

    ListeArr = sorted(ListeArr, key=lambda x: x[2])

    while len(result) < nbSommet:
        arrete = ListeArr.pop(0)

        ajoutArete(result, arrete[0], arrete[1])
        if isCyclic(result):
            enleveArete(result, arrete[0], arrete[1])
        else:
            poid += arrete[2]

    return result, poid

def Prim(ListeArr):
    result = dict()
    Graphe, Poids = areteToListe(ListeArr)

    distance = dict()
    peres = dict()
    for i in range(1, len(Graphe) + 1):
        distance[i] = -1
        peres[i] = 1

    return result, 0

class GrapheTest(unittest.TestCase):

    def setUp(self):
        self.ListAretes = [[1, 2, 7], [1, 5, 6], [1, 6, 2], [2, 3, 4], [2, 5, 5], [3, 4, 1], [3, 5, 2], [4, 5, 3],
                           [5, 6, 1]]

        self.G6 = {1: [2, 5, 6], 2: [1, 3, 5], 3: [2, 4, 5], 4: [3, 5], 5: [1, 2, 3, 4, 6], 6: [1, 5]}
        self.G6mat = {
            (1, 2): 7, (1, 5): 6, (1, 6): 2, (2, 3): 4, (2, 5): 5,
            (3, 4): 1, (3, 5): 2, (4, 5): 3, (5, 6): 1,
            (2, 1): 7, (5, 1): 6, (3, 2): 4, (5, 2): 5, (4, 3): 1,
            (5, 3): 2, (5, 4): 3, (6, 1): 2, (6, 5): 1,
        }

    def testAreteToListe(self):
        (G, M) = areteToListe(self.ListAretes)
        self.assertEqual(G, self.G6)
        self.assertEqual(M, self.G6mat)

    def testKruskal(self):
        (T, poids) = Kruskal(6, self.ListAretes)
        self.assertEqual(T, {1: [6], 2: [3], 3: [4, 5, 2], 4: [3], 5: [6, 3], 6: [5, 1]})
        self.assertEqual(poids, 10)

    def testPrim(self):
        (T, poids) = Prim(self.ListAretes)
        self.assertEqual(T, {1: [6], 2: [3], 3: [5, 4, 2], 4: [3], 5: [6, 3], 6: [1, 5]})
        self.assertEqual(poids, 10)

if __name__ == '__main__':
    unittest.main()
