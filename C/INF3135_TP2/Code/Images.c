
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "Images.h"
#include "Points.h"

/**
 * (Images_c) Structure contenant une image.
 */
struct _image {
  /**
   *   taille_x (int) largeur de l'image.
   */
  int taille_x;

  /**
   *   taille_y (int) hauteur de l'image.
   */
  int taille_y;

  /**
   *   surEchantillonage (int) largeur (et hauteur) du sur echantillonage.
   */
  int surEchantillonage;
  
  /**
   *   image (Couleur *) tableau une dimension contenant les points de 
   *   l'image.  Pour reconstruire la matrice la formule suivante est 
   *   utilisee : x + y * taille_x
   */
  Couleur * image;
  
  /**
   *   alphaMax (double) la valeur courrante du maximum alpha des couleurs
   *   presente dans la matrice est conserve pour accelerer le calcule
   *   de correction alpha.
   */
  double alphaMax;
};

Image *creerImage( int a_taille_x, int a_taille_y, int a_surEchantillonage ) {
  assert( a_taille_x > 0 );
  assert( a_taille_y > 0 );
  assert( a_surEchantillonage > 0 );
  Image * resultat = NULL;

  a_taille_x *= a_surEchantillonage;
  a_taille_y *= a_surEchantillonage;

  resultat = (Image *)malloc( sizeof( Image ) );
  if( NULL == resultat ) {
    fprintf( stderr, "Images : creerImage : erreur d'allocation\n" );
    exit(-1);
  }

  resultat->image = (Couleur *)malloc( sizeof( Couleur ) * 
				       a_taille_x * a_taille_y
				       );
  if( NULL == resultat->image ) {
    fprintf( stderr, "Images : creerImage : erreur d'allocation\n" );
    exit(-1);
  }

  resultat->taille_x = a_taille_x;
  resultat->taille_y = a_taille_y;
  resultat->alphaMax = 0.0;
  resultat->surEchantillonage = a_surEchantillonage;

  int i;
  int nombreCase = a_taille_x * a_taille_y;
  for( i = 0; i < nombreCase; i ++ ) {
    resultat->image[i].rouge = 0;
    resultat->image[i].vert  = 0;
    resultat->image[i].bleu  = 0;
    resultat->image[i].alpha = 0;
  }

  return resultat;
}

int tailleX( Image * a_image ) {
  assert( a_image != NULL );
  return a_image->taille_x / a_image->surEchantillonage;
}

int tailleY( Image * a_image ) {
  assert( a_image != NULL );
  return a_image->taille_y / a_image->surEchantillonage;
}

void sauvegarderImage( Image * a_image, char * a_nomFichier ) {
  assert( a_image != NULL );
  assert( a_nomFichier != NULL );
  FILE * fichier = fopen( a_nomFichier, "w" );

  int t_x = tailleX( a_image );
  int t_y = tailleY( a_image );

  fprintf( fichier, "P3\n%i %i\n255\n", t_x, t_y );

  int x = 0;
  int y = 0;
  int dx = 0;
  int dy = 0;

  for( y = 0; y < t_y; y++ ) {
    for( x = 0; x < t_x; x++ ) {
      double rouge = 0.0;
      double vert = 0.0;
      double bleu = 0.0;

      for( dx = 0; dx < a_image->surEchantillonage; dx++ ) {
	for( dy = 0; dy < a_image->surEchantillonage; dy++ ) {
	  int position = 
	    ( x * a_image->surEchantillonage + dx ) + 
	    ( y * a_image->surEchantillonage + dy ) * a_image->taille_x;

	  rouge += a_image->image[position].rouge;
	  vert  += a_image->image[position].vert ;
	  bleu  += a_image->image[position].bleu ;
	}
      }

      int surCarre = a_image->surEchantillonage * a_image->surEchantillonage;
      rouge = rouge / surCarre;
      vert  = vert  / surCarre;
      bleu  = bleu  / surCarre;

      fprintf( fichier, "%i %i %i\n", 
	       (int)( rouge * 255 ), 
	       (int)( vert  * 255 ), 
	       (int)( bleu  * 255 ) 
	       );
    }
  }

  fclose( fichier );
}
 
void convertionAlpha( Image * a_image ) {
  assert( a_image != NULL );
  int i = 0;
  int nombreCase = a_image->taille_x * a_image->taille_y;
  double alphaMax = a_image->alphaMax;

  for( i = 0; i < nombreCase; i ++ ) {
    a_image->image[i] = correctionAlpha( a_image->image[i], alphaMax );
  }
}

void additionnerCouleur( Image * a_image, int a_x, int a_y, Couleur a_couleur ) {
  assert( a_image != NULL );
  assert( 0 <= a_x && a_x < a_image->taille_x );
  assert( 0 <= a_y && a_y < a_image->taille_y );

  int position = a_x + a_y * a_image->taille_x;

  a_image->image[position] = additionner( a_image->image[position], a_couleur );
  if( a_image->image[position].alpha > a_image->alphaMax ) {
    a_image->alphaMax = a_image->image[position].alpha;
  }
}

void additionnerCouleurReel( Image * a_image, float a_x, float a_y, Couleur a_couleur ) {
  int x = ( a_x + 1.0 ) * a_image->taille_x / 2.0;
  int y = ( 1.0 - a_y ) * a_image->taille_y / 2.0;
  
  if( ( 0 <= x && x < a_image->taille_x )
      && 
      ( 0 <= y && y < a_image->taille_y ) ) {
    additionnerCouleur( a_image, x, y, a_couleur );
  }
}
