
#ifndef FONCTION_NON_LINEAIRE_H
#define FONCTION_NON_LINEAIRE_H

#include "Points.h"

/** @name Fonction Non Lineaires */
//@{

//@Include: FonctionNonLineaires.c

/**
 * @name Module FonctionNonLineaires.
 * @memo Bibliotheque de routines.
 * @doc
 * Plusieurs fonctions de transformation non lineaires sont decrites dans 
 * ce module.
 * @author Bruno Malenfant
 */
;

/** 
 * (FonctionNonLineaires_h) Definition d'un type de donnees decrivant une
 * fonction non-lineaire sous forme d'un pointeur de fonction.  Une fonction
 * non-lineaire transforme un Point vers un autre Point.
 */
typedef Point FonctionNonLineaire( Point );

/**
 * (FonctionNonLineaires_h) fonction de traduction d'une chaine de caracteres en
 * un pointeur de fonction non lineaire.
 * @return
 *   un pointeur sur une fonction non lineaire.
 * @postcondition
 *   resultat non NULL.
 * @param
 *   a_nomFonction (char *) une chaine de caractere contenant le nom
 *   d'une fonction non lineaire.
 * @precondition
 *   a_nomFonction != NULL;
 */
FonctionNonLineaire * chaineAFonction( char * a_nomFonction );

/** 
 * (FonctionNonLineaires_h) Identite.
 * @return
 *   $( x, y )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_lineaire( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \sin( x ), \sin( y ) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_sinusoidale( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \frac{x}{r^2}, \frac{y}{r^2} )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_spherique( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( r \cdot \cos( \theta + r), r \cdot \sin( \theta + r ) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_galaxy( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( r \cdot \cos( 2 \theta, r \cdot \sin( 2 \theta) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_feracheval( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \frac{\theta}{\pi}, r - 1 )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_polaire( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( r \cdot sin( r + \theta ), r \cdot \cos( \theta - r ) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_trapeze( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( r \cdot \sin( r \theta ), -r \cdot \cos( r \theta ) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_coeur( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \frac{\theta \cdot \sin( \pi r )}{\pi}, \frac{\theta \cdot \cos( \pi r )}{\pi} )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_disque( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \frac{\cos(\theta) + \sin(r)}{r}, \frac{\sin(\theta) - \cos(r)}{r} )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_spirale( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \frac{\sin(\theta)}{r}, r \cdot \cos(\theta) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_hyperbolique( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \sin(\theta) \cdot \cos(r), \cos(\theta) \cdot \sin(r) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_diamand( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( r \cdot \sin^3(\theta + r), r \cdot \cos^3( \theta - r ) )$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_ex( Point );

/** 
 * (FonctionNonLineaires_h)
 * @return
 *   $( \sqrt{r} \cdot \cos(\frac{\theta}{2} + \Omega), \sqrt{r} \cdot \sin(\frac{\theta}{2} + \Omega) )$
 *   ou $\Omega$ est choisi aleatoirement parmi $\{0, \pi\}$
 * @param
 *   point (Point) un point a transformer.
 */
Point fnl_julia( Point );

//@}

#endif
