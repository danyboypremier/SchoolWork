
/*
 *                   Sequences.c                        
 * ---------------------------------------------------
 * - Classe d'objets
 * - permet de contenir une suite d'element, les
 *   ajouts et suppressions sont fait a la fin (queue) ou
 *   au debut (tete).  Tout les elements peuvent etre
 *   consultes.
 * ---------------------------------------------------
 * auteur : Bruno Malenfant
 * date : 1996 - 2008
 */


#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include "Sequences.h"


typedef struct _noeud Noeud;

struct _noeud
{
  Element element;
  Noeud * suivant;
};


struct _sequence
{
  // Champs de base pour la Sequence :
  // un pointeur de tete et un de queue.

  int nbElement;
  Noeud * elementTete;
  Noeud * elementQueue;
  int fin_ok;

  // Champs pour optimiser certaine recherche dans la 
  // Sequence.

  int positionAccesRapide;
  Noeud * elementAccesRapide;

  // Champs pour l'iterateur.

  int positionIterateur;
  Noeud * elementCourrant;
};



/* 
 * ---------------------------------------------------
 * Routine de traitement interne :
 */

/*
 * initialise la sequence a 0 element.
 */
void initialiserSequence( Sequence * a_seq ) 
{
  assert( NULL != a_seq &&
     	  "Sequences : initialiserSequence : argument NULL." );

  a_seq->nbElement = 0;
  a_seq->positionAccesRapide = a_seq->positionIterateur = -1;
  a_seq->elementTete = a_seq->elementQueue = NULL;
  a_seq->elementAccesRapide = a_seq->elementCourrant = NULL;
  a_seq->fin_ok = 0;
}


/* 
 * pour utiliser amenerQueueALaFin, il doit y avoir au moins
 * un element dans la liste.
 */
void amenerQueueALaFin( Sequence * a_seq ) 
{
  assert( NULL != a_seq &&
     	  "Sequences : amenerQueueALaFin : argument NULL." );

  int i = 0;

  a_seq->elementQueue = a_seq->elementTete;

  for( i = 1; i < a_seq->nbElement; i++ )
  {
    a_seq->elementQueue = a_seq->elementQueue->suivant;
  }
  a_seq->fin_ok = 1;
}



/* 
 * ---------------------------------------------------
 * Constructeur, Destructeur :
 */

Sequence * creer_Seq()
{
  Sequence * nouvelleSequence = ( Sequence * )malloc( sizeof ( Sequence ) );

  if( NULL == nouvelleSequence ) 
  {
    fprintf( stderr, "Sequences : creer_Seq : erreur d'allocation.\n" );
    exit( -1 );
  }

  initialiserSequence( nouvelleSequence );

  return nouvelleSequence;
}



void detruire_Seq( Sequence * a_seq )
{
  assert( NULL != a_seq &&
     	  "Sequences : detruireSequence : argument NULL." );

  int i = 0;
  Noeud * suivant = a_seq->elementTete;

  for ( i = 0; i < a_seq->nbElement; i++ )
  {
    Noeud * courrant = suivant;
    suivant = suivant->suivant;
    free( courrant );
  }

  free( a_seq );
}



/*
 * ---------------------------------------------------
 * Fonctions de consultation :
 */

int nbElements_Seq( Sequence * a_seq )
{
  assert( NULL != a_seq &&
     	  "Sequences : nbElements_Seq : argument NULL." );

  return a_seq->nbElement;
}



Element kiemeElement_Seq( Sequence * a_seq, int a_k )
{
  assert( NULL != a_seq &&
     	  "Sequences : kiemeElement_Seq : argument NULL." );
  assert( 0 <= a_k && a_k < a_seq->nbElement &&
     	  "Sequences : kiemeElement_Seq : indice hors Sequence." );

  Element retour = NULL;
  
  if( ( -1 == a_seq->positionAccesRapide ) 
       || 
      ( a_seq->positionAccesRapide > a_k )
    )
  {
    a_seq->positionAccesRapide = 0;
    a_seq->elementAccesRapide = a_seq->elementTete;
  }

  while( a_seq->positionAccesRapide != a_k )
  {
    a_seq->elementAccesRapide = a_seq->elementAccesRapide->suivant;
    ( a_seq->positionAccesRapide )++;
  }
  retour = a_seq->elementAccesRapide->element;
  
  if( a_seq->positionAccesRapide == ( a_seq->nbElement - 1 ) )
  {
    a_seq->elementQueue = a_seq->elementAccesRapide;
    a_seq->fin_ok = 1;
  }
  
  return retour;
}



/*
 * ---------------------------------------------------
 * Procedures de modification :
 */

void ajouterEnTete_Seq( Sequence * a_seq, Element a_element )
{
  assert( NULL != a_seq &&
     	  "Sequences : ajouterEnTete_Seq : argument NULL." );
  
  Noeud * nouveauNoeud = ( Noeud * )malloc( sizeof( Noeud ) );

  if( NULL == nouveauNoeud ) 
  {
    fprintf( stderr, "Sequences : ajouterEnTete_Seq : erreur d'allocation.\n" );
    exit( -1 );
  }

  nouveauNoeud->element = a_element;
  nouveauNoeud->suivant = a_seq->elementTete;
  a_seq->elementTete = nouveauNoeud;

  if( 0 == a_seq->nbElement ) 
  {
    a_seq->elementQueue = a_seq->elementTete;
    a_seq->fin_ok = 1;
  }

  if( -1 != a_seq->positionAccesRapide ) 
  {
    ( a_seq->positionAccesRapide )++;
  }
  if( -1 != a_seq->positionIterateur ) 
  {
    ( a_seq->positionIterateur )++;
  }

  ( a_seq->nbElement )++;
}



void ajouterEnQueue_Seq( Sequence * a_seq, Element a_element )
{
  assert( NULL != a_seq &&
     	  "Sequences : ajouterEnQueue_Seq : argument NULL." );

  if( 0 == a_seq->nbElement )
  {
    ajouterEnTete_Seq( a_seq, a_element );
  }
  else
  {
    Noeud * nouveauNoeud = ( Noeud * )malloc( sizeof( Noeud ) );

    if( NULL == nouveauNoeud ) 
    {
      fprintf( stderr, "Sequences : ajouterEnQueue_Seq : erreur d'allocation.\n" );
      exit( -1 );
    }

    nouveauNoeud->element = a_element;
    nouveauNoeud->suivant = NULL;

    if( ! a_seq->fin_ok )
    {
      amenerQueueALaFin( a_seq );
    }

    a_seq->elementQueue->suivant = nouveauNoeud;
    a_seq->elementQueue = nouveauNoeud;
    ( a_seq->nbElement )++;
  }
}



void retirerDeTete_Seq( Sequence * a_seq )
{
  assert( NULL != a_seq &&
     	  "Sequences : retirerDeTete_Seq : argument NULL." );

  if( 1 == a_seq->nbElement )
  {
    free( a_seq->elementTete );
    initialiserSequence( a_seq );
  }
  if( 1 < a_seq->nbElement )
  {
    Noeud * elementSupprime = a_seq->elementTete;
    a_seq->elementTete = elementSupprime->suivant;

    if( -1 != a_seq->positionAccesRapide ) 
    {
      ( a_seq->positionAccesRapide )--;
    }
    if( -1 != a_seq->positionIterateur ) 
    {
      ( a_seq->positionIterateur )--;
    }
    free( elementSupprime );
    ( a_seq->nbElement )--;
  }
}



void retirerDeQueue_Seq( Sequence * a_seq )
{
  assert( NULL != a_seq &&
     	  "Sequences : retirerDeQueue_Seq : argument NULL." );

  if( 1 == a_seq->nbElement )
  {
    free( a_seq->elementTete );
    initialiserSequence( a_seq );
  }
  if( 1 < a_seq->nbElement )
  {
    if( a_seq->positionAccesRapide == ( a_seq->nbElement - 1 ) ) 
    {
      a_seq->positionAccesRapide = -1;
    }
    if( a_seq->positionIterateur == ( a_seq->nbElement - 1 ) ) 
    {
      a_seq->positionIterateur = -1;
    }
    if( ! a_seq->fin_ok ) 
    {
      amenerQueueALaFin( a_seq );
    }

    free( a_seq->elementQueue );

    ( a_seq->nbElement )--;
    if( a_seq->positionAccesRapide == ( a_seq->nbElement - 1 ) )
    {
      a_seq->elementQueue = a_seq->elementAccesRapide;
      a_seq->fin_ok = 1;
    }
    else
    {
      a_seq->fin_ok = 0;
    }
  }
}



/*
 * ---------------------------------------------------
 * Iterateur :
 */

void initIterateur_Seq( Sequence * a_seq )
{
  assert( NULL != a_seq &&
     	  "Sequences : initIterateur_Seq : argument NULL." );

  a_seq->positionIterateur = -1;
  a_seq->elementCourrant = NULL;
}



int prochainElement_Seq( Sequence * a_seq, Element * a_element )
{
  assert( NULL != a_seq &&
	  NULL != a_element &&
     	  "Sequences : prochainElement_Seq : argument NULL." );

  int estALaFin = 0;
  
  ( a_seq->positionIterateur )++;
  if( a_seq->positionIterateur != a_seq->nbElement )
  {
    if( 0 == a_seq->positionIterateur )
    {
      a_seq->elementCourrant = a_seq->elementTete;
    }
    else
    {
      a_seq->elementCourrant = a_seq->elementCourrant->suivant;
    }
    estALaFin = 1;
    *a_element = a_seq->elementCourrant->element;
  }
  
  return estALaFin;
}
