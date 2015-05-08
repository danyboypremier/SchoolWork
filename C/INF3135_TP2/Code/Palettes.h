
#ifndef PALETTES_H
#define PALETTES_H

#include "Sequences.h"
#include "Couleurs.h"

/** @name Palettes */
//@{

//@Include: Palettes.c

/**
 * @name Module Palettes.
 * @memo Classe d'objets.
 * @doc
 * Ce module sert de contenant pour palette de couleur.
 * Chaque couleur contenu sera associe a une valeur dependant de l'ordre
 * d'insertion des couleurs.  La premiere couleur aura la valeur 0, la
 * seconde aura la couleur 1, et ainsi de suite.
 * @author Bruno Malenfant
 */
;

/**
 * (Palettes_h) Definition du type Palette, une palette est equivalente
 * a une Sequence de Couleur.
 */
typedef Sequence Palette;

/**
 * (Palettes_h) Construit une Palette vide.
 * @return
 *   retourne un pointeur sur une Palette vide.
 * @postcondition
 *   retourne un pointeur non NULL
 */
#define creerPalette ( Palette * )creer_Seq

/**
 * (Palettes_h) accede a la k iem couleur de la palette.
 * @return
 *   Un pointeur sur une la k iem couleur de la palette.
 * @param
 *   palette (Palette) une palette de couleur.
 * @precondition
 *   palette != NULL
 * @param
 *   k (int) le numero de la couleur a trouver.
 * @precondition
 *   0 <= k < taille de la palette.
 */
#define kiemeCouleur( palette, k ) ( Couleur * )kiemeElement_Seq( palette, k )

/**
 * (Palettes_h) ajouter une couleur dans la palette, cette couleur aura la
 * position egale a la taille de la palette avant l'insertion.  La taille
 * de la palette sera ensuite incremente de 1.
 * @param
 *   palette (Palette) une palette de couleur.
 * @precondition
 *   palette != NULL
 * @param
 *   couleur (Couleur *) un pointeur sur une couleur.
 */
#define ajouterCouleur( palette, couleur ) ajouterEnQueue_Seq( palette, (Element) couleur )

/**
 * (Palettes_h) permet de charger une palette a partir du contenu d'un 
 * fichier.  Le fichier doit contenir une suite de couleur, a une couleur
 * par ligne.  Chaque couleur aura les valeur rouge, vert, bleu sous forme
 * d'un double.  Les composantes alpha seront place a 1.
 * @return 
 *   Un pointeur sur la palette construite par la procedure.
 * @postcondition
 *   Le pointeur n'est pas NULL.
 * @param
 *   nom (char *) le nom du fichier contenant la palette a lire.
 * @precondition
 *   nom != NULL
 *   le fichier existe.
 */
Palette * lirePalette( char * nom );

/**
 * (Palettes_h) fonction pour construire la palette avec les valeur RGB
 * @return 
 *   un pointeur sur une palette de 256 couleurs.
 * @postcondition
 *   n'est pas NULL.
 */
Palette * construirePalette(double qtRouge, double qtVert, double qtBleu);
//@}

#endif
