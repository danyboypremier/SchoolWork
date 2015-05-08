# -*- coding: utf-8 -*-

import unittest
import classes


class TestClassesRapport(unittest.TestCase):
    def setUp(self):
        self.rapport = classes.Rapport()

    def test_rapport_est_complet(self):
        self.assertFalse(self.rapport.est_complet)

    def test_rapport_conteneur_erreurs(self):
        self.assertEquals(self.rapport.conteneur_erreurs, [])

    def test_rapport_set_est_complet(self):
        self.rapport.set_est_complet()
        self.assertTrue(self.rapport.est_complet)

    def test_ajouter_erreurs(self):
        self.rapport.ajouter_erreurs('test')
        self.assertEquals(self.rapport.conteneur_erreurs, ['test'])

    def test_generer_dictionnaire_jsonable(self):
        rapport = classes.Rapport()

        dict_actuel = rapport.generer_dictionnaire_jsonable()

        dict_prevu = {'erreurs': [], 'complet': False}
        self.assertEquals(dict_actuel, dict_prevu)


if __name__ == '__main__':
    unittest.main()