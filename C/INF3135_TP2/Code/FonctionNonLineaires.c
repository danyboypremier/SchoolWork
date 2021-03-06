
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include "FonctionNonLineaires.h"
#include "Points.h"

FonctionNonLineaire * chaineAFonction( char * a_nomFonction ) {
  assert( NULL != a_nomFonction );
  FonctionNonLineaire * resultat = NULL;

  if( 0 == strcmp( a_nomFonction, "lineaire" ) ) {
    resultat = &fnl_lineaire;
  }
  if( 0 == strcmp( a_nomFonction, "spherique" ) ) {
    resultat = &fnl_spherique;
  }
  if( 0 == strcmp( a_nomFonction, "sinusoidale" ) ) {
    resultat = &fnl_sinusoidale;
  }
  if( 0 == strcmp( a_nomFonction, "galaxy" ) ) {
    resultat = &fnl_galaxy;
  }
  if( 0 == strcmp( a_nomFonction, "feracheval" ) ) {
    resultat = &fnl_feracheval;
  }
  if( 0 == strcmp( a_nomFonction, "spirale" ) ) {
    resultat = &fnl_spirale;
  }
  if( 0 == strcmp( a_nomFonction, "polaire" ) ) {
    resultat = &fnl_polaire;
  }
  if( 0 == strcmp( a_nomFonction, "trapeze" ) ) {
    resultat = &fnl_trapeze;
  }
  if( 0 == strcmp( a_nomFonction, "coeur" ) ) {
    resultat = &fnl_coeur;
  }
  if( 0 == strcmp( a_nomFonction, "disque" ) ) {
    resultat = &fnl_disque;
  }
  if( 0 == strcmp( a_nomFonction, "diamand" ) ) {
    resultat = &fnl_diamand;
  }
  if( 0 == strcmp( a_nomFonction, "ex" ) ) {
    resultat = &fnl_ex;
  }
  if( 0 == strcmp( a_nomFonction, "julia" ) ) {
    resultat = &fnl_julia;
  }

  if( NULL == resultat ) {
    fprintf( stderr, "FonctionNonLineaire : chaineAFonction : fonction non-lineaire non valide.\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_lineaire( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;

  resultat = copierPoint( a_point, & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_lineaire : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}


Point fnl_sinusoidale( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;

  resultat = creerPoint( sin( a_point->x ), sin( a_point->y ), 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_sinusoidale : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_spherique( Point a_point ){
  Point resultat = NULL;
  int constructionReussit = 0;
  double r2 = a_point->x * a_point->x + a_point->y * a_point->y;
  r2 = ( r2 == 0.0 ) ? 0.0000001 : r2;

  resultat = creerPoint( a_point->x / r2, a_point->y / r2, 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_spherique : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_galaxy( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( r * cos( theta + r ), r * sin( theta + r ), 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_galaxy : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_feracheval( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( r * cos( 2 * theta ), r * sin( 2 * theta ), 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_feracheval : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_polaire( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( theta / M_PI, r - 1.0, 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_polaire : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_trapeze( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( r * sin( r + theta ), r * cos( theta - r ), 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_trapeze : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_coeur( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( r * sin( r * theta ), - 1.0 * r * cos( theta * r ), 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_coeur : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_disque( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( theta * sin( M_PI * r ) / M_PI, theta * cos( M_PI * r ) / M_PI, 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_disque : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_spirale( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( ( cos( theta ) + sin( r ) ) / r, 
			 ( sin( theta ) - cos( r ) ) / r, 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_spiral : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_hyperbolique( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( sin( theta ) / (r == 0.0 ? 0.000001 : r), 
			 cos( theta ) * r, 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_hyperbolique : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_diamand( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );

  resultat = creerPoint( sin( theta ) * cos( r ), 
			 cos( theta ) * sin( r ), 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_diamand : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_ex( Point a_point ) { 
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );
  double sin_tr = sin( theta + r );
  double cos_tr = cos( theta - r );

  resultat = creerPoint( r * sin_tr * sin_tr * sin_tr, 
			 r * cos_tr * cos_tr * cos_tr, 
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_ex : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}

Point fnl_julia( Point a_point ) {
  Point resultat = NULL;
  int constructionReussit = 0;
  double r = distanceOrigine( a_point );
  double theta = angle( a_point );
  double sqrt_r = sqrt( r );
  double omega = rand() < 0.5 ? 0.0 : M_PI;

  resultat = creerPoint( sqrt_r * cos( theta / 2.0 + omega ), 
			 sqrt_r * sin( theta / 2.0 + omega ),
			 & constructionReussit );
  if( ! constructionReussit ) {
    fprintf( stderr, "FonctionNonLineaire : fnl_julia : construction non reussit\n" );
    exit( -1 );
  }

  return resultat;
}
