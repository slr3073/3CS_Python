#!/usr/bin/env python3

import unittest


# 1) Coloration Naïve
# on a besoin d'une fonction pour trouver  le plus petit entier>=1
# qui n'est pas dans la liste des couleurs interdites

def plusPetitEnDehorsDe(List):
    sortedList = sorted(List)
    for i in range(1, len(sortedList) + 2):
        if i not in sortedList:
            return i

def colorNaive(Graphe):
    coloration = dict()

    for sommet in Graphe:
        couleursDesVoisins = set()
        for voisin in Graphe[sommet]:
            couleursDesVoisins.add(coloration[voisin])

        coloration[sommet] = plusPetitEnDehorsDe(couleursDesVoisins)

    return coloration


# 2) Coloration gloutonne
# Ici il nous faut le calcul du noyau d'un ensemble de sommets
# c'est à dire une liste maximale sans couple de sommets adjacents

def noyau(L, G):
    N = set()
    # TODO compléter ici
    return N


def colorGlouton(G):
    color = {}  # Dictionnaire des couleurs
    S = set(G.keys())  # ensemble des sommets restant à colorier
    # TODO compléter ici
    return color


# 3) Complément pour occuper les plus rapides :
#   Coloration de Welsh et Powell
# On a vu en TD qu'on diminue sensiblement le nombre de couleurs nécessaires
# en traitant les sommets dans l'ordre décroissant des degrés

def colorWP(G):
    color = {1: 1}  # Dictionnaire des couleurs
    # Calcul des degrés
    Deg = {}
    for sommet in G:
        Deg[sommet] = len(G[sommet])
    # on trie par degré décroissant
    # for sommet in sorted(Deg, key=Deg.get, reverse=True):

    return color


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

    def testWP(self):
        self.assertEqual(colorWP(self.G), {1: 1, 2: 3, 3: 2, 4: 4, 5: 1, 6: 1, 7: 2})


if __name__ == '__main__':
    unittest.main()
