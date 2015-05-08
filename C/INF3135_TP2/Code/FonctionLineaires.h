
#ifndef FONCTION_LINEAIRE_H
#define FONCTION_LINEAIRE_H

#include <stdio.h>
#include "Points.h"

/** @name Fonction Lineaires */
//@{

//@Include: FonctionLineaires.c

/**
 * @name Module FonctionLineaires.
 * @memo Classe d'objets.
 * @doc
 * Contient la description des fonctions linéaires a 2 dimensions.
 * @author Bruno Malenfant
 */
;

/**
 * (FonctionLineaires_h) Definition de la classe d'objet, les champs
 * sont privees.
 */
typedef struct _fonctionLineaire FonctionLineaire;

/**
 * (FonctionLineaires_h) Constructeur de fonction lineaire.
 * @return
 *   Un pointeur sur une structure de fonction lineaire.
 * @postcondition
 *   Le pointeur n'est pas NULL.
 * @param
 *   a (double) coeificient de x pour le calcul de x
 * @param
 *   b (double) coeificient de y pour le calcul de x
 * @param
 *   c (double) coeificient de x pour le calcul de y
 * @param
 *   d (double) coeificient de y pour le calcul de y
 * @param
 *   e (double) constante ajoute pour le calcul de x
 * @param
 *   f (double) constante ajoute pour le calcul de y
 * @param
 *   noCouleur (int) numero identifiant la couleur associe a cette 
 *   transformation lineaire.
 * @precondition
 *   0 <= noCouleur <= 255
 */
FonctionLineaire * creerFonctionLineaire( double a, double b, double c, 
					  double d, double e, double f, 
					  int noCouleur );

/**
 * (FonctionLineaires_h) affiche les champs d'une fonction lineaire,
 * utile pour trouver des erreurs.
 * @param
 *   fonctionNL (FonctionLineaire *) un pointeur sur une fonction lineaire.
 * @precondition
 *   fonctionNL != NULL
 */
void afficherFonctionLineaire( FonctionLineaire * fonctionNL );

/**
 * (FonctionLineaires_h) Transforme un Point a l'aide d'une transforme
 * lineaire.
 * @return
 *   Un point contenant le resultat de l'application de la fonction lineaire.
 * @postcondition
 *   x = a x + b y + e
 * @postcondition
 *   y = c x + d y + f 
 * @param
 *   fonctionNL (FonctionLineaire *) un pointeur sur la fonction lineaire a 
 *   appliquer.
 * @precondition
 *   fonctionNL != NULL
 * @param
 *   point (Point) le point sur lequel la transforme lineaire sera applique.
 */
Point appliquerFonctionLineaire( FonctionLineaire * fonctionNL, Point point );

/**
 * (FonctionLineaires_h) accesseur : retourne le numero de la couleur 
 * associer a une fonction lineaire.
 * @return 
 *   le numero de la couleur associe.
 * @postcondition
 *   0 <= couleur <= 255
 * @param
 *   fonctionNL (FonctionLineaire *) un pointeur sur la fonction lineaire.
 * @precondition
 *   fonctionNL != NULL
 */
int noCouleurFonction( FonctionLineaire * fonctionNL );

//@}

#endif
