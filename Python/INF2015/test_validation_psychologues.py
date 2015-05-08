# -*- coding: utf-8 -*-

import unittest
import classes
import validation
import datetime

from constantes import Messages as Msg

COURS = 0
CONFERENCE = 1
GROUPE_DE_DISCUSSION = 2
PROJET_DE_RECHERCHE = 3
REDACTION_PROFESSIONNELLE = 4
QUELCONQUE = 4


class TestValidationPsychologues(unittest.TestCase):
    def setUp(self):
        donnees_json_psychologue = self.produire_json_membre_psychologue()
        self.membre_psychologue = classes.Membre(donnees_json_psychologue)
        self.psychologue = validation.Psychologues(self.membre_psychologue)
        self.psychologue.rapport.conteneur_erreurs = []
        self.psychologue.rapport.est_complet = False
        self.psychologue = None

    def test_valider_numero_permis_valide(self):
        liste_numero_permis_valide = ["83723-34", "99999-00"]

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        for numero_permis_valide in liste_numero_permis_valide:
            try:
                self.psychologue.membre.numero_permis = numero_permis_valide
                self.psychologue.valider()
            except validation.ExceptionFichierEntreeInvalide:
                self.fail()

    def test_valider_numero_permis_invalide(self):
        liste_numero_permis_valide = ["9999900", "a9999-00", "a99999-00", "99999.00"]

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        for numero_permis_valide in liste_numero_permis_valide:
            with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
                self.psychologue.membre.numero_permis = numero_permis_valide
                self.psychologue.valider()

    def test_valider_cycle_valide(self):
        cycle_valide = "2010-2015"
        self.membre_psychologue.cycle = cycle_valide

        try:
            self.psychologue = validation.Psychologues(self.membre_psychologue)

            nombre_erreurs_dans_rapport = len(self.psychologue.rapport.conteneur_erreurs)
            self.assertEquals(nombre_erreurs_dans_rapport, 0)
        except validation.ExceptionFichierEntreeInvalide:
            self.fail()

    def test_valider_cycle_invalide(self):
        cycle_invalide = "2014-2015"
        self.membre_psychologue.cycle = cycle_invalide

        with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
            self.psychologue = validation.Psychologues(self.membre_psychologue)

    def test_valider_heures_transferees_du_cycle_precedent_inexistant(self):
        self.membre_psychologue.heures_transferees = None

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.assertIsNone(self.psychologue.membre.heures_transferees)

    def test_valider_heures_transferees_du_cycle_precedent_existant(self):
        self.membre_psychologue.heures_transferees = 10

        with self.assertRaises(validation.ExceptionFichierEntreeInvalide):
            self.psychologue = validation.Psychologues(self.membre_psychologue)

    def test_valider_date_activite_cycle_2013_2016_1er_janvier_2010_valide(self):
        self.membre_psychologue.activites[QUELCONQUE].date = datetime.datetime(2010, 1, 1)

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.assertNotEquals(self.psychologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 90
        heures_activites_actuel = self.psychologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        self.verifier_nb_msg_attendu(0)

    def test_valider_date_activite_cycle_2013_2016_1er_janvier_2015_valide(self):
        self.membre_psychologue.activites[QUELCONQUE].date = datetime.datetime(2015, 1, 1)

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.assertNotEquals(self.psychologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 90
        heures_activites_actuel = self.psychologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        self.verifier_nb_msg_attendu(0)

    def test_valider_date_activite_cycle_2013_2016_31_decembre_2009_invalide(self):
        self.membre_psychologue.activites[QUELCONQUE].date = datetime.datetime(2009, 12, 31)

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.assertEquals(self.psychologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 70
        heures_activites_actuel = self.psychologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.psychologue.membre.activites[QUELCONQUE].description
        msg_actuel = self.psychologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_date_activite_cycle_2013_2016_2_juin_2016_invalide(self):
        self.membre_psychologue.activites[QUELCONQUE].date = datetime.datetime(2015, 1, 2)

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.assertEquals(self.psychologue.membre.activites[QUELCONQUE].heures, 0)
        heures_activites_attendu = 70
        heures_activites_actuel = self.psychologue.heures_activites_categorie.somme_toutes()
        self.assertEquals(heures_activites_attendu, heures_activites_actuel)
        msg_attendu = Msg.ERREUR_DATE_INVALIDE % self.psychologue.membre.activites[QUELCONQUE].description
        msg_actuel = self.psychologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_de_formation_total_valide(self):
        self.membre_psychologue.activites[COURS].heures = 25
        self.membre_psychologue.activites[CONFERENCE].heures = 15
        self.membre_psychologue.activites[GROUPE_DE_DISCUSSION].heures = 20
        self.membre_psychologue.activites[PROJET_DE_RECHERCHE].heures = 10
        self.membre_psychologue.activites[REDACTION_PROFESSIONNELLE].heures = 20

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_total_invalide(self):
        self.membre_psychologue.activites[COURS].heures = 25
        self.membre_psychologue.activites[CONFERENCE].heures = 15
        self.membre_psychologue.activites[GROUPE_DE_DISCUSSION].heures = 20
        self.membre_psychologue.activites[PROJET_DE_RECHERCHE].heures = 10
        self.membre_psychologue.activites[REDACTION_PROFESSIONNELLE].heures = 19

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (89, 1)
        msg_actuel = self.psychologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_de_formation_categorie_cours_valide(self):
        self.membre_psychologue.activites[COURS].heures = 25
        self.membre_psychologue.activites[CONFERENCE].heures = 15
        self.membre_psychologue.activites[GROUPE_DE_DISCUSSION].heures = 20
        self.membre_psychologue.activites[PROJET_DE_RECHERCHE].heures = 10
        self.membre_psychologue.activites[REDACTION_PROFESSIONNELLE].heures = 20

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_de_formation_categorie_cours_invalide(self):
        self.membre_psychologue.activites[COURS].heures = 24
        self.membre_psychologue.activites[CONFERENCE].heures = 15
        self.membre_psychologue.activites[GROUPE_DE_DISCUSSION].heures = 21
        self.membre_psychologue.activites[PROJET_DE_RECHERCHE].heures = 10
        self.membre_psychologue.activites[REDACTION_PROFESSIONNELLE].heures = 20

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_GEOLOGUES_HEURES_GROUPE_COURS % 1
        msg_actuel = self.psychologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_heures_maximum_categorie_conference_valide(self):
        self.membre_psychologue.activites[COURS].heures = 25
        self.membre_psychologue.activites[CONFERENCE].heures = 15
        self.membre_psychologue.activites[GROUPE_DE_DISCUSSION].heures = 20
        self.membre_psychologue.activites[PROJET_DE_RECHERCHE].heures = 10
        self.membre_psychologue.activites[REDACTION_PROFESSIONNELLE].heures = 20

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.verifier_nb_msg_attendu(0)

    def test_valider_heures_maximum_categorie_conference_invalide(self):
        self.membre_psychologue.activites[COURS].heures = 25
        self.membre_psychologue.activites[CONFERENCE].heures = 16
        self.membre_psychologue.activites[GROUPE_DE_DISCUSSION].heures = 20
        self.membre_psychologue.activites[PROJET_DE_RECHERCHE].heures = 9
        self.membre_psychologue.activites[REDACTION_PROFESSIONNELLE].heures = 20

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.verifier_nb_msg_attendu(1)
        msg_attendu = Msg.ERREUR_HEURES_TOTALES % (89, 1)
        msg_actuel = self.psychologue.rapport.conteneur_erreurs
        self.assertIn(msg_attendu, msg_actuel)

    def test_valider_est_complet(self):
        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.assertTrue(self.psychologue.rapport.est_complet)

    def test_valider_est_incomplet(self):
        self.membre_psychologue.activites.pop(COURS)

        self.psychologue = validation.Psychologues(self.membre_psychologue)

        self.assertFalse(self.psychologue.rapport.est_complet)

    def verifier_nb_msg_attendu(self, nb_msg_attendu):
        nb_msg_actuel = len(self.psychologue.rapport.conteneur_erreurs)
        self.assertEquals(nb_msg_attendu, nb_msg_actuel)

    def produire_json_membre_psychologue(self):
        return {
            "nom": u'Doulah',
            "prenom": u'Shrink',
            "sexe": 2,
            "ordre": u'psychologues',
            "numero_de_permis": u'12345-12',
            "cycle": u'2010-2015',
            "activites": [
                {
                    "description": u'Séminaire sur l\'archi1tecture contemporaine',
                    "categorie": u'cours',
                    "heures": 25,
                    "date": u'2014-01-07'
                },
                {
                    "description": u'Cours sur la déontologie',
                    "categorie": u'conférence',
                    "heures": 15,
                    "date": u'2014-03-20'
                },
                {
                    "description": u'Séminaire sur l\'archite2cture contemporaine',
                    "categorie": u'groupe de discussion',
                    "heures": 20,
                    "date": u'2014-01-07'
                },
                {
                    "description": u'Cours sur la déontologie',
                    "categorie": u'projet de recherche',
                    "heures": 10,
                    "date": u'2014-03-20'
                },
                {
                    "description": u'Séminaire sur l\'architec3ture contemporaine',
                    "categorie": u'rédaction professionnelle',
                    "heures": 20,
                    "date": u'2014-01-07'
                }
            ]
        }


if __name__ == '__main__':
    unittest.main()