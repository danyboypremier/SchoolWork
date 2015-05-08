# -*- coding: utf-8 -*-

import io
import json
import classes

FICHIER_STATISTIQUES = "stats.json"


def ajouter_membre_invalide():
    donnees_json = lire_fichier_statistiques()
    stats = Statistiques(donnees_json)
    stats.ajouter_membre_invalide()
    ecrire_fichier_statistiques(stats.generer_dictionnaire_jsonable())


def ajouter_membre_numero_permis_invalide():
    donnees_json = lire_fichier_statistiques()
    stats = Statistiques(donnees_json)
    stats.ajouter_membre_invalide()
    stats.nb_numero_permis_invalide += 1
    ecrire_fichier_statistiques(stats.generer_dictionnaire_jsonable())


def ajouter_membre_valide_incomplet(membre):
    donnees_json = lire_fichier_statistiques()
    stats = Statistiques(donnees_json)
    stats.ajouter_membre_valide_incomplet(membre)
    ecrire_fichier_statistiques(stats.generer_dictionnaire_jsonable())


def ajouter_membre_valide_complet(membre):
    donnees_json = lire_fichier_statistiques()
    stats = Statistiques(donnees_json)
    stats.ajouter_membre_valide_complet(membre)
    ecrire_fichier_statistiques(stats.generer_dictionnaire_jsonable())


def lire_fichier_statistiques():
    with open(FICHIER_STATISTIQUES) as fichier_json:
        return json.load(fichier_json)


def ecrire_fichier_statistiques(donnees_json):
    fichier_sortie = open(FICHIER_STATISTIQUES, 'w')
    json.dump(donnees_json, fichier_sortie, indent=4, ensure_ascii=False)


def afficher():
    donnees_json = lire_fichier_statistiques()
    stats = Statistiques(donnees_json)
    print stats


def reinitialiser():
    stats = Statistiques()
    ecrire_fichier_statistiques(stats.generer_dictionnaire_jsonable())


'''
    La classe Statistiques contient les statistiques sur les validations de formation continue.  Elle
    possède les méthodes pour ajouter de nouvelles données aux existantes ainsi que pour ré-initialiser
    les statistiques.
'''


class Statistiques():
    nb_complets = 0
    nb_incomplets = 0
    nb_invalides = 0
    nb_sexe_masculin = 0
    nb_sexe_feminin = 0
    nb_sexe_inconnu = 0
    nb_numero_permis_invalide = 0
    nb_ordre_complet = {'architectes': 0,
                        'geologues': 0,
                        'psychologues': 0,
                        'podiatres': 0
    }
    nb_ordre_incomplet = {'architectes': 0,
                          'geologues': 0,
                          'psychologues': 0,
                          'podiatres': 0
    }
    nb_activites_valides_par_categorie = classes.Categories()

    def __init__(self, donnees_json=None):
        if donnees_json is None:
            self.utiliser_valeurs_par_defaut()
        else:
            self.utiliser_donnees_json(donnees_json)

    def utiliser_valeurs_par_defaut(self):
        self.nb_complets = 0
        self.nb_incomplets = 0
        self.nb_invalides = 0
        self.nb_sexe_masculin = 0
        self.nb_sexe_feminin = 0
        self.nb_sexe_inconnu = 0
        self.nb_numero_permis_invalide = 0
        for categorie in self.nb_activites_valides_par_categorie.liste.keys():
            self.nb_activites_valides_par_categorie.liste[categorie] = 0
        for ordre in self.nb_ordre_complet.keys():
            self.nb_ordre_complet[ordre] = 0
            self.nb_ordre_incomplet[ordre] = 0

    def utiliser_donnees_json(self, donnees_json):
        self.nb_complets = donnees_json['nb_complets']
        self.nb_incomplets = donnees_json['nb_incomplets']
        self.nb_invalides = donnees_json['nb_invalides']
        self.nb_sexe_masculin = donnees_json['nb_sexe_masculin']
        self.nb_sexe_feminin = donnees_json['nb_sexe_feminin']
        self.nb_sexe_inconnu = donnees_json['nb_sexe_inconnu']
        self.nb_numero_permis_invalide = donnees_json['nb_numero_permis_invalide']
        for ordre, nombre in donnees_json['nb_ordre_complet'].iteritems():
            self.nb_ordre_complet[ordre] = nombre
        for ordre, nombre in donnees_json['nb_ordre_incomplet'].iteritems():
            self.nb_ordre_incomplet[ordre] = nombre
        for categorie, nombre in donnees_json['nb_activites_valides_par_categorie'].iteritems():
            self.nb_activites_valides_par_categorie.initialiser(categorie.encode('utf-8'), nombre)

    def ajouter_membre_valide_complet(self, membre):
        self.nb_complets += 1
        self.ajouter_sexe(membre.sexe)
        self.ajouter_activites_membre(membre.activites)
        self.nb_ordre_complet[membre.ordre] += 1

    def ajouter_membre_valide_incomplet(self, membre):
        self.nb_incomplets += 1
        self.ajouter_sexe(membre.sexe)
        self.ajouter_activites_membre(membre.activites)
        self.nb_ordre_incomplet[membre.ordre] += 1

    def ajouter_membre_invalide(self):
        self.nb_invalides += 1

    def ajouter_sexe(self, sexe):
        if sexe == 0:
            self.nb_sexe_inconnu += 1
        elif sexe == 1:
            self.nb_sexe_masculin += 1
        else:
            self.nb_sexe_feminin += 1

    def ajouter_activites_membre(self, activites):
        for activite in activites:
            if activite.heures > 0 and activite.categorie != "":
                self.nb_activites_valides_par_categorie.ajouter(activite.categorie, 1)

    def generer_dictionnaire_jsonable(self):
        return {
            'nb_complets': self.nb_complets,
            'nb_incomplets': self.nb_incomplets,
            'nb_invalides': self.nb_invalides,
            'nb_sexe_masculin': self.nb_sexe_masculin,
            'nb_sexe_feminin': self.nb_sexe_feminin,
            'nb_sexe_inconnu': self.nb_sexe_inconnu,
            'nb_numero_permis_invalide': self.nb_numero_permis_invalide,
            'nb_ordre_complet': self.nb_ordre_complet,
            'nb_ordre_incomplet': self.nb_ordre_incomplet,
            'nb_activites_valides_par_categorie': self.nb_activites_valides_par_categorie.liste
        }

    def __repr__(self):
        activites = self.nb_activites_valides_par_categorie.liste
        return "Déclarations traitées: " + str(self.compter_nb_declarations_traitees()) + "\n" + \
               "Déclarations complètes: " + str(self.nb_complets) + "\n" + \
               "Déclarations incomplètes ou invalides: " + str(self.nb_incomplets + self.nb_invalides) + "\n" + \
               "Déclarations faites par des hommes: " + str(self.nb_sexe_masculin) + "\n" + \
               "Déclarations faites par des femmes: " + str(self.nb_sexe_feminin) + "\n" + \
               "Déclarations faites par des gens de sexe inconnu: " + str(self.nb_sexe_inconnu) + "\n" + \
               "Activités valides totales: " + str(self.nb_activites_valides_par_categorie.somme_toutes()) + "\n" + \
               "Activités valides par catégorie: \n" + \
               "\tcours: " + str(activites['cours']) + "\n" + \
               "\tatelier: " + str(activites['atelier']) + "\n" + \
               "\tséminaire: " + str(activites['séminaire']) + "\n" + \
               "\tcolloque: " + str(activites['colloque']) + "\n" + \
               "\tconférence: " + str(activites['conférence']) + "\n" + \
               "\tlecture dirigée: " + str(activites['lecture dirigée']) + "\n" + \
               "\tprésentation: " + str(activites['présentation']) + "\n" + \
               "\tgroupe de discussion: " + str(activites['groupe de discussion']) + "\n" + \
               "\tprojet de recherche: " + str(activites['projet de recherche']) + "\n" + \
               "\trédaction professionnelle: " + str(activites['rédaction professionnelle']) + "\n" + \
               "Déclarations avec numéro de permis invalide: " + str(self.nb_numero_permis_invalide) + "\n" + \
               "Déclarations complètes par ordre professionnel:\n" + \
               "\tarchitectes: " + str(self.nb_ordre_complet['architectes']) + "\n" + \
               "\tgeologues: " + str(self.nb_ordre_complet['geologues']) + "\n" + \
               "\tpsychologues: " + str(self.nb_ordre_complet['psychologues']) + "\n" + \
               "\tpodiatres: " + str(self.nb_ordre_complet['podiatres']) + "\n" + \
               "Déclarations incomplètes par ordre professionnel:\n" + \
               "\tarchitectes: " + str(self.nb_ordre_incomplet['architectes']) + "\n" + \
               "\tgeologues: " + str(self.nb_ordre_incomplet['geologues']) + "\n" + \
               "\tpsychologues: " + str(self.nb_ordre_incomplet['psychologues']) + "\n" + \
               "\tpodiatres: " + str(self.nb_ordre_incomplet['podiatres']) + "\n"

    def compter_nb_declarations_traitees(self):
        return self.nb_complets + self.nb_incomplets + self.nb_invalides
