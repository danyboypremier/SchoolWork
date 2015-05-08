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


class TestValidationArchitectes(unittest.TestCase):
    def setUp(self):
        donnees_json_architecte = self.produire_json_membre_architecte()
        self.membre_architecte = classes.Membre(donnees_json_architecte)
        self.architecte = validation.Architectes(self.membre_architecte)
        self.architecte.rapport.conteneur_erreurs = []
        self.architecte.rapport.est_complet = False
        self.architecte = None

    def test_valider_numero_permis_valide(self):
        liste_numero_permis_valide = ["A0001", "T9999"]

        self.architecte = validation.Architectes(self.membre_architecte)

        for numero_permis_valide in liste_numero_permis_valide:
            try:
                self.architecte.membre.numero_permis = numero_permis_valide
                self.architecte.valider()
            except validation.ExceptionFichierEntreeInvalide:
                self.fail()

    def test_valider_numero_permis_invalide(self):
        liste_numero_permis_valide = ["S1000", "Z1111", "a0001", "1000", "A000w", "Z10000"]

        self.architecte = validation.Architectes(self.membre_architecte)

        for numero_permis_valide in liste_numero_permis_valide:
            with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
                self.architecte.membre.numero_permis = numero_permis_valide
                self.architecte.valider()

    def test_valider_cycle_2012_2014_valide(self):
        cycle_valide = "2012-2014"
        self.membre_architecte.cycle = cycle_valide

        try:
            self.architecte = validation.Architectes(self.membre_architecte)

            nombre_erreurs_dans_rapport = len(self.architecte.rapport.conteneur_erreurs)
            self.assertEquals(nombre_erreurs_dans_rapport, 0)
        except validation.ExceptionFichierEntreeInvalide:
            self.fail()

    def test_valider_cycle_2010_2012_valide(self):
        cycle_valide = "2010-2012"
        self.membre_architecte.cycle = cycle_valide
        self.modifier_date_des_activites("2011-01-01")

        try:
            self.architecte = validation.Architectes(self.membre_architecte)

            nombre_erreurs_dans_rapport = len(self.architecte.rapport.conteneur_erreurs)
            self.assertEquals(nombre_erreurs_dans_rapport, 0)
        except validation.ExceptionFichierEntreeInvalide:
            self.fail()

    def test_valider_cycle_2008_2010_valide(self):
        cycle_valide = "2008-2010"
        self.membre_architecte.cycle = cycle_valide
        self.modifier_date_des_activites("2009-01-01")

        try:
            self.architecte = validation.Architectes(self.membre_architecte)

            nombre_erreurs_dans_rapport = len(self.architecte.rapport.conteneur_erreurs)
            self.assertEquals(nombre_erreurs_dans_rapport, 0)
        except validation.ExceptionFichierEntreeInvalide:
            self.fail()

    def test_valider_cycle_2008_2009_invalide(self):
        cycle_invalide = "2008-2009"
        self.membre_architecte.cycle = cycle_invalide

        with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
            self.architecte = validation.Architectes(self.membre_architecte)

    def test_valider_heures_transferees_du_cycle_precedent_valide(self):
        liste_heures_transferees_valide = [0, 3, 7]

        for heures_transferees_valide in liste_heures_transferees_valide:
            self.membre_architecte.heures_transferees = heures_transferees_valide

            self.architecte = validation.Architectes(self.membre_architecte)

            nombre_erreurs_dans_rapport = len(self.architecte.rapport.conteneur_erreurs)
            self.assertEquals(nombre_erreurs_dans_rapport, 0)
            self.assertTrue(self.architecte.rapport.est_complet)

    def test_valider_heures_transferees_du_cycle_precedent_invalide(self):
        liste_heures_transferees_invalide = [8, 10, 100]
        self.membre_architecte.activites[PRESENTATION].heures = 1
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 4

        for heures_transferees_invalide in liste_heures_transferees_invalide:
            self.membre_architecte.heures_transferees = heures_transferees_invalide

            self.architecte = validation.Architectes(self.membre_architecte)

            nombre_erreurs_dans_rapport = len(self.architecte.rapport.conteneur_erreurs)
            self.assertNotEquals(nombre_erreurs_dans_rapport, 0)
            self.assertFalse(self.architecte.rapport.est_complet)

    def test_valider_date_activite_cycle_2012_2014_1er_janvier_2012_valide(self):
        self.membre_architecte.cycle = "2012-2014"
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2012, 4, 1)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertNotEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 42
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        self.verifier_nb_msg_attendu(0)

    def test_valider_date_activite_cycle_2012_2014_30_mars_2012_invalide(self):
        self.membre_architecte.cycle = "2012-2014"
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2012, 3, 30)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 37
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.architecte.membre.activites[QUELCONQUE].description
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_date_activite_cycle_2012_2014_1er_mai_2014_invalide(self):
        self.membre_architecte.cycle = "2012-2014"
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2014, 5, 1)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 37
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.architecte.membre.activites[QUELCONQUE].description
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_date_activite_cycle_2010_2012_1er_avril_2012_valide(self):
        self.membre_architecte.cycle = "2010-2012"
        self.modifier_date_des_activites("2011-01-01")
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2012, 4, 1)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertNotEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 42
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        self.verifier_nb_msg_attendu(0)

    def test_valider_date_activite_cycle_2010_2012_30_mars_2010_invalide(self):
        self.membre_architecte.cycle = "2010-2012"
        self.modifier_date_des_activites("2011-01-01")
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2010, 3, 30)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 37
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.architecte.membre.activites[QUELCONQUE].description
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_date_activite_cycle_2010_2012_1er_mai_2012_invalide(self):
        self.membre_architecte.cycle = "2010-2012"
        self.modifier_date_des_activites("2011-01-01")
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2012, 5, 1)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 37
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.architecte.membre.activites[QUELCONQUE].description
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_date_activite_cycle_2008_2010_1er_janvier_2009_valide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2009, 1, 1)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertNotEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 42
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        self.verifier_nb_msg_attendu(0)

    def test_valider_date_activite_cycle_2008_2010_30_mars_2008_invalide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2008, 3, 30)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 37
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.architecte.membre.activites[QUELCONQUE].description
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_date_activite_cycle_2008_2010_2_juillet_2010_invalide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[QUELCONQUE].date = datetime.datetime(2010, 7, 2)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertEquals(self.architecte.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 37
        heures_activites_actuel = self.architecte.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.architecte.membre.activites[QUELCONQUE].description
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_de_formation_total_cycle_2012_2014_valide(self):
        self.membre_architecte.cycle = "2012-2014"
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 8
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 5
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 5
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 5

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_total_cycle_2010_2012_valide(self):
        self.membre_architecte.cycle = "2010-2012"
        self.modifier_date_des_activites("2011-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 10
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 5
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 5
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 5

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_total_cycle_2008_2010_valide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 10
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 5
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 5
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 5

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_total_cycle_2012_2014_invalide(self):
        self.membre_architecte.cycle = "2012-2014"
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 7
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 5
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 5
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 5

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)

    def test_valider_heures_de_formation_total_cycle_2010_2012_invalide(self):
        self.membre_architecte.cycle = "2010-2012"
        self.modifier_date_des_activites("2011-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 10
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 5
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 4
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 5

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)

    def test_valider_heures_de_formation_total_cycle_2008_2010_invalide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 10
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 5
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 5
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 4

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)

    def test_valider_heures_de_formation_categorie_cours_valide(self):
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 15
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 20
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 10
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 20

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_categorie_cours_invalide(self):
        self.membre_architecte.activites[COURS].heures = 16
        self.membre_architecte.activites[PRESENTATION].heures = 15
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 21
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 10
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 20

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_ARCHITECTES_HEURES_GROUPE_COURS % 1
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_maximum_categorie_presentation_valide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 23
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 1
        self.membre_architecte.activites.pop(4)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_maximum_categorie_presentation_invalide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 24
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_architecte.activites.pop(3)
        self.membre_architecte.activites.pop(3)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (41, 1)
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_maximum_categorie_groupe_de_discussion_valide(self):
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 4
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 17
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 1
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_maximum_categorie_groupe_de_discussion_invalide(self):
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 3
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 18
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 1
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 1

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (39, 1)
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_maximum_categorie_projet_de_recherche_valide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 1
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 23
        self.membre_architecte.activites.pop(4)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_maximum_categorie_projet_de_recherche_invalide(self):
        self.membre_architecte.cycle = "2008-2010"
        self.modifier_date_des_activites("2009-01-01")
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 24
        self.membre_architecte.activites.pop(1)
        self.membre_architecte.activites.pop(3)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (41, 1)
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_maximum_categorie_redaction_valide(self):
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 4
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 1
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 17

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_maximum_categorie_redaction_invalide(self):
        self.membre_architecte.activites[COURS].heures = 17
        self.membre_architecte.activites[PRESENTATION].heures = 3
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].heures = 1
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].heures = 1
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].heures = 18

        self.architecte = validation.Architectes(self.membre_architecte)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (39, 1)
        msg_actuel = self.architecte.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_est_complet(self):
        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertTrue(self.architecte.rapport.est_complet)

    def test_valider_est_incomplet(self):
        self.membre_architecte.activites.pop(COURS)

        self.architecte = validation.Architectes(self.membre_architecte)

        self.assertFalse(self.architecte.rapport.est_complet)

    def verifier_nb_msg_attendu(self, nb_msg_attendu):
        nb_msg_actuel = len(self.architecte.rapport.conteneur_erreurs)
        self.assertEquals(nb_msg_attendu, nb_msg_actuel)

    def modifier_date_des_activites(self, nouvelle_date):
        nouvelle_date_formate = datetime.datetime(*[int(i) for i in nouvelle_date.split('-')])
        self.membre_architecte.activites[COURS].date = nouvelle_date_formate
        self.membre_architecte.activites[PRESENTATION].date = nouvelle_date_formate
        self.membre_architecte.activites[GROUPE_DE_DISCUSSION].date = nouvelle_date_formate
        self.membre_architecte.activites[PROJET_DE_RECHERCHE].date = nouvelle_date_formate
        self.membre_architecte.activites[REDACTION_PROFESSIONNELLE].date = nouvelle_date_formate

    def produire_json_membre_architecte(self):
        return {
            "nom": u'Archive',
            "prenom": u'Plan',
            "sexe": 1,
            "ordre": u'architectes',
            "numero_de_permis": u'A0001',
            "cycle": u'2012-2014',
            "heures_transferees_du_cycle_precedent": 0,
            "activites": [
                {
                    "description": u'Séminaire sur l\'archit1ecture contemporaine',
                    "categorie": u'cours',
                    "heures": 17,
                    "date": u'2013-01-07'
                },
                {
                    "description": u'Cours sur la déontologie',
                    "categorie": u'présentation',
                    "heures": 10,
                    "date": u'2013-03-20'
                },
                {
                    "description": u'Séminaire sur l\'arch2itecture contemporaine',
                    "categorie": u'groupe de discussion',
                    "heures": 5,
                    "date": u'2013-01-07'
                },
                {
                    "description": u'Cours sur la déontologie',
                    "categorie": u'projet de recherche',
                    "heures": 5,
                    "date": u'2013-03-20'
                },
                {
                    "description": u'Séminaire sur l\'arc3hitecture contemporaine',
                    "categorie": u'rédaction professionnelle',
                    "heures": 5,
                    "date": u'2013-01-07'
                }
            ]
        }


if __name__ == '__main__':
    unittest.main()