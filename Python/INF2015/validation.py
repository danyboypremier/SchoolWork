# -*- coding: utf-8 -*-

from constantes import Messages as Msg, ConstantesNumeriques as Num
from constantes import cycles_et_balises_valides_par_ordre_professionnel as balises
from constantes import conditions_architectes, conditions_psychologues, conditions_geologues, conditions_podiatres
from constantes import sexe, gabarit_numero_permis
import classes
import re


'''
    La classe Validation sert de classe abstraite pour valider les conditions de formation continue d'un
    membre. Elle contient les méthodes de validation communes aux sous-classes qui en héritent.
'''


class Validation:
    heures_activites_categorie = None
    membre = None
    conditions_activites = None
    conditions_permis = {}
    rapport = classes.Rapport()

    def valider(self):
        try:
            self.tenter_de_valider()
        except ExceptionCycleInvalide:
            self.rapport.ajouter_erreurs(Msg.ERREUR_CYCLE_INVALIDE)

    def tenter_de_valider(self):
        self.valider_sexe()
        self.valider_numero_permis()
        self.valider_cycle()
        self.valider_activites()
        self.valider_heures()

    def valider_sexe(self):
        if not self.membre.sexe in sexe:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_SEXE_INVALIDE)

    def valider_numero_permis(self):
        moule_numero_permis = re.compile(gabarit_numero_permis[self.membre.ordre])
        if not moule_numero_permis.match(self.membre.numero_permis):
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_NUMERO_PERMIS_INVALIDE)

    def valider_cycle(self):
        if not self.membre.cycle in balises[self.membre.ordre]['cycle_valide']:
            raise ExceptionCycleInvalide

    def valider_activites(self):
        for activite in self.membre.activites:
            self.valider_une_activite(activite)

    def valider_une_activite(self, activite):
        try:
            self.tenter_de_valider_activites(activite)
        except ExceptionDateActiviteInvalide:
            activite.heures = 0
            self.rapport.ajouter_erreurs(Msg.ERREUR_DATE_INVALIDE % activite.description)
        except KeyError:
            activite.heures = 0
            self.rapport.ajouter_erreurs(Msg.ERREUR_CATEGORIE_INVALIDE % (activite.description, activite.categorie))

    def tenter_de_valider_activites(self, activite):
        self.valider_date_activite(activite)
        self.valider_heures_activite(activite)
        self.valider_categorie_activite(activite)
        self.valider_description_activite(activite)

    def valider_date_activite(self, activite):
        if not self.date_est_dans_cycle_valide(activite.date):
            raise ExceptionDateActiviteInvalide

    def date_est_dans_cycle_valide(self, date):
        cycle = balises[self.membre.ordre]['cycle_valide'][self.membre.cycle]
        return date >= cycle[Num.DATE_DEBUT] and date <= cycle[Num.DATE_FIN]

    def valider_heures_activite(self, activite):
        if activite.heures <= 0:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_HEURES_ACTIVITE_INVALIDE % activite.categorie)

    def valider_categorie_activite(self, activite):
        self.heures_activites_categorie.ajouter(activite.categorie, activite.heures)

    def valider_description_activite(self, activite):
        if len(activite.description) <= Num.LONGUEUR_MINIMUM_DESCRIPTION:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_DESCRIPTION_ACTIVITE_INVALIDE % activite.categorie)


'''
    La classe Architectes sert à valider les conditions de formation continue des membres de l'ordre des
    architectes. Elle contient les méthodes de validation spécifiques aux architectes. Le résultat
    de cette validation est disponible dans sa variable membre rapport. Cette classe hérite de Validation.
'''


class Architectes(Validation):
    def __init__(self, membre):
        try:
            self.heures_activites_categorie = classes.Categories()
            self.membre = membre
            self.conditions_activites = conditions_architectes[self.membre.cycle]
            self.valider()
        except KeyError as e:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_CYCLE_INVALIDE)

    def valider_heures(self):
        heures_transferees_valides = self.calculer_heures_transferees_valides()
        self.valider_heures_des_categories(heures_transferees_valides)

    def calculer_heures_transferees_valides(self):
        heures_transferees_valides = self.membre.heures_transferees
        if self.membre.heures_transferees < self.conditions_activites['MIN_HEURES_TRANSFERE']:
            heures_transferees_valides = self.conditions_activites['MIN_HEURES_TRANSFERE']
        elif self.membre.heures_transferees > self.conditions_activites['MAX_HEURES_TRANSFERE']:
            heures_transferees_valides = self.conditions_activites['MAX_HEURES_TRANSFERE']
            heures_transferees_invalides = self.membre.heures_transferees - \
                    self.conditions_activites['MAX_HEURES_TRANSFERE']
            self.rapport.ajouter_erreurs(Msg.ERREUR_HEURES_TRANSFEREES_TROP %
                    (self.membre.heures_transferees, heures_transferees_invalides))
        return heures_transferees_valides

    def valider_heures_des_categories(self, heures_transferees_valides):
        heures_cours = self.calculer_somme_heures_groupe_cours() + heures_transferees_valides
        validation_heures_cours = self.valider_heures_cours(heures_cours)
        validation_heures_toutes_categories = self.valider_heures_toutes_categories(heures_transferees_valides)
        if validation_heures_cours and validation_heures_toutes_categories:
            self.rapport.set_est_complet()

    def calculer_somme_heures_groupe_cours(self):
        return self.heures_activites_categorie.somme('cours') + \
               self.heures_activites_categorie.somme('atelier') + \
               self.heures_activites_categorie.somme('séminaire') + \
               self.heures_activites_categorie.somme('colloque') + \
               self.heures_activites_categorie.somme('conférence') + \
               self.heures_activites_categorie.somme('lecture dirigée')

    def valider_heures_cours(self, heures_cours):
        if heures_cours >= self.conditions_activites['MIN_HEURES_COURS']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_ARCHITECTES_HEURES_GROUPE_COURS % (
                self.conditions_activites['MIN_HEURES_COURS'] - heures_cours))
            return False

    def valider_heures_toutes_categories(self, heures_transferees_valides):
        heures_total = self.calculer_total_heures_selon_maximum_permis(heures_transferees_valides)
        if heures_total >= conditions_architectes[self.membre.cycle]['MIN_HEURES_COMPLET']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_HEURES_TOTALES %
                    (heures_total, self.conditions_activites['MIN_HEURES_COMPLET'] - heures_total))
        return False

    def calculer_total_heures_selon_maximum_permis(self, heures_transferees_valides):
        return (self.calculer_somme_heures_groupe_cours() +
                min(self.heures_activites_categorie.somme('présentation'),
                    self.conditions_activites['MAX_HEURES_PRESENTATION']) +
                min(self.heures_activites_categorie.somme('groupe de discussion'),
                    self.conditions_activites['MAX_HEURES_GROUPE_DE_DISCUSSION']) +
                min(self.heures_activites_categorie.somme('projet de recherche'),
                    self.conditions_activites['MAX_HEURES_PROJET_DE_RECHERCHE']) +
                min(self.heures_activites_categorie.somme('rédaction professionnelle'),
                    self.conditions_activites['MAX_HEURES_REDACTION_PROFESSIONNELLE']) +
                heures_transferees_valides)


'''
    La classe Geologues sert à valider les conditions de formation continue des membres de l'ordre des
    geologues. Elle contient les méthodes de validation spécifiques aux géologues. Le résultat
    de cette validation est disponible dans sa variable membre rapport. Cette classe hérite de Validation.
'''


class Geologues(Validation):
    def __init__(self, membre):
        try:
            self.heures_activites_categorie = classes.Categories()
            self.membre = membre
            self.conditions_activites = conditions_geologues[self.membre.cycle]
            self.valider()
        except KeyError as e:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_CYCLE_INVALIDE)

    # Overrides Validation.valider_numero_permis()    
    def valider_numero_permis(self):
        try:
            premiere_lettre = self.membre.nom[0].upper() == self.membre.numero_permis[0]
            deuxieme_lettre = self.membre.prenom[0].upper() == self.membre.numero_permis[1]
        except IndexError:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_NUMERO_PERMIS_INVALIDE)
        moule_numero_permis = re.compile(gabarit_numero_permis[self.membre.ordre])
        if not (moule_numero_permis.match(self.membre.numero_permis) and premiere_lettre and deuxieme_lettre):
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_NUMERO_PERMIS_INVALIDE)

    def valider_heures(self):
        self.valider_heures_transferees_none()
        self.valider_heures_categories()

    def valider_heures_transferees_none(self):
        if self.membre.heures_transferees is not None:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_HEURES_TRANSFEREES_INVALIDE)

    def valider_heures_categories(self):
        heures_cours = self.heures_activites_categorie.somme('cours')
        heures_projet_de_recherche = self.heures_activites_categorie.somme('projet de recherche')
        heures_groupe_de_discussion = self.heures_activites_categorie.somme('groupe de discussion')

        validation_heures_cours = self.valider_heures_cours(heures_cours)
        validation_heures_projet_de_recherche = self.valider_heures_projet_de_recherche(heures_projet_de_recherche)
        validation_heures_groupe_de_discussion = self.valider_heures_groupe_de_discussion(heures_groupe_de_discussion)
        validation_heures_toutes_categories = self.valider_heures_toutes_categories()
        if validation_heures_cours and validation_heures_projet_de_recherche and \
                validation_heures_groupe_de_discussion and validation_heures_toutes_categories:
            self.rapport.set_est_complet()

    def valider_heures_cours(self, heures_cours):
        if heures_cours >= self.conditions_activites['MIN_HEURES_COURS']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_GEOLOGUES_HEURES_GROUPE_COURS %
                    (self.conditions_activites['MIN_HEURES_COURS'] - heures_cours))
            return False

    def valider_heures_projet_de_recherche(self, heures_projet_de_recherche):
        if heures_projet_de_recherche >= self.conditions_activites['MIN_HEURES_PROJET_DE_RECHERCHE']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_GEOLOGUES_HEURES_GROUPE_PROJET_DE_RECHERCHE %
                (self.conditions_activites['MIN_HEURES_PROJET_DE_RECHERCHE'] - heures_projet_de_recherche))
            return False

    def valider_heures_groupe_de_discussion(self, heures_groupe_de_discussion):
        if heures_groupe_de_discussion >= self.conditions_activites['MIN_HEURES_GROUPE_DE_DISCUSSION']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_GEOLOGUES_HEURES_GROUPE_GROUPE_DE_DISCUSSION %
                    (self.conditions_activites['MIN_HEURES_GROUPE_DE_DISCUSSION'] - heures_groupe_de_discussion))
            return False

    def valider_heures_toutes_categories(self):
        heures_total = self.calculer_total_heures_selon_maximum_permis()
        if heures_total >= self.conditions_activites['MIN_HEURES_COMPLET']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_HEURES_TOTALES %
                    (heures_total, self.conditions_activites['MIN_HEURES_COMPLET'] - heures_total))
        return False

    def calculer_total_heures_selon_maximum_permis(self):
        return (self.heures_activites_categorie.somme('cours') +
                self.heures_activites_categorie.somme('atelier') +
                self.heures_activites_categorie.somme('séminaire') +
                self.heures_activites_categorie.somme('colloque') +
                self.heures_activites_categorie.somme('conférence') +
                self.heures_activites_categorie.somme('lecture dirigée') +
                self.heures_activites_categorie.somme('présentation') +
                self.heures_activites_categorie.somme('groupe de discussion') +
                self.heures_activites_categorie.somme('projet de recherche') +
                self.heures_activites_categorie.somme('rédaction professionnelle'))


'''
    La classe Psychologues sert à valider les conditions de formation continue des membres de l'ordre des
    psychologues. Elle contient les méthodes de validation spécifiques aux psychologues. Le résultat
    de cette validation est disponible dans sa variable membre rapport. Cette classe hérite de Validation.
'''


class Psychologues(Validation):
    def __init__(self, membre):
        try:
            self.heures_activites_categorie = classes.Categories()
            self.membre = membre
            self.conditions_activites = conditions_psychologues[self.membre.cycle]
            self.valider()
        except KeyError as e:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_CYCLE_INVALIDE)

    def valider_heures(self):
        self.valider_heures_transferees_none()
        self.valider_heures_categories()

    def valider_heures_transferees_none(self):
        if self.membre.heures_transferees is not None:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_HEURES_TRANSFEREES_INVALIDE)

    def valider_heures_categories(self):
        heures_categorie_cours = self.heures_activites_categorie.somme('cours')
        validation_heures_categorie_cours = self.valider_heures_categorie_cours(heures_categorie_cours)
        validation_heures_toutes_categories = self.valider_heures_toutes_categories()
        if validation_heures_categorie_cours and validation_heures_toutes_categories:
            self.rapport.set_est_complet()

    def valider_heures_categorie_cours(self, heures_categorie_cours):
        if heures_categorie_cours >= self.conditions_activites['MIN_HEURES_COURS']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_PSYCHOLOGUES_HEURES_GROUPE_COURS %
                    (self.conditions_activites['MIN_HEURES_COURS'] - heures_categorie_cours))
            return False

    def valider_heures_toutes_categories(self):
        heures_total = self.calculer_total_heures_selon_maximum_permis()
        if heures_total >= self.conditions_activites['MIN_HEURES_COMPLET']:
            return True
        else:
            self.rapport.ajouter_erreurs(Msg.ERREUR_HEURES_TOTALES %
                    (heures_total, self.conditions_activites['MIN_HEURES_COMPLET'] - heures_total))
        return False

    def calculer_total_heures_selon_maximum_permis(self):
        return (self.heures_activites_categorie.somme('cours') +
                self.heures_activites_categorie.somme('atelier') +
                self.heures_activites_categorie.somme('séminaire') +
                self.heures_activites_categorie.somme('colloque') +
                min(self.heures_activites_categorie.somme('conférence'),
                        self.conditions_activites['MAX_HEURES_CONFERENCE']) +
                self.heures_activites_categorie.somme('lecture dirigée') +
                self.heures_activites_categorie.somme('présentation') +
                self.heures_activites_categorie.somme('groupe de discussion') +
                self.heures_activites_categorie.somme('projet de recherche') +
                self.heures_activites_categorie.somme('rédaction professionnelle'))


'''
    La classe Podiatres sert à valider les conditions de formation continue des membres de l'ordre des
    podiatres. Elle contient les méthodes de validation spécifiques aux podiatres. Le résultat
    de cette validation est disponible dans sa variable membre rapport. Cette classe hérite de Geologues
    puisque les règles de validation des podiatres et des géologues sont similaires.
'''


class Podiatres(Geologues):
    # Overrides Geologues(membre)
    def __init__(self, membre):
        try:
            self.heures_activites_categorie = classes.Categories()
            self.membre = membre
            self.conditions_activites = conditions_podiatres[self.membre.cycle]
            self.valider()
        except KeyError as e:
            raise ExceptionFichierEntreeInvalide(Msg.ERREUR_CYCLE_INVALIDE)

    # Overrides Geologues.valider_numero_permis() avec Validation.valider_numero_permis
    def valider_numero_permis(self):
        Validation.valider_numero_permis(self)


class ExceptionDateActiviteInvalide(Exception):
    pass


class ExceptionCycleInvalide(Exception):
    pass


class ExceptionFichierEntreeInvalide(Exception):
    pass
