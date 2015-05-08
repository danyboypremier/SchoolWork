# -*- coding: utf-8 -*-

import datetime


def tester_type(variable, type_attendu):
    if not isinstance(variable, type_attendu):
        raise TypeError("'{}' n'est pas du type '{}'".format(variable, type_attendu))
    return variable


'''
    La classe Membre contient les informations d'un membre d'un ordre professionnel extraites d'un fichier JSON.
'''


class Membre:
    extrait_donne_json = None
    nom = None
    prenom = None
    sexe = None
    numero_permis = None
    cycle = None
    heures_transferees = None
    activites = []
    ordre = None

    def __init__(self, extrait_donne_json):
        self.extrait_donne_json = extrait_donne_json
        self.nom = tester_type(extrait_donne_json['nom'], unicode).encode('utf-8')
        self.prenom = tester_type(extrait_donne_json['prenom'], unicode).encode('utf-8')
        self.sexe = extrait_donne_json['sexe']
        self.numero_permis = tester_type(extrait_donne_json['numero_de_permis'], unicode).encode('utf-8')
        self.cycle = extrait_donne_json['cycle']
        self.extraire_heures_transferees()
        self.activites = self.lire_activites(extrait_donne_json['activites'])
        self.ordre = tester_type(extrait_donne_json['ordre'], unicode).encode('utf-8')
        self.remplacer_caracteres_accentues_dans_ordre()
        self.tester_typage_autres_attributs()

    def extraire_heures_transferees(self):
        try:
            self.heures_transferees = \
                tester_type(self.extrait_donne_json['heures_transferees_du_cycle_precedent'], int)
            self.tester_nombre_heures_transfere_est_non_negatif()
        except KeyError as e:
            return None

    def tester_nombre_heures_transfere_est_non_negatif(self):
        if self.heures_transferees < 0:
            raise TypeError

    def lire_activites(self, liste_activites_json):
        activites_retour = []
        for activite_json in self.extrait_donne_json['activites']:
            activites_retour.append(Membre.generer_activite(activite_json))
        return activites_retour

    @staticmethod
    def generer_activite(activite_json):
        return Activites(activite_json['description'],
                         activite_json['categorie'],
                         activite_json['heures'],
                         activite_json['date'])

    def remplacer_caracteres_accentues_dans_ordre(self):
        self.ordre = self.ordre.replace("é", 'e')

    def tester_typage_autres_attributs(self):
        if not isinstance(self.numero_permis, str):
            raise TypeError


'''
    La classe Activites contient les informations sur une activité d'un Membre.
'''


class Activites:
    description = None
    categorie = None
    heures = 0
    date = None

    def __init__(self, description, categorie, heures, date):
        self.description = tester_type(description, unicode).encode('utf-8')
        self.categorie = tester_type(categorie, unicode).encode('utf-8')
        self.heures = tester_type(heures, int)
        try:
            self.date = datetime.datetime(*[int(i) for i in date.split('-')])
        except ValueError as e:
            raise ValueError(self.categorie)


'''
    La classe Rapport contient les résultats de validation des conditions de validation sous format JSON.
    Les erreurs de validation sont ajoutées par la méthode ajouter_erreurs(). On signifie que le résultat
    de la validation est complet ou non par respectivement set_est_complet() et set_est_incomplet().
'''


class Rapport:
    est_complet = False
    conteneur_erreurs = []

    def __init__(self):
        self.est_complet = False
        self.conteneur_erreurs = []

    def set_est_complet(self):
        self.est_complet = True

    def ajouter_erreurs(self, erreur):
        self.conteneur_erreurs.append(tester_type(erreur, str))

    def generer_dictionnaire_jsonable(self):
        return {
            'complet': self.est_complet,
            'erreurs': self.conteneur_erreurs
        }


'''
    La classe Categories comptabilise les heures des activités de formation continue par regroupement de 
    catégories.  Les heures sont ajoutées par la méthode ajouter_heures().  La somme des heures est 
    obtenue par la méthode somme()
'''


class Categories:
    liste = {'cours': 0,
             'atelier': 0,
             'séminaire': 0,
             'colloque': 0,
             'conférence': 0,
             'lecture dirigée': 0,
             'présentation': 0,
             'groupe de discussion': 0,
             'projet de recherche': 0,
             'rédaction professionnelle': 0
    }

    def __init__(self):
        self.liste['cours'] = 0
        self.liste['atelier'] = 0
        self.liste['séminaire'] = 0
        self.liste['colloque'] = 0
        self.liste['conférence'] = 0
        self.liste['lecture dirigée'] = 0
        self.liste['présentation'] = 0
        self.liste['groupe de discussion'] = 0
        self.liste['projet de recherche'] = 0
        self.liste['rédaction professionnelle'] = 0

    def initialiser(self, categorie, nombre):
        self.liste[categorie] = nombre

    def ajouter(self, categorie, nombre):
        self.liste[categorie] += nombre

    def somme(self, categorie):
        return self.liste[categorie]

    def somme_toutes(self):
        return sum(self.liste.values())
