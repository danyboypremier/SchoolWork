# -*- coding: utf-8 -*-

import unittest
import classes
import validation
import datetime

from constantes import Messages as Msg

COURS = 0
PRESENTATION = 1
GROUPE_DE_DISCUSSION = 2
PROJET_DE_RECHERCHE = 3
REDACTION_PROFESSIONNELLE = 4


class TestValidationPodiatres(unittest.TestCase):
    def setUp(self):
        donnees_json_podiatre = self.produire_json_membre_podiatre()
        self.membre_podiatre = classes.Membre(donnees_json_podiatre)
        self.podiatre = validation.Podiatres(self.membre_podiatre)
        self.podiatre.rapport.conteneur_erreurs = []
        self.podiatre.rapport.est_complet = False
        self.podiatre = None

    def test_valider_numero_permis_valide(self):
        liste_numero_permis_valide = ["12345", "99999"]

        self.podiatre = validation.Podiatres(self.membre_podiatre)

        for numero_permis_valide in liste_numero_permis_valide:
            try:
                self.podiatre.membre.numero_permis = numero_permis_valide
                self.podiatre.valider()
            except validation.ExceptionFichierEntreeInvalide:
                self.fail()

    def test_valider_numero_permis_invalide(self):
        liste_numero_permis_valide = ["1234", "123456", "aaaaa", "a83723"]

        self.podiatre = validation.Podiatres(self.membre_podiatre)

        for numero_permis_valide in liste_numero_permis_valide:
            with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
                self.podiatre.membre.numero_permis = numero_permis_valide
                self.podiatre.valider()

    def test_valider_cycle_valide(self):
        cycle_valide = "2013-2016"
        self.membre_podiatre.cycle = cycle_valide

        try:
            self.podiatre = validation.Podiatres(self.membre_podiatre)

            nombre_erreurs_dans_rapport = len(self.podiatre.rapport.conteneur_erreurs)
            self.assertEquals(nombre_erreurs_dans_rapport, 0)
        except validation.ExceptionFichierEntreeInvalide:
            self.fail()

    def test_valider_cycle_invalide(self):
        cycle_invalide = "2013-2015"
        self.membre_podiatre.cycle = cycle_invalide

        with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
            self.podiatre = validation.Podiatres(self.membre_podiatre)

    def test_valider_heures_de_formation_total_valide(self):
        self.membre_podiatre.activites[COURS].heures = 27
        self.membre_podiatre.activites[PRESENTATION].heures = 28
        self.membre_podiatre.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_podiatre.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_podiatre.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.podiatre = validation.Podiatres(self.membre_podiatre)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_total_invalide(self):
        self.membre_podiatre.activites[COURS].heures = 26
        self.membre_podiatre.activites[PRESENTATION].heures = 28
        self.membre_podiatre.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_podiatre.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_podiatre.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.podiatre = validation.Podiatres(self.membre_podiatre)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (59, 1)
        msg_actuel = self.podiatre.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def verifier_nb_msg_attendu(self, nb_msg_attendu):
        nb_msg_actuel = len(self.podiatre.rapport.conteneur_erreurs)
        self.assertEquals(nb_msg_attendu, nb_msg_actuel)

    def produire_json_membre_podiatre(self):
        return {
            "nom": u'Mister',
            "prenom": u'Beaudoin',
            "sexe": 1,
            "ordre": u'podiatres',
            "numero_de_permis": u'12345',
            "cycle": u'2013-2016',
            "activites": [
                {
                    "description": u'Séminaire sur l\'archi1tecture contemporaine',
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
                    "description": u'Séminaire sur l\'archite2cture contemporaine',
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
                    "description": u'Séminaire sur l\'archite3cture contemporaine',
                    "categorie": u'rédaction professionnelle',
                    "heures": 3,
                    "date": u'2014-01-07'
                }
            ]
        }


if __name__ == '__main__':
    unittest.main()