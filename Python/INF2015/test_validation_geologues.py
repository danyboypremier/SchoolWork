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
QUELCONQUE = 4

PRENOM = 0
NOM = 1
NUM = 2


class TestValidationGeologues(unittest.TestCase):
    def setUp(self):
        donnees_json_geologue = self.produire_json_membre_geologue()
        self.membre_geologue = classes.Membre(donnees_json_geologue)
        self.geologue = validation.Geologues(self.membre_geologue)
        self.geologue.rapport.conteneur_erreurs = []
        self.geologue.rapport.est_complet = False
        self.geologue = None

    def test_valider_numero_permis_valide(self):
        liste_numero_permis_valide = [["Madame", "Totonski", "TM1234"],
                                      ["Abdul", "Bariba", "BA0000"]]

        self.geologue = validation.Geologues(self.membre_geologue)

        for numero_permis_valide in liste_numero_permis_valide:
            try:
                self.geologue.membre.prenom = numero_permis_valide[PRENOM]
                self.geologue.membre.nom = numero_permis_valide[NOM]
                self.geologue.membre.numero_permis = numero_permis_valide[NUM]
                self.geologue.valider()
            except validation.ExceptionFichierEntreeInvalide:
                self.fail()

    def test_valider_numero_permis_invalide(self):
        liste_numero_permis_valide = [["Madame", "Totonski", "tm1234"],
                                      ["Abdul", "Bariba", "BA-0000"],
                                      ["Madame", "Totonski", "TM12"]]

        self.geologue = validation.Geologues(self.membre_geologue)

        for numero_permis_valide in liste_numero_permis_valide:
            with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
                self.geologue.membre.prenom = numero_permis_valide[PRENOM]
                self.geologue.membre.nom = numero_permis_valide[NOM]
                self.geologue.membre.numero_permis = numero_permis_valide[NUM]
                self.geologue.valider()

    def test_valider_cycle_valide(self):
        cycle_valide = "2013-2016"
        self.membre_geologue.cycle = cycle_valide

        try:
            self.geologue = validation.Geologues(self.membre_geologue)

            nombre_erreurs_dans_rapport = len(self.geologue.rapport.conteneur_erreurs)
            self.assertEquals(nombre_erreurs_dans_rapport, 0)
        except validation.ExceptionFichierEntreeInvalide:
            self.fail()

    def test_valider_cycle_invalide(self):
        cycle_invalide = "2013-2015"
        self.membre_geologue.cycle = cycle_invalide

        with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
            self.geologue = validation.Geologues(self.membre_geologue)

    def test_valider_categories_activite_valide(self):
        self.geologue = validation.Geologues(self.membre_geologue)

        nombre_erreurs_dans_rapport = len(self.geologue.rapport.conteneur_erreurs)
        self.assertEquals(nombre_erreurs_dans_rapport, 0)
        heures_activites_attendu = 72
        heures_activites_actuel = self.geologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)

    def test_valider_categories_activite_invalide(self):
        activite_invalide = "activite quelconque"
        self.membre_geologue.activites[QUELCONQUE].categorie = activite_invalide

        self.geologue = validation.Geologues(self.membre_geologue)

        nombre_erreurs_dans_rapport = len(self.geologue.rapport.conteneur_erreurs)
        self.assertEquals(nombre_erreurs_dans_rapport, 1)
        msg_attendu = Msg.ERREUR_CATEGORIE_INVALIDE % \
                      (self.geologue.membre.activites[QUELCONQUE].description, activite_invalide)
        msg_actuel = self.geologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_heures_transferees_du_cycle_precedent_inexistant(self):
        self.membre_geologue.heures_transferees = None

        self.geologue = validation.Geologues(self.membre_geologue)

        self.assertIsNone(self.geologue.membre.heures_transferees)

    def test_heures_transferees_du_cycle_precedent_existant(self):
        self.membre_geologue.heures_transferees = 10

        with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
            self.geologue = validation.Geologues(self.membre_geologue)

    def test_date_activite_cycle_2013_2016_1er_juin_2016_valide(self):
        self.membre_geologue.activites[QUELCONQUE].date = datetime.datetime(2016, 6, 1)

        self.geologue = validation.Geologues(self.membre_geologue)

        self.assertNotEquals(self.geologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 72
        heures_activites_actuel = self.geologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        self.verifier_nb_msg_attendu(0)

    def test_date_activite_cycle_2013_2016_1er_juin_2013_valide(self):
        self.membre_geologue.activites[QUELCONQUE].date = datetime.datetime(2013, 6, 1)

        self.geologue = validation.Geologues(self.membre_geologue)

        self.assertNotEquals(self.geologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 72
        heures_activites_actuel = self.geologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        self.verifier_nb_msg_attendu(0)

    def test_date_activite_cycle_2013_2016_31_mai_2013_invalide(self):
        self.membre_geologue.activites[QUELCONQUE].date = datetime.datetime(2013, 5, 31)

        self.geologue = validation.Geologues(self.membre_geologue)

        self.assertEquals(self.geologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 69
        heures_activites_actuel = self.geologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.geologue.membre.activites[QUELCONQUE].description
        msg_actuel = self.geologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_date_activite_cycle_2013_2016_2_juin_2016_invalide(self):
        self.membre_geologue.activites[QUELCONQUE].date = datetime.datetime(2016, 6, 2)

        self.geologue = validation.Geologues(self.membre_geologue)

        self.assertEquals(self.geologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 69
        heures_activites_actuel = self.geologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.geologue.membre.activites[QUELCONQUE].description
        msg_actuel = self.geologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_de_formation_total_valide(self):
        self.membre_geologue.activites[COURS].heures = 22
        self.membre_geologue.activites[PRESENTATION].heures = 28
        self.membre_geologue.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_geologue.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_geologue.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_total_invalide(self):
        self.membre_geologue.activites[COURS].heures = 22
        self.membre_geologue.activites[PRESENTATION].heures = 27
        self.membre_geologue.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_geologue.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_geologue.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (54, 1)
        msg_actuel = self.geologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_de_formation_categorie_cours_valide(self):
        self.membre_geologue.activites[COURS].heures = 22
        self.membre_geologue.activites[PRESENTATION].heures = 28
        self.membre_geologue.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_geologue.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_geologue.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_categorie_cours_invalide(self):
        self.membre_geologue.activites[COURS].heures = 21
        self.membre_geologue.activites[PRESENTATION].heures = 29
        self.membre_geologue.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_geologue.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_geologue.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_GEOLOGUES_HEURES_GROUPE_COURS % 1
        msg_actuel = self.geologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_de_formation_categorie_projet_de_recherche_valide(self):
        self.membre_geologue.activites[COURS].heures = 22
        self.membre_geologue.activites[PRESENTATION].heures = 28
        self.membre_geologue.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_geologue.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_geologue.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_categorie_projet_de_recherche_invalide(self):
        self.membre_geologue.activites[COURS].heures = 22
        self.membre_geologue.activites[PRESENTATION].heures = 28
        self.membre_geologue.activites[GROUPE_DE_DISCUSSION].heures = 2
        self.membre_geologue.activites[PROJET_DE_RECHERCHE].heures = 2
        self.membre_geologue.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_GEOLOGUES_HEURES_GROUPE_PROJET_DE_RECHERCHE % 1
        msg_actuel = self.geologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_de_formation_categorie_groupe_de_discussion_valide(self):
        self.membre_geologue.activites[COURS].heures = 22
        self.membre_geologue.activites[PRESENTATION].heures = 28
        self.membre_geologue.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_geologue.activites[PROJET_DE_RECHERCHE].heures = 3
        self.membre_geologue.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_categorie_groupe_de_discussion_invalide(self):
        self.membre_geologue.activites[COURS].heures = 22
        self.membre_geologue.activites[PRESENTATION].heures = 28
        self.membre_geologue.activites.pop(GROUPE_DE_DISCUSSION)
        self.membre_geologue.activites[2].heures = 4
        self.membre_geologue.activites[3].heures = 1

        self.geologue = validation.Geologues(self.membre_geologue)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_GEOLOGUES_HEURES_GROUPE_GROUPE_DE_DISCUSSION % 1
        msg_actuel = self.geologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_est_complet(self):
        self.geologue = validation.Geologues(self.membre_geologue)

        self.assertTrue(self.geologue.rapport.est_complet)

    def test_valider_est_incomplet(self):
        self.membre_geologue.activites.pop(0)

        self.geologue = validation.Geologues(self.membre_geologue)

        self.assertFalse(self.geologue.rapport.est_complet)

    def verifier_nb_msg_attendu(self, nb_msg_attendu):
        nb_msg_actuel = len(self.geologue.rapport.conteneur_erreurs)
        self.assertEquals(nb_msg_attendu, nb_msg_actuel)

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
                    "description": u'Séminaire sur l\'archi3tecture contemporaine',
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
                    "description": u'Séminaire sur l\'arch2itecture contemporaine',
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
                    "description": u'Séminaire sur l\'archi1tecture contemporaine',
                    "categorie": u'rédaction professionnelle',
                    "heures": 3,
                    "date": u'2014-01-07'
                }
            ]
        }


if __name__ == '__main__':
    unittest.main()