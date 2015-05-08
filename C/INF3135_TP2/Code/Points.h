
#ifndef POINTS_H
#define POINTS_H

/** @name Points */
//@{

//@Include: Points.c

/**
 * @name Module Points.
 * @memo Classe d'objets.
 * @doc
 * Ce module decrit la structure Point qui permet de contenir les
 * coordonnee 'x' et 'y' d'un point sous forme de 'double'.
 * Les champs de cette structure sont accessible de l'exterieur,
 * il n'y a pas de routine d'acces.
 * @author Bruno Malenfant
 */
;

 
/**
 * (Points_h) Structure contenant les coordonnees cartesiennes
 * d'un point.
 */
struct _point {
  /**
   *   x (double) coordonne en x.
   */
  double x;

  /**
   *   y (double) coordonne en y.
   */
  double y;
};

/**
 * (Points_h) Pointeur sur une structure _point.
 */
typedef struct _point * Point;


/**
 * (Points_h) Construit un point avec les coordonnees fournis.
 * @param
 *   double a_x : coordonnees x
 * @param
 *   double a_y : coordonnees y
 * @return
 *   Une structure Point contenant les coordonnees
 *   en entrees.  Si l'allocation ne fonctionne pas
 *   alors NULL est retourne.
 * @exception
 *   Si l'allocation ne fonctionne pas alors 
 *   0 est place dans 'allocationReussit.
 *   Sinon 1 est place.
 */
Point creerPoint( double a_x, double a_y, 
		  int *a_allocationReussit );

/**
 * (Points_h) Constructeur de copie.
 * @param
 *   a_point (Point) La structure a copier.
 * @precondition
 *   a_point != NULL.
 * @return
 *   Une copie du point recu.
 *   NULL si l'allocation ne reussit pas.
 * @exception
 *   allocationReussit :
 *   Si l'allocation ne fonctionne pas alors 
 *   0 est place dans 'allocationReussit'.
 *   Sinon 1 est place.
 */
Point copierPoint( Point a_point,
		   int *a_allocationReussit );

/**
 * (Points_h) procedure affichant un Point.
 *   le point (x, y) est affiche avec les parantheses 
 *   et la virgule pour separer les coordonnees.
 * @param
 *   a_point (Point) un point a afficher.
 * @precondition
 *   a_point != NULL
 */
void afficherPoint( Point a_point );

/**
 * (Points_h) Calcule la norme du vecteur genere par le point.
 * @return
 *   $\sqrt{x^2 + y^2}$
 * @param
 *   point (Point) le point duquel le vecteur sera genere.
 * @precondition
 *   point != NULL
 */
double distanceOrigine( Point a_point );

/**
 * (Points_h) Calcule l'orientation du vecteur genere par le point.
 * @return
 *   $\arctan{\frac{y}{x}}$
 *   si $y = 0$ alors retourne 0.
 *   si $x = 0$ alors utilise un $x$ tres petit.
 * @param
 *   point (Point) le point duquel le vecteur sera genere.
 * @precondition
 *   point != NULL
 */
double angle( Point point );

//@}

#endif
