
#ifndef COULEURS_H
#define COULEURS_H

//@Include: Couleurs.c

/** @name Couleur */
//@{

/**
 * @name Module Couleurs.
 * @memo Classe d'objets.
 * @doc
 * Ce module sert de contenant pour une couleur de type rgb.  Une composante 
 * alpha est ajoute pour l'utilisateur.  
 * @author Bruno Malenfant
 */
;

/**
 * (Couleurs_h) Structure contenant l'information pour la classe d'objet.
 * Les champs sont publiques, aucun accesseur n'existe.
 */
struct _couleur {
  /**
   *   rouge (double) composante rouge de la couleur.
   */
  double rouge;

  /**
   *   vert (double) composante verte de la couleur.
   */
  double vert;

  /**
   *   bleu (double) composante bleu de la couleur.
   */
  double bleu;

  /**
   *   alpha (double) composante alpha de la couleur, est utilise par la routine
   *   de correction pour remener les autres composantes entre 0 et 1.
   */
  double alpha;
};

/**
 * (Couleur_h) Definition de la structure de couleur.
 */
typedef struct _couleur Couleur;

/**
 * (Couleurs_h) Addition de 2 couleurs pour obtenir une troisieme couleur.
 * @return
 *   Le resultat de cette addition peu donner des valeurs plus grande que 1
 *   pour les champs rouge, vert, bleu et alpha.
 * @param
 *   couleur1 (Couleur) une premiere couleur.
 * @param
 *   couleur2 (Couleur) une deuxieme couleur.
 */
Couleur additionner( Couleur couleur1, Couleur couleur2 );

/**
 * (Couleurs_h) Effectue une correction sur chaque champs de la couleur.
 * @return
 *   Le resultat est une couleur qui a ete corrige selon le facteur suivant :
 *   log( alpha ) / ( alpha * log( max ) ).
 * @postcondition
 *   0 <= rouge <= 1
 * @postcondition
 *   0 <= vert <= 1
 * @postcondition
 *   0 <= bleu <= 1 
 * @postcondition
 *   alpha == 1
 * @param
 *   couleur (Couleur) la couleur a corriger.
 * @precondition
 *   0 <= alpha
 * @param
 *   max (double) une valeur qui equivaut au 1 d'une composante.
 * @precondition
 *   1 <= max
 */
Couleur correctionAlpha( Couleur couleur , double max );

//@}

#endif
