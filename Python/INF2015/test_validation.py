# -*- coding: utf-8 -*-

import unittest
import classes
import validation

from constantes import sexe


class TestValidation(unittest.TestCase):
    def setUp(self):
        donnees_json_geologue = self.produire_json_membre_geologue()
        membre_geologue = classes.Membre(donnees_json_geologue)
        self.geologue = validation.Geologues(membre_geologue)

    def test_valider_sexe_0_1_ou_2(self):
        liste_sexe_valide = [0, 1, 2]

        for sexe_valide in liste_sexe_valide:
            try:
                self.geologue.membre.sexe = sexe_valide
                self.geologue.valider()
            except validation.ExceptionFichierEntreeInvalide:
                self.fail()

    def test_valider_sexe_autre_que_0_1_2(self):
        liste_sexe_invalide = [-1, 3]

        for sexe_invalide in liste_sexe_invalide:
            with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
                self.geologue.membre.sexe = sexe_invalide
                self.geologue.valider()

    def test_valider_description_activite_plus_de_20_caracteres(self):
        description_activite_valide = "Description longue123"
        self.geologue.membre.activites[0].description = description_activite_valide

        try:
            self.geologue.valider()
        except validation.ExceptionFichierEntreeInvalide:
            self.fail()

    def test_valider_description_activite_20_caracteres_ou_moins(self):
        description_activite_invalide = "Description courte12"
        self.geologue.membre.activites[0].description = description_activite_invalide

        with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
            self.geologue.valider()

    def test_valider_heures_activite_plus_grandes_que_0(self):
        liste_heures_activite_valide = [1, 5, 10, 25]

        for heures_activite_valide in liste_heures_activite_valide:
            try:
                self.geologue.membre.activites[0].heures = heures_activite_valide
                self.geologue.valider()
            except validation.ExceptionFichierEntreeInvalide:
                self.fail()

    def test_valider_heures_activite_0_ou_moins(self):
        liste_heures_activite_invalide = [0, -1, -10]

        for heures_activite_invalide in liste_heures_activite_invalide:
            with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
                self.geologue.membre.activites[0].heures = heures_activite_invalide
                self.geologue.valider()

    def produire_json_membre_geologue(self):
        return {
            "nom": u'ttt',
            "prenom": u'ttt',
            "sexe": 0,
            "ordre": u'géologues',
            "numero_de_permis": u'TT1234',
            "cycle": u'2013-2016',
            "activites": [
                {
                    "description": u'Séminaire sur l\'architecture contemporaine',
                    "categorie": u'cours',
                    "heures": 22,
                    "date": u'2014-01-07'
                },
                {
                    "description": u'Cours sur la déontologie',
                    "categorie": u'présentation',
                    "heures": 22,
                    "date": u'2014-03-20'
                },
                {
                    "description": u'Séminaire sur l\'architecture contemporaine',
                    "categorie": u'groupe de discussion',
                    "heures": 3,
                    "date": u'2014-01-07'
                },
                {
                    "description": u'Cours sur la déontologie',
                    "categorie": u'projet de recherche',
                    "heures": 22,
                    "date": u'2014-03-20'
                },
                {
                    "description": u'Séminaire sur l\'architecture contemporaine',
                    "categorie": u'rédaction professionnelle',
                    "heures": 3,
                    "date": u'2014-01-07'
                }
            ]
        }


if __name__ == '__main__':
    unittest.main()