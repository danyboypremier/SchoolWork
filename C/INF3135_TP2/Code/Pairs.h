
#ifndef PAIRS_H
#define PAIRS_H

/** @name Pairs */
//@{

//@Include: Pairs.c

/**
 * @name Module Pairs.
 * @memo Classe d'objets.
 * @doc
 * Ce module decrit la structure d'une pair d'elements.
 * Les elements sont des pointeurs 'void'.
 * Ils sont identifies par les champs 'premier' et 'deuxieme'.
 * @author Bruno Malenfant
 */
;

 
/**
 * (Pairs_h) Structure contenant les elements
 * d'une pair.
 */
struct _pair {
  /**
   *   premier (void *) premier element.
   */
  void * premier;

  /**
   *   deuxieme (void *) deuxieme element.
   */
  void * deuxieme;
};

/**
 * (Pairs_h) Pointeur sur une structure _pair.
 */
typedef struct _pair * Pair;


/**
 * (Pairs_h) Construit une pair avec les elements fournis.
 * @param
 *    a_premier (void *) premier element.
 * @param
 *   a_deuxieme (void *) deuxieme element.
 * @return
 *   Une structure Pair contenant les elements
 *   en entrees.  Si l'allocation ne fonctionne pas
 *   alors NULL est retourne.
 * @exception
 *   Si l'allocation ne fonctionne pas alors 
 *   0 est place dans 'allocationReussit.
 *   Sinon 1 est place.
 */
Pair creerPair( void * a_premier, void * a_deuxieme,
		int *a_allocationReussit );

/**
 * (Pairs_h) Constructeur de copie.
 * @param
 *   a_pair (Pair) La structure a copier.
 * @precondition
 *   a_pair != NULL.
 * @return
 *   Une copie de la pair recu.
 *   NULL si l'allocation ne reussit pas.
 * @exception
 *   allocationReussit :
 *   Si l'allocation ne fonctionne pas alors 
 *   0 est place dans 'allocationReussit'.
 *   Sinon 1 est place.
 */
Pair copierPair( Pair a_pair,
		 int *a_allocationReussit );

//@}

#endif
