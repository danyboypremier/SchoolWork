# -*- coding: utf-8 -*-

import unittest
import classes


class TestClassesCategorie(unittest.TestCase):
    def setUp(self):
        self.categorie = classes.Categories()

    def test_categorie_cours_commence_a_0(self):
        self.assertEquals(self.categorie.liste['cours'], 0)

    def test_categorie_atelier_initialiser_a_5(self):
        self.categorie.initialiser('atelier', 5)
        self.assertEquals(self.categorie.liste['atelier'], 5)

    def test_categorie_atelier_ajouter_5(self):
        self.categorie.ajouter('atelier', 5)
        self.assertEquals(self.categorie.liste['atelier'], 5)

    def test_categorie_atelier_somme(self):
        self.categorie.ajouter('atelier', 3)
        self.assertEquals(self.categorie.liste['atelier'], 3)

    def test_categorie_somme_toutes(self):
        self.categorie.initialiser('atelier', 10)
        self.categorie.initialiser('cours', 5)
        self.assertEquals(self.categorie.somme_toutes(), 15)


if __name__ == '__main__':
    unittest.main()