#!/usr/bin/env python3
import unittest

def plusPetitEnDehorsDe(List: set):
    sortedList = sorted(List)
    for i in range(1, len(sortedList) + 2):
        if i not in sortedList:
            return i
    return 1

def colorNaive(Graphe: dict):
    coloration = dict()
    for sommet in Graphe:
        couleurVoisins = set()
        for voisin in Graphe[sommet]:
            if voisin in coloration:
                couleurVoisins.add(coloration[voisin])

        coloration[sommet] = plusPetitEnDehorsDe(couleurVoisins)

    return coloration

def noyau(Sommets: set, Graphe: dict):
    Sommets = Sommets.copy()
    Noyau = set()
    while Sommets:
        sommet = Sommets.pop()
        Noyau.add(sommet)
        for voisin in Graphe[sommet]:
            if voisin in Sommets:
                Sommets.remove(voisin)

    return Noyau

def colorGlouton(Graphe: dict):
    coloration = dict()
    Sommets = set()
    for sommet in Graphe:
        Sommets.add(sommet)

    noyau(Sommets, Graphe)

    couleur = 1
    while Sommets:
        for sommet in noyau(Sommets, Graphe):
            coloration[sommet] = couleur
            Sommets.remove(sommet)

        couleur += 1

    return coloration

class GrapheTest(unittest.TestCase):

    def setUp(self):
        self.Petersen = {
            1: [2, 5, 6], 2: [1, 3, 7], 3: [2, 4, 8], 4: [3, 5, 9], 5: [1, 4, 10],
            6: [1, 8, 9], 7: [2, 9, 10], 8: [3, 6, 10], 9: [4, 6, 7], 10: [5, 7, 8]
        }
        self.G = {1: [2, 3, 4], 2: [1, 3, 4, 5], 3: [1, 2, 4, 5, 6], 4: [1, 2, 3, 6], 5: [2, 3, 7], 6: [3, 4, 7],
                  7: [5, 6]}

    def testPlusPetitEnDehorsDe(self):
        self.assertEqual(plusPetitEnDehorsDe({}), 1)
        self.assertEqual(plusPetitEnDehorsDe({1, 2, 3}), 4)
        self.assertEqual(plusPetitEnDehorsDe({1, 4, 2, 6, 9}), 3)
        self.assertEqual(plusPetitEnDehorsDe({1, 4, 2, 6, 9, 3}), 5)

    def testNaive(self):
        self.assertEqual(colorNaive(self.Petersen), {1: 1, 2: 2, 3: 1, 4: 2, 5: 3, 6: 2, 7: 1, 8: 3, 9: 3, 10: 2})
        self.assertEqual(colorNaive(self.G), {1: 1, 2: 2, 3: 3, 4: 4, 5: 1, 6: 1, 7: 2})

    def testGlouton(self):
        self.assertEqual(noyau({i for i in range(1, 10)}, self.Petersen), {1, 3, 7})
        self.assertEqual(noyau({2, 4, 5, 6, 8, 9, 10}, self.Petersen), {2, 4, 6, 10})
        self.assertEqual(noyau({5, 8, 9}, self.Petersen), {5, 8, 9})
        self.assertEqual(colorGlouton(self.Petersen), {1: 1, 2: 2, 3: 1, 4: 2, 5: 3, 6: 2, 7: 1, 8: 3, 9: 3, 10: 2})
        self.assertEqual(colorGlouton(self.G), {1: 1, 2: 2, 3: 3, 4: 4, 5: 1, 6: 1, 7: 2})

if __name__ == '__main__':
    unittest.main()
