#!/usr/bin/env python3
import unittest

def nbSommets(Graphe):
    return len(Graphe)

def nbAretes(Graphe):
    nbLiens = 0
    for sommet in Graphe:
        for successeur in Graphe[sommet]:
            if successeur == sommet:
                nbLiens += 2
            else:
                nbLiens += 1

    return int(nbLiens / 2)

def ajoutArete(G, i, j):
    if i not in G:
        G[i] = []
    G[i].append(j)
    if i != j:
        if j not in G:
            G[j] = []
        G[j].append(i)

def enleveArete(G, i, j):
    if j not in G[i]:
        raise ValueError("L'arête n'existe pas")
    G[i].remove(j)
    if i != j:
        G[j].remove(i)

def deg(Graphe, sommet):
    return len(Graphe[sommet])

def degre(Graphe):
    result = {}
    for sommet in Graphe:
        result[sommet] = len(Graphe[sommet])

    return result

def kuratowski(n):
    result = {}
    for i in range(1, n + 1):
        successeur = []
        for j in range(1, n + 1):
            if i != j:
                successeur.append(j)
        result[i] = successeur

    return result

def areteToListe(L):
    G = {}
    for arete in L:
        s1 = arete[0]
        s2 = arete[1]
        if s1 in G:
            G[s1].append(s2)
        else:
            G[s1] = [s2]
        if s1 != s2:
            if s2 in G:
                G[s2].append(s1)
            else:
                G[s2] = [s1]
    return G

def listeToMatrice(G, n):
    M = [[0 for _ in range(n)] for _ in range(n)]
    for k in G:
        for v in G[k]:
            if v >= k:
                M[k - 1][v - 1] += 1
                if k != v:
                    M[v - 1][k - 1] += 1
    return M

def nonOriente(M):
    # TODO
    return True

def matToListe(M):
    # TODO

    return {}

class GrapheTest(unittest.TestCase):

    def setUp(self):
        self.liste = [(1, 2), (1, 5), (1, 5), (2, 3), (2, 4), (2, 4), (3, 3), (3, 4), (4, 5)]
        self.LAdj = {1: [2, 5, 5], 2: [1, 3, 4, 4], 3: [2, 3, 4], 4: [2, 2, 3, 5], 5: [1, 1, 4]}
        self.matrice = [
            [0, 1, 0, 0, 2],
            [1, 0, 1, 2, 0],
            [0, 1, 1, 1, 0],
            [0, 2, 1, 0, 1],
            [2, 0, 0, 1, 0]]

    def testsBasiques(self):
        self.assertEqual(nbSommets(self.LAdj), 6, 'Décompte erroné des sommets')
        self.assertEqual(nbAretes(self.LAdj), 9, 'Décompte erroné des arêtes')
        self.assertEqual(degre(self.LAdj), {1: 3, 2: 4, 3: 3, 4: 4, 5: 3}, 'Erreur dans le calcul des degrés')

    def testAjoutGeneral(self):
        ajoutArete(self.LAdj, 1, 4)
        self.assertEqual(nbAretes(self.LAdj), 10, 'Décompte des arêtes erroné après insertion')
        self.assertIn(1, self.LAdj[4], 'La liste d\'adjacence a été mise à jour de manière erronée')
        self.assertIn(4, self.LAdj[1], 'La liste d\'adjacence a été mise à jour de manière erronée')

    def testAjoutReflexif(self):
        ajoutArete(self.LAdj, 1, 1)
        self.assertEqual(nbAretes(self.LAdj), 10, 'Décompte des arêtes erroné après insertion')
        self.assertEqual(self.LAdj[1].count(1), 1, 'La liste d\'adjacence a été mise à jour de manière erronée')

    def testEnleveNA(self):
        try:
            enleveArete(self.LAdj, 1, 4)
        except ValueError:
            return
        self.fail('Tentative non détectée de supprimer une arête qui n\'existe pas')

    def testEnleveGeneral(self):
        enleveArete(self.LAdj, 1, 2)
        self.assertEqual(nbAretes(self.LAdj), 8, 'Décompte des arêtes erroné après suppression')
        self.assertNotIn(1, self.LAdj[2])

    def testEnleveMulti(self):
        enleveArete(self.LAdj, 2, 4)
        self.assertEqual(self.LAdj[2].count(4), 1,
                         'Connexité erronée après suppression d\'une arête présente en plusieurs exemplaires')

    def testEnleveReflexif(self):
        enleveArete(self.LAdj, 3, 3)
        self.assertEqual(nbAretes(self.LAdj), 8, 'Décompte des arêtes erroné après suppression')
        self.assertNotIn(3, self.LAdj[3], 'Connexité erronée après suppression d\'une arête réflexive')

    def testKuratowski(self):
        self.assertEqual(kuratowski(1), {1: []}, 'K_1 erroné')
        self.assertEqual(kuratowski(2), {1: [2], 2: [1]}, 'K_2 erroné')
        self.assertEqual(kuratowski(3), {1: [2, 3], 2: [1, 3], 3: [1, 2]}, 'K_3 erroné')
        for i, l in kuratowski(12).items():
            for j in range(1, 13):
                if i != j:
                    self.assertIn(j, l, 'Il manque une ou plusieurs arêtes')
            self.assertNotIn(i, l, 'Présence erronée d\'une arête réflexive')

    def testAreteToListe(self):
        self.assertEqual(areteToListe(self.liste), self.LAdj)

    def testListeToMatrice(self):
        self.assertEqual(listeToMatrice(self.LAdj, 5), self.matrice)

    def testNonOriente(self):
        self.assertTrue(nonOriente(self.matrice))
        self.assertTrue(nonOriente([[0, 1, 2], [1, 0, 3], [2, 3, 0]]))
        self.assertFalse(nonOriente([[0, 0, 0], [0, 0, 0], [1, 0, 0]]))

    def testMatToListe(self):
        self.assertEqual(matToListe(self.matrice), self.LAdj)

if __name__ == '__main__':
    unittest.main()
