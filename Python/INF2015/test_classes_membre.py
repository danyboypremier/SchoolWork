# -*- coding: utf-8 -*-

import unittest
import classes
import datetime

COURS = 0


class TestClassesMembre(unittest.TestCase):
    def setUp(self):
        self.membre = classes.Membre(self.produire_json_membre())

    def test_nom_membre(self):
        self.assertEqual(self.membre.nom, 'ttt')

    def test_prenom_membre(self):
        self.assertEqual(self.membre.prenom, 'ttt')

    def test_sexe_membre(self):
        self.assertEqual(self.membre.sexe, 1)

    def test_ordre_membre(self):
        self.assertEqual(self.membre.ordre, 'geologues')

    def test_numero_permis(self):
        self.assertEqual(self.membre.numero_permis, 'TT1234')

    def test_cycle(self):
        self.assertEqual(self.membre.cycle, '2013-2016')

    def test_membre_activite_cour_description(self):
        self.assertEqual(self.membre.activites[COURS].description, 'Séminaire sur l\'architecture contemporaine')

    def test_membre_activite_cour_categorie(self):
        self.assertEqual(self.membre.activites[COURS].categorie, 'cours')

    def test_membre_activite_cour_heures(self):
        self.assertEqual(self.membre.activites[COURS].heures, 22)

    def test_membre_activite_cour_date(self):
        self.assertEqual(self.membre.activites[COURS].date,
                         datetime.datetime(*[int(i) for i in '2014-01-07'.split('-')]))

    def test_heures_transferees_superieur_ou_egale_a_0(self):
        self.membre.heures_transferees = 0

        try:
            self.membre.tester_nombre_heures_transfere_est_non_negatif()
        except TypeError:
            self.fail()

    def test_heures_transferees_inferieur_a_0(self):
        self.membre.heures_transferees = -1

        with self.assertRaises(TypeError):
            self.membre.tester_nombre_heures_transfere_est_non_negatif()

    def produire_json_membre(self):
        return {
            "nom": u'ttt',
            "prenom": u'ttt',
            "sexe": 1,
            "ordre": u'géologues',
            "numero_de_permis": u'TT1234',
            "cycle": u'2013-2016',
            "activites": [
                {
                    "description": u'Séminaire sur l\'architecture contemporaine',
                    "categorie": u'cours',
                    "heures": 22,
                    "date": u'2014-01-07'
                }
            ]
        }


if __name__ == '__main__':
    unittest.main()