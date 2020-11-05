#!/usr/bin/env python3
from collections import deque
from tp2_profondeur import *
import unittest

G1 = {1: [2], 2: [1, 3, 7], 3: [2], 4: [7], 5: [7], 6: [7], 7: [2, 4, 5, 6]}  # arbre
G2 = {1: [2, 4], 2: [1, 3, 7], 3: [2], 4: [1, 7], 5: [7], 6: [7], 7: [2, 4, 5, 6]}  # connexe cyclique
G3 = {1: [2], 2: [1, 3], 3: [2], 4: [7], 5: [7], 6: [7], 7: [4, 5, 6]}  # ni connexe ni cyclique
G4 = {1: [2], 2: [1, 3], 3: [2], 4: [5, 7], 5: [4, 7], 6: [7], 7: [4, 5, 6]}  # pas connexe cyclique


def nbSommets(G):
    return len(G) - 1


def isConnexe(G):
    return len(G) == len(profond(G, 1))


def cyclicRec(G, i, pere, Visite):
    Visite.add(i)

    for j in G[i]:
        if j not in Visite:
            if cyclicRec(G, j, i, Visite):
                return True
        elif j != pere:
            return True
    return False


def isCyclic(G):
    Visite = set()
    for s in G:
        if s not in Visite:
            if cyclicRec(G, s, s, Visite):
                return True
    return False


def isArbre(G):
    return (not isCyclic(G)) & isConnexe(G)


def plusCourtChemin(G, sommet):
    Dist = dict()
    Pere = dict()

    Visite = {sommet}
    File = deque()

    File.append(sommet)

    Dist[sommet] = 0
    Pere[sommet] = sommet

    while len(File) != 0:
        s = File[0]
        for succ in G[s]:
            if not succ in Visite:
                Visite.add(succ)
                File.append(succ)
                Dist[succ] = Dist[s] + 1
                Pere[succ] = s
        File.popleft()

    return Dist, Pere


def cyclicRecOriente(G, sommet, Visite):
    Visite[sommet] = 1  # La visite commence
    cycle = False
    for succ in G[sommet]:
        if cycle:
            return True
        if succ not in Visite:
            cycle = cyclicRecOriente(G, succ, Visite)
        elif Visite[succ] == 1:
            return True

    Visite[sommet] = 2
    return cycle


def isCyclicOriente(G):
    Visite = dict()
    for sommet in G:
        if cyclicRecOriente(G, sommet, Visite):
            return True

    return cyclicRecOriente(G, 1, Visite)


class GrapheTest(unittest.TestCase):

    def setUp(self):
        self.G1 = {1: [2], 2: [1, 3, 7], 3: [2], 4: [7], 5: [7], 6: [7], 7: [2, 4, 5, 6]}  # arbre
        self.G2 = {1: [2, 4], 2: [1, 3, 7], 3: [2], 4: [1, 7], 5: [7], 6: [7], 7: [2, 4, 5, 6]}  # connexe cyclique
        self.G3 = {1: [2], 2: [1, 3], 3: [2], 4: [7], 5: [7], 6: [7], 7: [4, 5, 6]}  # ni connexe ni cyclique
        self.G4 = {1: [2], 2: [1, 3], 3: [2], 4: [5, 7], 5: [4, 7], 6: [7], 7: [4, 5, 6]}  # pas connexe cyclique

    def testConnexe(self):
        self.assertTrue(isConnexe(self.G1))
        self.assertTrue(isConnexe(self.G2))
        self.assertFalse(isConnexe(self.G3))
        self.assertFalse(isConnexe(self.G4))

    def testCyclic(self):
        self.assertFalse(isCyclic(self.G1))
        self.assertTrue(isCyclic(self.G2))
        self.assertFalse(isCyclic(self.G3))
        self.assertTrue(isCyclic(self.G4))

    def testArbre(self):
        self.assertTrue(isArbre(self.G1))
        self.assertFalse(isArbre(self.G2))
        self.assertFalse(isArbre(self.G3))
        self.assertFalse(isArbre(self.G4))

    def testPlusCourtChemin(self):
        Dist, Pere = plusCourtChemin(self.G1, 1)
        self.assertEqual(Pere, {1: 1, 2: 1, 3: 2, 4: 7, 5: 7, 6: 7, 7: 2})
        self.assertEqual(Dist, {1: 0, 2: 1, 3: 2, 4: 3, 5: 3, 6: 3, 7: 2})
        Dist, Pere = plusCourtChemin(self.G1, 3)
        self.assertEqual(Pere, {1: 2, 2: 3, 3: 3, 4: 7, 5: 7, 6: 7, 7: 2})
        self.assertEqual(Dist, {1: 2, 2: 1, 3: 0, 4: 3, 5: 3, 6: 3, 7: 2})
        Dist, Pere = plusCourtChemin(self.G2, 1)
        self.assertEqual(Pere, {1: 1, 2: 1, 3: 2, 4: 1, 5: 7, 6: 7, 7: 2})
        self.assertEqual(Dist, {1: 0, 2: 1, 3: 2, 4: 1, 5: 3, 6: 3, 7: 2})
        Dist, Pere = plusCourtChemin(self.G4, 1)
        self.assertEqual(Pere, {1: 1, 2: 1, 3: 2})
        self.assertEqual(Dist, {1: 0, 2: 1, 3: 2})
        Dist, Pere = plusCourtChemin(self.G4, 5)
        self.assertEqual(Pere, {4: 5, 5: 5, 6: 7, 7: 5})
        self.assertEqual(Dist, {4: 1, 5: 0, 6: 2, 7: 1})

    def testIsCyclicOriente(self):
        self.assertTrue(isCyclicOriente({1: [3, 4, 5, 6], 2: [1], 3: [2, 4], 4: [], 5: [], 6: [4]}))
        self.assertFalse(isCyclicOriente({1: [4, 5, 6], 2: [1], 3: [2, 4], 4: [], 5: [], 6: [4]}))


if __name__ == '__main__':
    unittest.main()
