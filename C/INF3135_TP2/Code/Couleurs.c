
#include "Couleurs.h"

#include <assert.h>
#include "Math2.h"

Couleur additionner( Couleur a_couleur1, Couleur a_couleur2) {
  Couleur resultat;

  resultat.rouge = a_couleur1.rouge + a_couleur2.rouge;
  resultat.vert  = a_couleur1.vert  + a_couleur2.vert;
  resultat.bleu  = a_couleur1.bleu  + a_couleur2.bleu;
  resultat.alpha = a_couleur1.alpha + a_couleur2.alpha;

  return resultat;
}

Couleur correctionAlpha( Couleur a_couleur, double a_alphaMax ) {
  assert( a_couleur.alpha >= 0 );
  assert( a_alphaMax >= 1 );

  Couleur resultat;

  double k = 0.0;
  if( a_couleur.alpha != 0.0 ) {
    if( a_alphaMax == 1.0 ) {
      k = a_couleur.alpha;
    } else {
      k = log2( a_couleur.alpha ) / log2( a_alphaMax );
    }
    k = k / a_couleur.alpha;
  }

  resultat.rouge = ( a_couleur.rouge * k );
  resultat.vert  = ( a_couleur.vert  * k );
  resultat.bleu  = ( a_couleur.bleu  * k );
  resultat.alpha = 1;

  return resultat;
}

