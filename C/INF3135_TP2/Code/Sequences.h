
/*
 *                   Sequences.h                        
 * ---------------------------------------------------
 * - Classe d'objets
 * - permet de contenir une suite d'element, les
 *   ajouts et suppressions sont fait a la fin ou
 *   au debut.  Tout les elements peuvent etre
 *   consultes.  Les elements sont de type generique
 *   (void *) et leurs allocations doit etre faites
 *   avant leurs ajout.
 * ---------------------------------------------------
 * auteur : Bruno Malenfant
 * date : 1996 - 2008
 */


#ifndef SEQUENCES_H
#define SEQUENCES_H



/*
 * ---------------------------------------------------
 * Definition des types :
 */

typedef void * Element;

typedef struct _sequence Sequence;




/* 
 * ---------------------------------------------------
 * Constructeur, Destructeur :
 */

/*
 * Sequence * creer_Seq()
 *
 * retourne une nouvelle Sequence vide.
 *
 * O(1)
 */
Sequence * creer_Seq();

/*
 * detruire_Seq( Sequence * seq )
 *
 * desaloue la Sequence en arguements, les elements
 * de la Sequence ne seront pas desalloues.
 * (desallocation faible)
 *
 * O(n)
 */
void detruire_Seq( Sequence * seq );



/*
 * ---------------------------------------------------
 * Fonctions de consultation :
 */

/*
 * int nbElements_Seq( Sequence * seq )
 *
 * retourne le nombre d'elements de la Sequence
 *
 * O(1)
 */
int nbElements_Seq( Sequence * seq );

/*
 * Element kiemeElement_Seq( Sequence * seq, int k )
 *
 * retourne le kieme element de la Sequence.
 * k doit etre comprit dans l'interval 0..n-1, 
 * ou 'n' est le nombre d'element de la Sequence.
 *
 * pire cas : O(n)
 * meilleur cas : O(1)
 */
Element kiemeElement_Seq( Sequence * seq, int k );



/*
 * ---------------------------------------------------
 * Procedures de modification :
 */

/*
 * ajouterEnTete_Seq( Sequence * seq, Element e )
 *
 * ajoute l'element en tete de la Sequence.
 * (l'element ajoute devient l'element 0,
 *  les autres montent d'une position vers
 *  l'indice suivant.)
 *
 * O(1)
 */
void ajouterEnTete_Seq( Sequence * seq, Element e );

/*
 * ajouterEnQueue_Seq( Sequence * seq, Element e )
 *
 * ajoute l'element a la fin de la Sequence.
 * (L'element ajoute devient l'element n)
 *
 * pire cas : O(n)
 * meilleur cas : O(1)
 * la structure de donne tente de garder la fin de
 * la liste, tant que l'element de queue n'est pas
 * retirer, un ordre constant est garantie pour 
 * ajouterEnQueue.
 */
void ajouterEnQueue_Seq( Sequence * seq, Element e );

/*
 * retirerDeTete_Seq( Sequence * seq )
 *
 * Enleve le premier element de la Sequence.
 *
 * O(1)
 */
void retirerDeTete_Seq( Sequence * seq );

/*
 * retirerDeQueue_Seq( Sequence * seq );
 *
 * Enleve le dernier element de la Sequence.
 *
 * pire cas : O(n)
 * meilleur cas : O(1)
 * si un element est enlever immidiatement apres un
 * ajout, O(1), sinon, dans la plupart des cas, cela
 * ne peut pas etre garantie.
 */
void retirerDeQueue_Seq( Sequence * seq );



/*
 * ---------------------------------------------------
 * Iterateur :
 */


/* exemple d'utilisation de l'iterateur pour 
 * parcourir la Sequence:  La Sequence sera 
 * parcourue a partir de l'element de tete,
 * vers l'element de queue.

   Sequence * seq;
   Element e;
   ...
   initIterateur_Seq( seq );
   while( prochainElement_Seq( seq, &e ) )
   {
       ...
   }
 */

/*
 * initIterateur_Seq( Sequence * seq );
 * 
 * Prepare l'iterateur interne de la structure 
 * Sequence en arguement.
 * Donc un seul iterateur par sequence peut etre
 * utilise en meme temps.
 * il est conseille de ne pas modifier la sequence lors 
 * d'un parcours.
 *
 * O(1)
 */
void initIterateur_Seq( Sequence * seq );

/*
 * int prochainElement_Seq( Sequence * seq, Element * e )
 *
 * Procedure-fonction
 * Cette procedure passe l'iterateur au prochain element
 * et donne une reference a cette element en argument.
 * Elle retourne vrai si l'iterateur est arriver
 * a la fin.
 * O(1)
 */
int prochainElement_Seq( Sequence * seq, Element * e );




#endif
