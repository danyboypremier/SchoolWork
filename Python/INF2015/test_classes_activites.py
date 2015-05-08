# -*- coding: utf-8 -*-

import unittest
import classes
import datetime


class TestClassesActivites(unittest.TestCase):
    def setUp(self):
        description = u'La description d\'une activité'
        categorie = u'cours'
        heures = 20
        date = u'2014-01-07'
        self.activite = classes.Activites(description, categorie, heures, date)

    def test_description_activite(self):
        self.assertEqual(self.activite.description, 'La description d\'une activité')

    def test_categorie_activite(self):
        self.assertEqual(self.activite.categorie, "cours")

    def test_heures_activite(self):
        self.assertEqual(self.activite.heures, 20)

    def test_date_activite(self):
        self.assertEqual(self.activite.date, datetime.datetime(*[int(i) for i in '2014-01-07'.split('-')]))

    def test_generer_dictionnaire_jsonable(self):
        rapport = classes.Rapport()

        dict_actuel = rapport.generer_dictionnaire_jsonable()

        dict_prevu = {'erreurs': [], 'complet': False}
        self.assertEquals(dict_actuel, dict_prevu)


if __name__ == '__main__':
    unittest.main()