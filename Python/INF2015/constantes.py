# -*- coding: utf-8 -*-

import datetime


class Messages:
    USAGE = "usage : {} <fichierentree> <fichiersortie>\n        -S\n        -SR"
    STATS_REMISES_A_0 = "Les statistiques ont été réinitialisées."
    ERREUR_LECTURE = "erreur : fichier introuvable ou impossible a lire"
    ERREUR_ECRITURE = "erreur : impossible d'écrire dans le fichier de sortie"
    ERREUR_FICHIER_ENTREE_INVALIDE = "Le fichier source est invalide. "
    ERREUR_SEXE_INVALIDE = "[Sexe]"
    ERREUR_NUMERO_PERMIS_INVALIDE = "[Numéro de permis]"
    ERREUR_HEURES_TRANSFEREES_INVALIDE = "[Heures transférées]"
    ERREUR_HEURES_ACTIVITE_INVALIDE = "[Heures activité: %s]"
    ERREUR_DESCRIPTION_ACTIVITE_INVALIDE = "[Description: %s]"
    ERREUR_CHAMP_MANQUANT = "[Champ inexistant: %s]"
    ERREUR_ORDRE_INVALIDE = "Cet ordre professionel n'est pas pris en charge."
    ERREUR_CYCLE_INVALIDE = "Le cycle entré n'est pas valide ou n'est pas pris en charge."
    ERREUR_HEURES_TRANSFEREES_TROP = \
        "Le nombre d'heure(s) tranférée(s) du dernier cycle est %d. Nombre d'heure(s) non transférée(s): %d"
    ERREUR_CATEGORIE_INVALIDE = "L'activité '%s' de la catégorie '%s' n'est pas valide."
    ERREUR_DATE_INVALIDE = "La date pour l'activité '%s' n'est pas valide."
    ERREUR_HEURES_TOTALES = \
        "Vous avez fait %d heure(s) de formation continue. Il vous manque %d heure(s) pour compléter ce cycle."
    ERREUR_ARCHITECTES_HEURES_PROJET_DE_RECHERCHE = \
        "Il vous manque %d heure(s) dans la catégorie : projet de recherche."
    ERREUR_ARCHITECTES_HEURES_GROUPE_DE_DISCUSSION = \
        "Il vous manque %d heure(s) dans la catégorie : groupe de discussion."
    ERREUR_ARCHITECTES_HEURES_GROUPE_COURS = \
        "Il vous manque %d heure(s) dans les catégories : cours, atelier, séminaire, colloque, " + \
        "conférence ou lecture dirigée."
    ERREUR_PSYCHOLOGUES_HEURES_GROUPE_COURS = "Il vous manque %d heure(s) dans la catégorie : cours."
    ERREUR_GEOLOGUES_HEURES_GROUPE_COURS = "Il vous manque %d heure(s) dans la catégorie : cours."
    ERREUR_GEOLOGUES_HEURES_GROUPE_PROJET_DE_RECHERCHE = \
        "Il vous manque %d heure(s) dans la catégorie : projet de recherche."
    ERREUR_GEOLOGUES_HEURES_GROUPE_GROUPE_DE_DISCUSSION = \
        "Il vous manque %d heure(s) dans la catégorie : groupe de discussion."
    ERREUR_HEURES_TRANSFEREES_NON_NULL = "Le fichier ne devrait pas avoir d'heures transférées."


class ConstantesNumeriques:
    LONGUEUR_NUMERO_PERMIS = 5
    LONGUEUR_MINIMUM_DESCRIPTION = 20
    DATE_DEBUT = 0
    DATE_FIN = 1


gabarit_numero_permis = {'architectes': "^([A,T])(\d{4})$",
                         'geologues': "^([A-Z][A-Z])(\d{4})$",
                         'psychologues': "^(\d{5})-(\d{2})$",
                         'podiatres': "^(\d{5})$"
}

sexe = {0,
        1,
        2}

cycles_et_balises_valides_par_ordre_professionnel = {
    'architectes': {
        'cycle_valide': {
            '2008-2010': [datetime.datetime(2008, 4, 1), datetime.datetime(2010, 7, 1)],
            '2010-2012': [datetime.datetime(2010, 4, 1), datetime.datetime(2012, 4, 1)],
            '2012-2014': [datetime.datetime(2012, 4, 1), datetime.datetime(2014, 4, 1)]
        }
    },
    'geologues': {
        'cycle_valide': {
            '2013-2016': [datetime.datetime(2013, 6, 1), datetime.datetime(2016, 6, 1)]
        }
    },
    'psychologues': {
        'cycle_valide': {
            '2010-2015': [datetime.datetime(2010, 1, 1), datetime.datetime(2015, 1, 1)]
        }
    },
    'podiatres': {
        'cycle_valide': {
            '2013-2016': [datetime.datetime(2013, 6, 1), datetime.datetime(2016, 6, 1)]
        }
    }
}

conditions_architectes = {
    '2008-2010': {
        'MIN_HEURES_TRANSFERE': 0,
        'MAX_HEURES_TRANSFERE': 7,
        'MIN_HEURES_COMPLET': 42,
        'MIN_HEURES_COURS': 17,
        'MAX_HEURES_REDACTION_PROFESSIONNELLE': 17,
        'MAX_HEURES_PROJET_DE_RECHERCHE': 23,
        'MAX_HEURES_GROUPE_DE_DISCUSSION': 17,
        'MAX_HEURES_PRESENTATION': 23
    },
    '2010-2012': {
        'MIN_HEURES_TRANSFERE': 0,
        'MAX_HEURES_TRANSFERE': 7,
        'MIN_HEURES_COMPLET': 42,
        'MIN_HEURES_COURS': 17,
        'MAX_HEURES_REDACTION_PROFESSIONNELLE': 17,
        'MAX_HEURES_PROJET_DE_RECHERCHE': 23,
        'MAX_HEURES_GROUPE_DE_DISCUSSION': 17,
        'MAX_HEURES_PRESENTATION': 23
    },
    '2012-2014': {
        'MIN_HEURES_TRANSFERE': 0,
        'MAX_HEURES_TRANSFERE': 7,
        'MIN_HEURES_COMPLET': 40,
        'MIN_HEURES_COURS': 17,
        'MAX_HEURES_REDACTION_PROFESSIONNELLE': 17,
        'MAX_HEURES_PROJET_DE_RECHERCHE': 23,
        'MAX_HEURES_GROUPE_DE_DISCUSSION': 17,
        'MAX_HEURES_PRESENTATION': 23
    }
}

conditions_geologues = {
    '2013-2016': {
        'MIN_HEURES_COMPLET': 55,
        'MIN_HEURES_COURS': 22,
        'MIN_HEURES_PROJET_DE_RECHERCHE': 3,
        'MIN_HEURES_GROUPE_DE_DISCUSSION': 1,
        'MAX_HEURES_TRANSFERE': None
    }
}

conditions_psychologues = {
    '2010-2015': {
        'MIN_HEURES_COMPLET': 90,
        'MIN_HEURES_COURS': 25,
        'MAX_HEURES_TRANSFERE': None,
        'MAX_HEURES_CONFERENCE': 15
    }
}

conditions_podiatres = {
    '2013-2016': {
        'MIN_HEURES_COMPLET': 60,
        'MIN_HEURES_COURS': 22,
        'MIN_HEURES_PROJET_DE_RECHERCHE': 3,
        'MIN_HEURES_GROUPE_DE_DISCUSSION': 1,
        'MAX_HEURES_TRANSFERE': None
    }
}