# -*- coding: utf-8 -*-

from constantes import Messages as Msg
import classes
import validation
import sys
import json
import statistiques as Stats


'''
    Ce fichier contient les méthodes du programme principal servant à valider les heures des activités de 
    formation d'un ordre professionnel pour un cycle déterminé selon les conditions de cet ordre 
    professionel.  Les informations sont fournies dans un fichier source sous format JSON et les résultats 
    sont inscrits dans un fichier de sortie sous format JSON.
    
    Usage du programme:             python main.py <fichierentree> <fichiersortie>
    Consulter les statistiques:     python main.py -S
    Réinitialiser les statistiques: python main.py -SR
'''


def main():
    try:
        executer_programme_selon_arguments()
    except Exception as e:
        print e


def executer_programme_selon_arguments():
    nb_arguments = len(sys.argv)
    if nb_arguments == 3:
        executer_programme_principal()
    elif nb_arguments == 2 and sys.argv[1] == "-S":
        Stats.afficher()
    elif nb_arguments == 2 and sys.argv[1] == "-SR":
        Stats.reinitialiser()
        print Msg.STATS_REMISES_A_0
    else:
        print Msg.USAGE.format(sys.argv[0])


def executer_programme_principal():
    try:
        fichiers = lire_nom_fichier_entree_et_sortie()
        membre = lire_json_dans_membre(fichiers['entree'])
        resultat_validation = instancier_validation_dynamiquement_selon_ordre(membre)
        ecrire_resultat_en_json(fichiers['sortie'], resultat_validation.rapport)
        ajouter_membre_valide_dans_statistiques(membre, resultat_validation)
    except ErreurUtilisation as e:
        print e.message
    except KeyError as e:
        traiter_exception_fichier_invalide(fichiers['sortie'], Msg.ERREUR_CYCLE_INVALIDE)
    except validation.ExceptionFichierEntreeInvalide as e:
        traiter_exception_fichier_invalide(fichiers['sortie'], e.message)


def lire_nom_fichier_entree_et_sortie():
    return {'entree': sys.argv[1],
            'sortie': sys.argv[2]}


def lire_json_dans_membre(nom_fichier_entree):
    try:
        with open(nom_fichier_entree) as fichier_json:
            membre_retour = classes.Membre(json.load(fichier_json))
    except KeyError as e:
        raise validation.ExceptionFichierEntreeInvalide(Msg.ERREUR_CHAMP_MANQUANT % e.message)
    except IOError:
        raise ErreurUtilisation(Msg.ERREUR_LECTURE)
    except ValueError as e:
        raise validation.ExceptionFichierEntreeInvalide(Msg.ERREUR_DATE_INVALIDE % e.message)
    except TypeError:
        raise validation.ExceptionFichierEntreeInvalide(Msg.ERREUR_HEURES_TRANSFEREES_INVALIDE)
    return membre_retour


def instancier_validation_dynamiquement_selon_ordre(membre):
    try:
        ordre = membre.ordre
        ordre = ordre.title()
        ClasseDynamiqueValidationSelonOrdre = getattr(validation, ordre)
        return ClasseDynamiqueValidationSelonOrdre(membre)
    except AttributeError:
        raise validation.ExceptionFichierEntreeInvalide(Msg.ERREUR_ORDRE_INVALIDE)


def ecrire_resultat_en_json(nom_fichier_sortie, resultat_validation):
    try:
        fichier_sortie = open(nom_fichier_sortie, 'w')
    except IOError:
        raise ErreurUtilisation(Msg.ERREUR_ECRITURE)
    json.dump(resultat_validation.generer_dictionnaire_jsonable(), fichier_sortie, indent=4, ensure_ascii=False)


def ajouter_membre_valide_dans_statistiques(membre, resultat_validation):
    if resultat_validation.rapport.est_complet:
        Stats.ajouter_membre_valide_complet(membre)
    else:
        Stats.ajouter_membre_valide_incomplet(membre)


def traiter_exception_fichier_invalide(fichier_sortie, message_erreur):
    print Msg.ERREUR_FICHIER_ENTREE_INVALIDE + message_erreur
    rapport = classes.Rapport()
    rapport.ajouter_erreurs(Msg.ERREUR_FICHIER_ENTREE_INVALIDE + message_erreur)
    ecrire_resultat_en_json(fichier_sortie, rapport)
    if (message_erreur == Msg.ERREUR_NUMERO_PERMIS_INVALIDE):
        Stats.ajouter_membre_numero_permis_invalide()
    else:
        Stats.ajouter_membre_invalide()


class ErreurUtilisation(Exception):
    pass


if __name__ == '__main__':
    main()