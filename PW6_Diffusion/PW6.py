import unittest
from PW1_Graphe_Represantations.PW1_P1 import ajoutArete, enleveArete
from PW3_Search_Algorithms_Applications.PW3 import isCyclic

def areteToListe(ListeArr: list):
    Poids = dict()
    Graphe = dict()

    for arrete in ListeArr:
        Poids[arrete[0], arrete[1]] = arrete[2]
        Poids[arrete[1], arrete[0]] = arrete[2]

        if arrete[0] not in Graphe:
            Graphe[arrete[0]] = [arrete[1]]
        else:
            Graphe[arrete[0]].append(arrete[1])

        if arrete[1] not in Graphe:
            Graphe[arrete[1]] = [arrete[0]]
        else:
            Graphe[arrete[1]].append(arrete[0])

    return Graphe, Poids

def Kruskal(nbSommet: int, ListeArr: list):
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

def minimise(Dist: dict):
    y = -1
    poidsMini = float('inf')
    for sommet in Dist:
        if Dist[sommet] != 0 and Dist[sommet] < poidsMini:
            y = sommet
            poidsMini = Dist[sommet]

    return y

def Prim(ListeArr: list):
    result = dict()
    poid = 0
    (Graphe, Poids) = areteToListe(ListeArr)
    nbArrete = 0
    Dist = dict()
    for sommet in Graphe:
        Dist[sommet] = float('inf')
    Dist[1] = 0

    Min = dict()
    for sommet in Graphe:
        Min[sommet] = 1

    for voisin in Graphe[1]:
        Dist[voisin] = Poids[(1, voisin)]

    while nbArrete < len(Graphe) - 1:
        sommetLePlusProche = minimise(Dist)
        entecedantSommetProche = Min[sommetLePlusProche]

        ajoutArete(result, entecedantSommetProche, sommetLePlusProche)
        nbArrete += 1
        poid += Poids[(entecedantSommetProche, sommetLePlusProche)]
        Dist[sommetLePlusProche] = 0

        for voisin in Graphe[sommetLePlusProche]:
            if Dist[voisin] > Poids[sommetLePlusProche, voisin]:
                Dist[voisin] = Poids[sommetLePlusProche, voisin]
                Min[voisin] = sommetLePlusProche

    return result, poid

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
