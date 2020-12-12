#!/usr/bin/env python3
import unittest

def arcToMat(ListeArc):
    Poids = dict()
    for arc in ListeArc:
        Poids[arc[0], arc[1]] = arc[2]

    return Poids

def inverse(Graphe):
    GrapheInv = dict()
    for sommet in Graphe:
        GrapheInv[sommet] = []

    for sommet in Graphe:
        for successeur in Graphe[sommet]:
            GrapheInv[successeur].append(sommet)

    return GrapheInv

def degreE(Graphe):
    Deg = dict()
    GrapheInv = inverse(Graphe)
    for sommet in GrapheInv:
        Deg[sommet] = len(GrapheInv[sommet])

    return Deg

def triTopo(Graphe):
    listeTri = []
    degreEntrant = degreE(Graphe)


    return listeTri

def plusTot(Graphe, GrapheInv, Poids, TriTopo):
    PlusTot = dict()
    return PlusTot

def critique(Graphe, GrapheInv, Poids, TriTopo):
    lol = True
    return lol

def plusTard(Graphe, GrapheInv, Poids, TriTopo):
    PlusTard = dict()
    return PlusTard

def marges(Graphe, Ptot, Ptard):
    marges = dict()
    return marges

class GrapheTest(unittest.TestCase):

    def setUp(self):

        self.G = {1: [2, 3, 5], 2: [4, 5], 3: [5, 6],
                  4: [7], 5: [7, 8], 6: [8, 9],
                  7: [10], 8: [10, 11, 12], 9: [11],
                  10: [12], 11: [12], 12: []}

        self.ListArcs = [[1, 2, 3], [1, 3, 2], [1, 5, 9], [2, 4, 2],
                         [2, 5, 4], [3, 5, 6], [3, 6, 9], [4, 7, 3],
                         [5, 7, 1], [5, 8, 2], [6, 8, 1], [6, 9, 2],
                         [7, 10, 5], [8, 10, 5], [8, 11, 6], [8, 12, 9],
                         [9, 11, 2], [10, 12, 5], [11, 12, 3]]

        self.Ginv = {
            1: [], 2: [1], 3: [1],
            4: [2], 5: [1, 2, 3], 6: [3],
            7: [4, 5], 8: [5, 6], 9: [6],
            10: [7, 8], 11: [8, 9], 12: [8, 10, 11]}

        self.Gtopo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def testArcToMat(self):
        M = arcToMat(self.ListArcs)
        self.assertEqual(M[(1, 2)], 3)
        self.assertEqual(M[(1, 3)], 2)
        self.assertEqual(M[(1, 5)], 9)
        self.assertEqual(M[(11, 12)], 3)
        self.assertFalse((1, 1) in M)

    def testInverse(self):
        G1 = {1: [2, 3], 2: [], 3: []}
        self.assertEqual(inverse(G1), {1: [], 2: [1], 3: [1]})
        G2 = {1: [2], 2: [3], 3: [1]}
        self.assertEqual(inverse(G2), {1: [3], 2: [1], 3: [2]})
        self.assertEqual(inverse(self.G), self.Ginv)

    def testDegreE(self):
        G1 = {1: [2, 4], 2: [1, 4], 3: [4], 4: [2]}
        self.assertEqual(degreE(G1), {1: 1, 2: 2, 3: 0, 4: 3})
        self.assertEqual(
            degreE(self.G),
            {1: 0, 2: 1, 3: 1, 4: 1, 5: 3, 6: 1, 7: 2, 8: 2, 9: 1, 10: 2, 11: 2, 12: 3}
        )

    def testTriTopo(self):
        T = triTopo(self.G)
        self.assertEqual(T, self.Gtopo)

    def testTriTopoCycle(self):
        cyclique = {1: [2], 2: [3], 3: [4], 4: [2]}
        try:
            triTopo(cyclique)
        except RuntimeError:
            return
        self.fail('Graphe cyclique non détecté')

    def testPlusTot(self):
        M = arcToMat(self.ListArcs)
        PlusTot = plusTot(self.G, self.Ginv, M, self.Gtopo)
        self.assertEqual(PlusTot, {1: 0, 2: 3, 3: 2, 4: 5, 5: 9, 6: 11, 7: 10, 8: 12, 9: 13, 10: 17, 11: 18, 12: 22})

    def testCritique(self):
        M = arcToMat(self.ListArcs)
        chemin, duree = critique(self.G, self.Ginv, M, self.Gtopo)
        self.assertEqual(chemin, [1, 3, 6, 8, 10, 12])
        self.assertEqual(duree, 22)

    def testPlusTard(self):
        M = arcToMat(self.ListArcs)
        PlusTard = plusTard(self.G, self.Ginv, M, self.Gtopo)
        self.assertEqual(PlusTard, {1: 0, 2: 6, 3: 2, 4: 9, 5: 10, 6: 11, 7: 12, 8: 12, 9: 17, 10: 17, 11: 19, 12: 22})

    def testMarges(self):
        Ptot = {1: 0, 2: 3, 3: 2, 4: 5, 5: 9, 6: 11, 7: 10, 8: 12, 9: 13, 10: 17, 11: 18, 12: 22}
        Ptard = {1: 0, 2: 6, 3: 2, 4: 9, 5: 10, 6: 11, 7: 12, 8: 12, 9: 17, 10: 17, 11: 19, 12: 22}
        self.assertEqual(marges(self.G, Ptot, Ptard),
                         {1: 0, 2: 3, 3: 0, 4: 4, 5: 1, 6: 0, 7: 2, 8: 0, 9: 4, 10: 0, 11: 1, 12: 0})

if __name__ == '__main__':
    unittest.main()
