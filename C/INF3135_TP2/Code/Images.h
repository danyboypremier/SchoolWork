
#ifndef IMAGES_H
#define IMAGES_H

#include "Couleurs.h"

/** @name Images */
//@{

//@Include: Images.c

/**
 * @name Module Images.
 * @memo Classe d'objets.
 * @doc
 * Ce module definie un type de donnees pouvant contenir et manipuler une
 * image couleur.
 * @author Bruno Malenfant
 */
;

/**
 * (Images_h) Definition d'une classe d'images, certains champs de cette
 * classe sont accessible par des fonctions (taille_x et taille_y).
 */
typedef struct _image Image;

/**
 * (Images_h) Construit une nouvelle image.
 * @return
 *   retourne une image taille a_taille_x par a_taille_y.
 *   cette image est noire initialement.
 * @postcondition
 *   ne retourne pas de pointeur NULL.
 * @param
 *   a_taille_x (int) largeur de l'image
 * @precondition
 *   a_taille_x > 0
 * @param
 *   a_taille_y (int) hauteur de l'image
 * @precondition
 *   a_taille_y > 0
 * @param
 *   a_surEchantillonage (int) largeur du sur echantillonage.
 * @precondition
 *   a_surEchantillonage > 0
 */
Image *creerImage( int a_taille_x, int a_taille_y, int a_surEchantillonage );

/**
 * (Images_h) Retourne la largeur de l'image.
 * @return
 *   retourne un entier representant la largeur de l'image.
 * @param
 *   image (Image *) un pointeur sur une image valide.
 * @precondition
 *   image != NULL
 */
int tailleX( Image * image );

/**
 * (Images_h) Retourne la hauteur de l'image.
 * @return
 *   retourne un entier representant la hauteur de l'image.
 * @param
 *   image (Image *) un pointeur sur une image valide.
 * @precondition
 *   image != NULL
 */
int tailleY( Image * image );

/**
 * (Images_h) Enregistre l'image dans un fichier.  Le format PPM
 * est utilise pour ce fichier.
 * @param
 *   image (Image *) l'image a sauvegarder.
 * @precondition
 *   image != NULL
 * @param
 *   nom (char *) nom du fichier PPM pour la sauvegarde de l'image.
 * @precondition
 *   nom != NULL
 */
void sauvegarderImage( Image * image, char * nom );
 
/**
 * (Images_h) Effectue une correction selon la composante alpha des couleurs
 * d'une image.  Cette correction utilise la procedure 'correctionAlpha' du
 * module Couleurs.
 * @param
 *   image (Image *) un pointeur sur une image a corriger.
 * @precondition
 *   image != NULL
 */
void convertionAlpha( Image * image );

/**
 * (Images_h) Ajoute une couleur a l'image.  Cette couleur est ajoute a la
 * couleur presente dans l'image.  La composante alpha est aussi ajoute.
 * Dans ce cas la routine de convertionAlpha devra etre
 * utilise pour ramener les composante alpha a 1.
 * @param 
 *   image (Image *) l'image sur laquelle la couleur est ajoute.
 * @param
 *   x (int) position en x du point a modifier.
 * @precondition
 *   0 <= x < tailleX
 * @param
 *   y (int) position en y du point a modifier.
 * @precondition
 *   0 <= y < tailleY
 * @param
 *   couleur (Couleur) valeur de la couleur a ajouter.
 */
void additionnerCouleur( Image * image, int x, int y, 
			 Couleur couleur );


/**
 * (Images_h) Ajoute une couleur a l'image.  Cette couleur est ajoute a la
 * couleur presente dans l'image.  La composante alpha est aussi ajoute.
 * Dans ce cas la routine de convertionAlpha devra etre
 * utilise pour ramener les composante alpha a 1.
 * Les coordonnees represente une image de -1 a 1 sur les deux axes.
 * Si les coordonnees sont a l'exterieur de l'image alors il n'y a 
 * aucune modification a l'image.
 * @param 
 *   image (Image *) l'image sur laquelle la couleur est ajoute.
 * @param
 *   x (float) position en x du point a modifier.
 * @param
 *   y (float) position en y du point a modifier.
 * @param
 *   couleur (Couleur) valeur de la couleur a ajouter.
 */
void additionnerCouleurReel( Image * image, float x, float y, 
			     Couleur couleur );

//@}

#endif
