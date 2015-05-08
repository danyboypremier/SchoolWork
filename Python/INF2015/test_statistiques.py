# -*- coding: utf-8 -*-

import unittest
import statistiques as Stats
import classes


class TestStatistiquesConstructeurVide(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.stats = Stats.Statistiques()

    def test_nb_complets(self):
        self.assertEquals(self.stats.nb_complets, 0)

    def test_nb_incomplets(self):
        self.assertEquals(self.stats.nb_incomplets, 0)

    def test_nb_invalides(self):
        self.assertEquals(self.stats.nb_invalides, 0)

    def test_nb_sexe_inconnu(self):
        self.assertEquals(self.stats.nb_sexe_inconnu, 0)

    def test_nb_sexe_masculin(self):
        self.assertEquals(self.stats.nb_sexe_masculin, 0)

    def test_nb_sexe_feminin(self):
        self.assertEquals(self.stats.nb_sexe_feminin, 0)

    def test_nb_activites_valides_par_categorie_cours(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['cours'], 0)

    def test_nb_activites_valides_par_categorie_atelier(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['atelier'], 0)

    def test_nb_activites_valides_par_categorie_seminaire(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['séminaire'], 0)

    def test_nb_activites_valides_par_categorie_colloque(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['colloque'], 0)

    def test_nb_activites_valides_par_categorie_conference(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['conférence'], 0)

    def test_nb_activites_valides_par_categorie_lecture_dirigee(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['lecture dirigée'], 0)

    def test_nb_activites_valides_par_categorie_presentation(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['présentation'], 0)

    def test_nb_activites_valides_par_categorie_groupe_de_discussion(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['groupe de discussion'], 0)

    def test_nb_activites_valides_par_categorie_projet_de_recherche(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['projet de recherche'], 0)

    def test_nb_activites_valides_par_categorie_redaction_professionnelle(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['rédaction professionnelle'], 0)

    def test_nb_numero_permis_invalide(self):
        self.assertEquals(self.stats.nb_numero_permis_invalide, 0)

    def test_nb_ordre_complet_architectes(self):
        self.assertEquals(self.stats.nb_ordre_complet['architectes'], 0)

    def test_nb_ordre_complet_geologues(self):
        self.assertEquals(self.stats.nb_ordre_complet['geologues'], 0)

    def test_nb_ordre_complet_psychologues(self):
        self.assertEquals(self.stats.nb_ordre_complet['psychologues'], 0)

    def test_nb_ordre_complet_podiatres(self):
        self.assertEquals(self.stats.nb_ordre_complet['podiatres'], 0)

    def test_nb_ordre_incomplet_architectes(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['architectes'], 0)

    def test_nb_ordre_incomplet_geologues(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['geologues'], 0)

    def test_nb_ordre_incomplet_psychologues(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['psychologues'], 0)

    def test_nb_ordre_incomplet_podiatres(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['podiatres'], 0)


class TestStatistiquesConstructeurDonneesJSON(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        donnees_json = produire_statistiques_json()
        self.stats = Stats.Statistiques(donnees_json)

    def test_nb_invalides(self):
        self.assertEquals(self.stats.nb_invalides, 1)

    def test_nb_complets(self):
        self.assertEquals(self.stats.nb_complets, 2)

    def test_nb_incomplets(self):
        self.assertEquals(self.stats.nb_incomplets, 3)

    def test_nb_sexe_inconnu(self):
        self.assertEquals(self.stats.nb_sexe_inconnu, 4)

    def test_nb_sexe_masculin(self):
        self.assertEquals(self.stats.nb_sexe_masculin, 5)

    def test_nb_sexe_feminin(self):
        self.assertEquals(self.stats.nb_sexe_feminin, 6)

    def test_nb_activites_valides_par_categorie_cours(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['cours'], 7)

    def test_nb_activites_valides_par_categorie_atelier(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['atelier'], 8)

    def test_nb_activites_valides_par_categorie_seminaire(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['séminaire'], 9)

    def test_nb_activites_valides_par_categorie_colloque(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['colloque'], 10)

    def test_nb_activites_valides_par_categorie_conference(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['conférence'], 11)

    def test_nb_activites_valides_par_categorie_lecture_dirigee(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['lecture dirigée'], 12)

    def test_nb_activites_valides_par_categorie_presentation(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['présentation'], 13)

    def test_nb_activites_valides_par_categorie_groupe_de_discussion(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['groupe de discussion'], 14)

    def test_nb_activites_valides_par_categorie_projet_de_recherche(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['projet de recherche'], 15)

    def test_nb_activites_valides_par_categorie_redaction_professionnelle(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['rédaction professionnelle'], 16)

    def test_nb_numero_permis_invalide(self):
        self.assertEquals(self.stats.nb_numero_permis_invalide, 17)

    def test_nb_ordre_complet_architectes(self):
        self.assertEquals(self.stats.nb_ordre_complet['architectes'], 18)

    def test_nb_ordre_complet_geologues(self):
        self.assertEquals(self.stats.nb_ordre_complet['geologues'], 19)

    def test_nb_ordre_complet_psychologues(self):
        self.assertEquals(self.stats.nb_ordre_complet['psychologues'], 20)

    def test_nb_ordre_complet_podiatres(self):
        self.assertEquals(self.stats.nb_ordre_complet['podiatres'], 21)

    def test_nb_ordre_incomplet_architectes(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['architectes'], 22)

    def test_nb_ordre_incomplet_geologues(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['geologues'], 23)

    def test_nb_ordre_incomplet_psychologues(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['psychologues'], 24)

    def test_nb_ordre_incomplet_podiatres(self):
        self.assertEquals(self.stats.nb_ordre_incomplet['podiatres'], 25)


class TestStatistiquesGenererDictionnaireJsonable(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        stats = Stats.Statistiques()
        self.dict_stats = stats.generer_dictionnaire_jsonable()

    def test_nb_complets(self):
        self.assertEquals(self.dict_stats['nb_complets'], 0)

    def test_nb_incomplets(self):
        self.assertEquals(self.dict_stats['nb_incomplets'], 0)

    def test_nb_invalides(self):
        self.assertEquals(self.dict_stats['nb_invalides'], 0)

    def test_nb_sexe_masculin(self):
        self.assertEquals(self.dict_stats['nb_sexe_masculin'], 0)

    def test_nb_sexe_feminin(self):
        self.assertEquals(self.dict_stats['nb_sexe_feminin'], 0)

    def test_nb_sexe_inconnu(self):
        self.assertEquals(self.dict_stats['nb_sexe_inconnu'], 0)

    def test_nb_numero_permis_invalide(self):
        self.assertEquals(self.dict_stats['nb_numero_permis_invalide'], 0)

    def test_nb_ordre_complet(self):
        self.assertEquals(self.dict_stats['nb_ordre_complet'], {'architectes': 0,
                                                                'geologues': 0,
                                                                'psychologues': 0,
                                                                'podiatres': 0
        })

    def test_nb_ordre_incomplet(self):
        self.assertEquals(self.dict_stats['nb_ordre_incomplet'], {'architectes': 0,
                                                                  'geologues': 0,
                                                                  'psychologues': 0,
                                                                  'podiatres': 0
        })

    def test_nb_activites_valides_par_categorie(self):
        self.assertEquals(self.dict_stats['nb_activites_valides_par_categorie'], classes.Categories().liste)


class TestStatistiquesAjouterActivites(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        donnees_json = produire_json_membre_valide_complet()
        membre = classes.Membre(donnees_json)
        self.stats = Stats.Statistiques()

        self.stats.ajouter_activites_membre(membre.activites)

    def test_nb_activites_valides_categorie_cours(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['cours'], 1)

    def test_nb_activites_valides_categorie_atelier(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['atelier'], 0)

    def test_nb_activites_valides_categorie_seminaire(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['séminaire'], 0)

    def test_nb_activites_valides_categorie_colloque(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['colloque'], 0)

    def test_nb_activites_valides_categorie_conference(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['conférence'], 0)

    def test_nb_activites_valides_categorie_lecture_dirigee(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['lecture dirigée'], 0)

    def test_nb_activites_valides_categorie_presentation(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['présentation'], 1)

    def test_nb_activites_valides_categorie_groupe_de_discussion(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['groupe de discussion'], 1)

    def test_nb_activites_valides_categorie_projet_de_recherche(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['projet de recherche'], 1)

    def test_nb_activites_valides_categorie_redaction_professionnelle(self):
        self.assertEquals(self.stats.nb_activites_valides_par_categorie.liste['rédaction professionnelle'], 1)


class TestStatistiques(unittest.TestCase):
    def test_ajouter_membre_valide_complet(self):
        donnees_json = produire_json_membre_valide_complet()
        membre = classes.Membre(donnees_json)
        stats = Stats.Statistiques()

        stats.ajouter_membre_valide_complet(membre)
        stats.ajouter_membre_valide_complet(membre)

        self.assertEquals(stats.nb_complets, 2)

    def test_ajouter_membre_valide_incomplet(self):
        donnees_json = produire_json_membre_valide_complet()
        membre = classes.Membre(donnees_json)
        stats = Stats.Statistiques()

        stats.ajouter_membre_valide_incomplet(membre)
        stats.ajouter_membre_valide_incomplet(membre)

        self.assertEquals(stats.nb_incomplets, 2)

    def test_ajouter_membre_invalide(self):
        stats = Stats.Statistiques()

        stats.ajouter_membre_invalide()
        stats.ajouter_membre_invalide()

        self.assertEquals(stats.nb_invalides, 2)

    def test_ordre_complet(self):
        donnees_json = produire_json_membre_valide_complet()
        membre = classes.Membre(donnees_json)
        stats = Stats.Statistiques()

        stats.ajouter_membre_valide_complet(membre)
        stats.ajouter_membre_valide_complet(membre)

        self.assertEquals(stats.nb_ordre_complet['geologues'], 2)

    def test_ordre_incomplet(self):
        donnees_json = produire_json_membre_valide_complet()
        membre = classes.Membre(donnees_json)
        stats = Stats.Statistiques()

        stats.ajouter_membre_valide_incomplet(membre)
        stats.ajouter_membre_valide_incomplet(membre)

        self.assertEquals(stats.nb_ordre_incomplet['geologues'], 2)

    def test_ajouter_sexe_inconnu(self):
        stats = Stats.Statistiques()

        stats.ajouter_sexe(0)

        self.assertEquals(stats.nb_sexe_inconnu, 1)

    def test_ajouter_sexe_masculin(self):
        stats = Stats.Statistiques()

        stats.ajouter_sexe(1)

        self.assertEquals(stats.nb_sexe_masculin, 1)

    def test_ajouter_sexe_feminin(self):
        stats = Stats.Statistiques()

        stats.ajouter_sexe(2)

        self.assertEquals(stats.nb_sexe_feminin, 1)

    def test_repr(self):
        stats = Stats.Statistiques()
        actuel = str(stats)

        prevu = "Déclarations traitées: 0\n" + \
                "Déclarations complètes: 0\n" + \
                "Déclarations incomplètes ou invalides: 0\n" + \
                "Déclarations faites par des hommes: 0\n" + \
                "Déclarations faites par des femmes: 0\n" + \
                "Déclarations faites par des gens de sexe inconnu: 0\n" + \
                "Activités valides totales: 0\n" + \
                "Activités valides par catégorie: \n" + \
                "\tcours: 0\n" + \
                "\tatelier: 0\n" + \
                "\tséminaire: 0\n" + \
                "\tcolloque: 0\n" + \
                "\tconférence: 0\n" + \
                "\tlecture dirigée: 0\n" + \
                "\tprésentation: 0\n" + \
                "\tgroupe de discussion: 0\n" + \
                "\tprojet de recherche: 0\n" + \
                "\trédaction professionnelle: 0\n" + \
                "Déclarations avec numéro de permis invalide: 0\n" + \
                "Déclarations complètes par ordre professionnel:\n" + \
                "\tarchitectes: 0\n" + \
                "\tgeologues: 0\n" + \
                "\tpsychologues: 0\n" + \
                "\tpodiatres: 0\n" + \
                "Déclarations incomplètes par ordre professionnel:\n" + \
                "\tarchitectes: 0\n" + \
                "\tgeologues: 0\n" + \
                "\tpsychologues: 0\n" + \
                "\tpodiatres: 0\n"

        self.assertEquals(actuel, prevu)

    def test_compter_nb_declarations_traitees(self):
        stats = Stats.Statistiques()
        self.assertEqual(stats.compter_nb_declarations_traitees(), 0)


def produire_statistiques_json():
    return {"nb_invalides": 1,
            "nb_complets": 2,
            "nb_incomplets": 3,
            "nb_sexe_inconnu": 4,
            "nb_sexe_masculin": 5,
            "nb_sexe_feminin": 6,
            "nb_activites_valides_par_categorie": {u'cours': 7,
                                                   u'atelier': 8,
                                                   u'séminaire': 9,
                                                   u'colloque': 10,
                                                   u'conférence': 11,
                                                   u'lecture dirigée': 12,
                                                   u'présentation': 13,
                                                   u'groupe de discussion': 14,
                                                   u'projet de recherche': 15,
                                                   u'rédaction professionnelle': 16
            },
            "nb_numero_permis_invalide": 17,
            "nb_ordre_complet": {"architectes": 18,
                                 "geologues": 19,
                                 "psychologues": 20,
                                 "podiatres": 21
            },
            "nb_ordre_incomplet": {"architectes": 22,
                                   "geologues": 23,
                                   "psychologues": 24,
                                   "podiatres": 25
            }
    }


def produire_json_membre_valide_complet():
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