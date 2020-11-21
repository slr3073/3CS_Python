#!/usr/bin/env python3
import unittest

def nbSommets(G):
	return len(G)

def nbArcs(G):
	nbLiens = 0
	for k in G:
		for _ in G[k]:
			nbLiens += 1
	return nbLiens

def ajoutArc(G, i, j):
	G[i].append(j)

def enleveArc(G, i, j):
	if j == i:
		if i in G[i]:
			G[i].remove(i)
		else:
			raise ValueError("L'arc n'existe pas")
	else:
		if j in G[i]:
			G[i].remove(j)
		else:
			raise ValueError("L'arc n'existe pas")

def degS(G, i):
	return len(G[i])

def degreS(G):
	D = {}
	for k in G:
		D[k] = len(G[k])
	return D

def degE(G, i):
	cpt = 0
	for k in G:
		for e in G[k]:
			if e == i:
				cpt += 1
	return cpt

def degreE(G):
	D = {}
	for k in G:
		D[k] = degE(G, k)
	return D

def listeToMatrice(G):
	n = len(G)
	M = [[0 for _ in range(n)] for _ in range(n)]
	for k in G:
		for v in G[k]:
			M[k - 1][v - 1] += 1
	return M

def arcsToListe(n, L):
	G = {}
	for arc in L:
		s = arc[0]
		e = arc[1]
		if s in G:
			G[s].append(e)
		else:
			G[s] = [e]
	return G

def matToListe(M):
	L = {}
	for i in range(len(M)):
		liste = []
		for j in range(len(M[0])):
			for _ in range(M[i][j]):
				liste.append(j + 1)
		L[i + 1] = liste
	return L

class GrapheTest(unittest.TestCase):

	def setUp(self):
		self.list = [(1, 5), (2, 1), (2, 4), (3, 2), (4, 3), (5, 2), (5, 4)]
		self.LAdj = {1: [5], 2: [1, 4], 3: [2], 4: [3], 5: [2, 4]}
		self.mat = [
			[0, 0, 0, 0, 1],
			[1, 0, 0, 1, 0],
			[0, 1, 0, 0, 0],
			[0, 0, 1, 0, 0],
			[0, 1, 0, 1, 0]]

	def testsBasiques(self):
		self.assertEqual(nbSommets(self.LAdj), 5, 'Décompte erroné des sommets')
		self.assertEqual(nbArcs(self.LAdj), 7, 'Décompte erroné des arcs')
		self.assertEqual(degreS(self.LAdj), {1: 1, 2: 2, 3: 1, 4: 1, 5: 2}, 'Connexité sortante erronée')
		self.assertEqual(degreE(self.LAdj), {1: 1, 2: 2, 3: 1, 4: 2, 5: 1}, 'Connexité entrante erronée')

	def testAjoutGeneral(self):
		ajoutArc(self.LAdj, 1, 4)
		self.assertEqual(nbArcs(self.LAdj), 8, 'Décompte des arcs erroné après insertion')
		self.assertIn(4, self.LAdj[1], 'La liste d\'adjacence a été mise à jour de manière erronée')
		self.assertNotIn(1, self.LAdj[4], 'La liste d\'adjacence a été mise à jour de manière erronée')

	def testAjoutReflexif(self):
		ajoutArc(self.LAdj, 1, 1)
		self.assertEqual(nbArcs(self.LAdj), 8, 'Décompte des arcs erroné après insertion')
		self.assertEqual(self.LAdj[1].count(1), 1, 'La liste d\'adjacence a été mise à jour de manière erronée')

	def testEnleveNA(self):
		try:
			enleveArc(self.LAdj, 1, 4)
		except ValueError:
			return
		except:
			pass
		self.fail('Tentative non détectée de supprimer un arc qui n\'existe pas')

	def testEnleveGeneral(self):
		enleveArc(self.LAdj, 2, 4)
		self.assertEqual(nbArcs(self.LAdj), 6, 'Décompte des arcs erroné après suppression')
		self.assertNotIn(4, self.LAdj[2])

	def testGestionMulti(self):
		ajoutArc(self.LAdj, 1, 5)
		self.assertEqual(nbArcs(self.LAdj), 8)
		self.assertEqual(self.LAdj[1].count(5), 2, 'La liste d\'adjacence a été mise à jour de manière erronée')
		enleveArc(self.LAdj, 1, 5)
		self.assertEqual(nbArcs(self.LAdj), 7)
		self.assertEqual(self.LAdj[1].count(5), 1, 'La liste d\'adjacence a été mise à jour de manière erronée')

	def testListeToMatrice(self):
		self.assertEqual(listeToMatrice(self.LAdj), self.mat)

	def testArcsToListe(self):
		self.assertEqual(arcsToListe(5, self.list), self.LAdj)

	def testMatToListe(self):
		self.assertEqual(matToListe(self.mat), self.LAdj)

if __name__ == '__main__':
	unittest.main()
