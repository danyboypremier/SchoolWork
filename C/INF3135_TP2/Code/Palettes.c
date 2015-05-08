
#include "Palettes.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

Palette * lirePalette( char * a_nomFichier ) {
  assert( NULL != a_nomFichier );

  Palette * resultat = creerPalette();

  FILE * fichierCouleur = fopen( a_nomFichier, "r" );
  if( NULL == fichierCouleur ) {
    fprintf( stderr, "Palettes : lirePalette erreur lors de louverture du fichier.\n" );
    exit( -1 );
  }

  do {
    double rouge, vert, bleu;
    int n = fscanf( fichierCouleur, "%lf %lf %lf", &rouge, &vert, &bleu );
    if( 3 == n ) {
      Couleur * couleur = ( Couleur * ) malloc( sizeof( Couleur ) );
      if( NULL == couleur ) {
        fprintf( stderr, "Palettes : lirePalette : erreur d'allocation.\n" );
	exit( -1 );
      }

      couleur->rouge = rouge;
      couleur->vert  = vert;
      couleur->bleu  = bleu;
      couleur->alpha = 1;

      ajouterCouleur( resultat, couleur );
    } else if ( n != -1 ) {
      fprintf( stderr, "Palettes : lirePalette : erreur de lecture dans le fichier de couleur.\n" );
      exit( -1 );
    }
  } while( ! feof( fichierCouleur ) );

  return resultat;
}

Palette * construirePalette(double qtRouge, double qtVert, double qtBleu) {
  Palette * resultat = creerPalette();
  Couleur * couleur = ( Couleur * )malloc( sizeof( Couleur ) );

  if( NULL == couleur ) {
    fprintf( stderr, "Palettes : construirePaletteBlanche : erreur d'allocation.\n" );
    exit( -1 );
  }

  couleur->rouge = qtRouge;
  couleur->vert  = qtVert;
  couleur->bleu  = qtBleu;
  couleur->alpha = 1.0;

  int i = 0;
  for( i = 0; i < 256 ; i++ ) {
    ajouterCouleur( resultat, couleur );
  }
  return resultat;
}
