#!/usr/bin/env python3
from collections import deque
from PW1_Graphe_Represantations.PW1_P2 import *

def triTopo(Graphe: dict):
    result = []
    degreEntrant = degreE(Graphe)
    sources = deque()

    for sommet in Graphe:
        if degreEntrant[sommet] == 0:
            sources.append(sommet)

    while sources:
        source = sources.popleft()
        result.append(source)
        for successeur in Graphe[source]:
            degreEntrant[successeur] -= 1
            if degreEntrant[successeur] == 0:
                sources.append(successeur)

    if len(result) != len(Graphe):
        raise RuntimeError

    return result

def triNiveaux(Graphe: dict):
    result = []
    degreEntrant = degreE(Graphe)
    niveau = set()

    for sommet in Graphe:
        if degreEntrant[sommet] == 0:
            niveau.add(sommet)

    while niveau:
        result.append(niveau)
        nextNiveau = set()
        for sommet in niveau:
            for successeur in Graphe[sommet]:
                degreEntrant[successeur] -= 1
                if degreEntrant[successeur] == 0:
                    nextNiveau.add(successeur)
        niveau = nextNiveau

    return result

class GrapheTest(unittest.TestCase):

    def setUp(self):
        self.simple = {1: [2], 2: [3], 3: []}
        self.simple2 = {1: [2, 3], 2: [], 3: []}
        self.cyclique = {1: [2], 2: [3], 3: [4], 4: [2]}
        self.G = {1: [2, 6], 2: [3, 5, 6], 3: [4, 5], 4: [], 5: [4], 6: [5], 7: [2, 6]}
        self.G2 = {1: [2, 7], 2: [6], 3: [2, 4, 5], 4: [5], 5: [], 6: [5, 7], 7: []}

    def testTriTopo(self):
        self.assertEqual(triTopo(self.simple), [1, 2, 3])
        self.assertEqual(triTopo(self.G), [1, 7, 2, 3, 6, 5, 4])

    def testTriTopoCyclique(self):
        try:
            triTopo(self.cyclique)
        except RuntimeError:
            return
        self.fail('Tentative de tri topologique d\'un graphe cyclique')

    def testTriNiveaux(self):
        self.assertEqual(triNiveaux(self.simple), [{1}, {2}, {3}])
        self.assertEqual(triNiveaux(self.simple2), [{1}, {2, 3}])
        self.assertEqual(triNiveaux(self.G), [{1, 7}, {2}, {3, 6}, {5}, {4}])
        self.assertEqual(triNiveaux(self.G2), [{1, 3}, {2, 4}, {6}, {5, 7}])

if __name__ == '__main__':
    unittest.main()
