#!/usr/bin/env python3
import unittest
from collections import deque

def nbSommets(Graphe: dict):
    return len(Graphe.keys())

def largeur(Graphe: dict, i: int):
    Visite = set()
    File = deque()
    ordreVisite = []

    File.append(i)
    Visite.add(i)

    while len(File) != 0:
        k = File[0]
        ordreVisite.append(k)
        for e in Graphe[k]:
            if e not in Visite:
                Visite.add(e)
                File.append(e)
        File.popleft()

    return ordreVisite

def largeur2(Graphe: dict, i: int):
    Visite = set()
    File = deque()
    ordreVisite = []

    File.append(i)
    Visite.add(i)

    while File:
        sommetVisite = File[0]
        ordreVisite.append(sommetVisite)
        for voisin in Graphe[sommetVisite]:
            if voisin not in Visite:
                File.append(voisin)
                Visite.add(voisin)

        File.popleft()
    return ordreVisite

def largeurG(Graphe: dict):
    ordreVisite = []

    for k in Graphe:
        if k not in ordreVisite:
            newOrdreVisite = largeur(Graphe, k)
            for e in newOrdreVisite:
                if e not in ordreVisite:
                    ordreVisite.append(e)

    return ordreVisite

class GrapheTest(unittest.TestCase):

    def setUp(self):
        self.G1 = {1: [5], 2: [1, 4], 3: [2], 4: [3], 5: [2, 4]}
        self.G2 = {1: [5], 2: [1, 4, 5], 3: [2, 4], 4: [], 5: [4]}
        self.G3 = {1: [3, 5, 6], 2: [1], 3: [2, 4], 4: [], 5: [], 6: [4]}
        self.G4 = {1: [4, 6], 2: [3], 3: [], 4: [5, 6], 5: [1], 6: []}
        self.Petersen = {
            1: [2, 5, 6],
            2: [1, 3, 7],
            3: [2, 4, 8],
            4: [3, 5, 9],
            5: [1, 4, 10],
            6: [1, 8, 9],
            7: [2, 9, 10],
            8: [3, 6, 10],
            9: [4, 6, 7],
            10: [5, 7, 8]
        }

    def testNbSommets(self):
        self.assertEqual(nbSommets(self.G1), 5)

    def testLargeurOriente(self):
        for k, v in {
            1: [1, 5, 2, 4, 3],
            2: [2, 1, 4, 5, 3],
            3: [3, 2, 1, 4, 5],
            4: [4, 3, 2, 1, 5],
            5: [5, 2, 4, 1, 3]
        }.items():
            self.assertEqual(largeur(self.G1, k), v)
        self.assertEqual(largeur(self.G1, 5), [5, 2, 4, 1, 3])
        self.assertEqual(largeur(self.G2, 3), [3, 2, 4, 1, 5])
        self.assertEqual(largeur(self.G2, 5), [5, 4])
        self.assertEqual(largeur(self.G3, 4), [4])
        self.assertEqual(largeur(self.G3, 6), [6, 4])
        self.assertEqual(largeur(self.G4, 1), [1, 4, 6, 5])
        self.assertEqual(largeur(self.G4, 2), [2, 3])

    def testLargeurNonOriente(self):
        self.assertEqual(largeur(self.Petersen, 1), [1, 2, 5, 6, 3, 7, 4, 10, 8, 9])
        self.assertEqual(largeur(self.Petersen, 2), [2, 1, 3, 7, 5, 6, 4, 8, 9, 10])

    def testLargeurGeneraliseOriente(self):
        self.assertEqual(largeurG(self.G1), [1, 5, 2, 4, 3])
        self.assertEqual(largeurG(self.G2), [1, 5, 4, 2, 3])
        self.assertEqual(largeurG(self.G3), [1, 3, 5, 6, 2, 4])
        self.assertEqual(largeurG(self.G4), [1, 4, 6, 5, 2, 3])

    def testLargeurGeneraliseNonOriente(self):
        self.assertEqual(largeurG(self.Petersen), [1, 2, 5, 6, 3, 7, 4, 10, 8, 9])

if __name__ == '__main__':
    unittest.main()
