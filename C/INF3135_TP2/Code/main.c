
/**
 * Dany Deroy
 * DERD02088403
 * danyderoy@gmail.com
 */

#include "Points.h"
#include "FonctionNonLineaires.h"
#include "FonctionLineaires.h"
#include "Sequences.h"
#include "Images.h"
#include "Palettes.h"
#include "Pairs.h"

//convertionAlpha( image );

//@Include: Couleurs.h
//@Include: FonctionNonLineaires.h
//@Include: FonctionLineaires.h
//@Include: Images.h
//@Include: Math2.h
//@Include: Palettes.h
//@Include: Points.h
//@Include: Fractals.h
//@Include: Pairs.h

#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>

/** @name Principale */
//@{

/**
 * @name Fichier Principal.
 * @memo .
 * @doc
 * Ce fichier contient les routines necessaires a la construction d'une
 * fractal de type "flame", utilisant des transformations lineaire et 
 * non-lineaire.  La fractal est genere en construisant l'ensemble 
 * solution que represent les differentes transformes.
 */
;

/**
 * (main_c) structure contenant les arguments d'entrees du logiciel.
 */
struct _arguments {
    /**
     *   tailleX (int) represente la largeur de l'image a construire.
     *   Ce champs contient la valeurs 200 par defaut sinon il contient
     *   l'argumens -x.
     * @invariant
     *   100 <= tailleX <= 10 000
     */
    int tailleX;

    /**
     *   tailleY (int) represente la hauteur de l'image a construire.
     *   Ce champs contient la valeurs 200 par defaut sinon il contient
     *   l'arguments -y.
     * @invariant
     *   100 <= tailleY <= 10 000
     */
    int tailleY;

    /**
     *   nbrIteration (int) contient le nombre d'iteration pour evaluer la
     *   fonction.  Par defaut la valeur sera 10 000, sinon la valeur de
     *   -n sera utilise.
     * @invariant
     *   100 <= nbrIteration <= 10 000 000
     */
    int nbrIteration;

    /**
     *   nomFichierPpm (char *) contient le nom du fichier ppm pour l'image 
     *   resultante, selon l'argument -o.
     */
    char * nomFichierPpm;

    /**
     *   nomFichierIfs (char *) contient le nom du fichier ifs qui doit
     *   contenir la description de la transforme lineaire. 
     */
    char * nomFichierIfs;

    /**
     *   nomFichierPalette (char *) contient le nom du fichier contenant
     *   la palette de couleur a utiliser, selon l'argument -p.
     */
    char * nomFichierPalette;

    /** 
     *   nbrImagesGen (int) contient le nombre d'images de passaqe a creer entre
     *   une fractale de depart et une fractale de fin.
     *  @invariant
     *   2 <= nbrImagesGen <= 250
     */
    int nbrImagesGen;

    /**
     *   nomFichierFinalIfs (int) contient le nom du fichier ifs du fin qui doit
     *   contenir la description de la transforme lineaire.
     */
    char * nomFichierFinalIfs;

    /**
     *   numRouge, numVert, numBleu (int) contiennent les valeurs des composantes
     *   de couleur pour creer une palette de couleur.
     *  @invariant
     *   0 <= numRouge, numVert, numBleu <= 255
     */
    int numRouge, numVert, numBleu;

};

/**
 * (main.c) Definition du type Arguments.
 */
typedef struct _arguments Arguments;

/**
 * (main_c) fonction lisant le fichier contenant la description des
 * fonctions lineaire.
 * @return 
 *   Une sequence contenant les differentes fonction lineaire lues.
 * @param 
 *   a_nomFichier (char *) le nom du fichier contenant les transformations
 *   lineaires.
 * @precondition
 *   a_nomFichier != NULL
 */
Sequence * lireFichierIfs(char * a_nomFichier) {
    assert(NULL != a_nomFichier);

    Sequence * ifs = creer_Seq();
    assert(ifs != NULL);

    FILE * fichierEquation = fopen(a_nomFichier, "r");
    if (NULL == fichierEquation) {
        fprintf(stderr, "main : lireFichierIfs : erreur lors de l'ouverture du fichier.\n");
        exit(-1);
    }

    do {
        double a, b, c, d, e, f;
        char nomFctNL [50];
        int couleur;
        int n = fscanf(fichierEquation, "%lf %lf %lf %lf %lf %lf %d %s", &a, &b, &c, &d, &e, &f,
                &couleur, nomFctNL);

        if (8 == n) {
            FonctionLineaire * fonctionL = creerFonctionLineaire(a, b, c, d, e, f, couleur);

            FonctionNonLineaire * fonctionNL = chaineAFonction(nomFctNL);

            int allocationReussi = 0;
            Pair fonctionComplete = creerPair(fonctionL, fonctionNL,
                    &allocationReussi);
            if (!allocationReussi) {
                fprintf(stderr, "main : lireFichierIfs : erreur d'allocation.\n");
                exit(-1);
            }

            ajouterEnQueue_Seq(ifs, (Element) fonctionComplete);
        } else if (n != -1) {
            fprintf(stderr, "main : lireFichierIfs : erreur de lecture dans le fichier d'entrees.\n");
            exit(-1);
        }
    } while (!feof(fichierEquation));

    return ifs;
}

/**
 * (main.c) fonction mathematique pour calculer la valeur transitoire entre deux fichier ifs
 * @return 
 *   un double representant la valeure intermediaire
 * @param 
 *   valeurInitiale (double) la valeur du fichier ifs de debut
 * @param 
 *   valeurFinale (double) la valeur du fichier ifs de fin
 * @param 
 *   nbrImage (int) le nombre d'images total qui sera cree
 * @param 
 *   numImage (int) le numero de l'image a creer dans la suite
 */
double calculValeurIntermediaire(double valeurInitiale, double valeurFinale, int nbrImage, int numImage) {
    return numImage * ((valeurFinale - valeurInitiale) / (nbrImage - 1.0)) + valeurInitiale;
}

/**
 * (main.c) fonction qui renvoie le fichier ifs de transition
 * @return
 *   une sequence des fonctions de transition
 * @param
 *   debut_nomFichier (char *) le fichier ifs de depart
 * @precondition
 *   debut_nomFichier != NULL
 * @param
 *   fin_nomFichier (char *) le fichier ifs de fin
 * @precondition
 *   fin_nomFichier != NULL
 * @param
 *   n_nbrImage (int) le nombre d'images total qui sera cree
 * @param
 *   numImage (int) le numero de l'image a creer dans la suite
 *  
 */
Sequence * calculerIfsIntermediaire(char * debut_nomFichier, char * fin_nomFichier, int n_nbrImage, int numImage) {
    assert(NULL != a_nomFichier);
    
    Sequence * ifs = creer_Seq();
    assert(ifs != NULL);

    FILE * fichierDebut = fopen(debut_nomFichier, "r");
    FILE * fichierFin = fopen(fin_nomFichier, "r");
    if (NULL == fichierDebut || NULL == fichierFin) {
        fprintf(stderr, "main : lireFichierIfs : erreur lors de l'ouverture du fichier.\n");
        exit(-1);
    }

    do {
        double a1, b1, c1, d1, e1, f1;
        double a2, b2, c2, d2, e2, f2;
        char nomFctNL1 [50];
        int couleur1;
        char nomFctNL2 [50];
        int couleur2;

        int n1 = fscanf(fichierDebut, "%lf %lf %lf %lf %lf %lf %d %s", &a1, &b1, &c1, &d1, &e1, &f1,
                &couleur1, nomFctNL1);
        int n2 = fscanf(fichierFin, "%lf %lf %lf %lf %lf %lf %d %s", &a2, &b2, &c2, &d2, &e2, &f2,
                &couleur2, nomFctNL2);

        double a = calculValeurIntermediaire(a1, a2, n_nbrImage, numImage);
        double b = calculValeurIntermediaire(b1, b2, n_nbrImage, numImage);
        double c = calculValeurIntermediaire(c1, c2, n_nbrImage, numImage);
        double d = calculValeurIntermediaire(d1, d2, n_nbrImage, numImage);
        double e = calculValeurIntermediaire(e1, e2, n_nbrImage, numImage);
        double f = calculValeurIntermediaire(f1, f2, n_nbrImage, numImage);
        double couleur = calculValeurIntermediaire(couleur1, couleur2, n_nbrImage, numImage);
        
        if(strcmp(nomFctNL1, nomFctNL2) != 0) {
            fprintf(stderr, "main : calculerIfsIntermediaire : erreur de lecture dans le fichier de debut ou de fin, les fichiers ifs n'ont pas les memes fonctions.\n");
        }
        
        if (8 == n1 && 8 == n2) {
            FonctionLineaire * fonctionL = creerFonctionLineaire(a, b, c, d, e, f, 200);

            FonctionNonLineaire * fonctionNL = chaineAFonction(nomFctNL1);

            int allocationReussi = 0;
            Pair fonctionComplete = creerPair(fonctionL, fonctionNL,
                    &allocationReussi);
            if (!allocationReussi) {
                fprintf(stderr, "main : lireFichierIfs : erreur d'allocation.\n");
                exit(-1);
            }

            ajouterEnQueue_Seq(ifs, (Element) fonctionComplete);
        } else if (n1 != -1 || n2 != -1) {
            fprintf(stderr, "main : calculerIfsIntermediaire : erreur de lecture dans le fichier de debut ou de fin.\n");
            exit(-1);
        }
    } while (!feof(fichierDebut));

    return ifs;
}

/**
 * (main_c) fonction qui verifie si les 4 derniers caracteres d'une
 * chaine sont valide.
 * @return
 *  vrai si les 4 dernier caracteres de la chaine a_nomFichier sont
 *  equivalent aux caractere de a_extention.
 *  retourne faux sinon ou si la chaine a_extention contient moins
 *  de 4 caracteres.
 * @param
 *   a_extention (char *) une chaine de caracteres representant l'extention.
 * @precondition 
 *   taille(a_extention) == 4
 *   a_extention != NULL
 * @param 
 *   a_nomFichier (char *) une chaine de caractere representant un nom
 *   de fichier.
 * @precondition
 *   a_nomFichier != NULL
 */
int extentionEstValide(char * a_extention, char * a_nomFichier) {
    assert(a_extention != NULL);
    assert(strlen(a_extention) == 4);
    assert(a_nomFichier != NULL);

    int tailleChaine = strlen(a_nomFichier);

    return ( tailleChaine >= 4
            &&
            0 == strcmp(&(a_nomFichier[ tailleChaine - 4 ]), a_extention));
}

/**
 * (main_c) fonction qui sert a valider et transformer les arguements
 * recu sur la ligne de commande.
 * @return
 *  Une structure d'arguments contenant les differentes valeurs lues
 *  ou celle par defaut.  Voir la description de cette structure
 *  pour plus d'information.
 * @param
 *   a_argn (int) le nombre d'argument que contient le tableau 
 *   d'arguements.
 * @param
 *   a_argv (char *[]) un tableau de chaine de caractere representant
 *   chaque argument.
 * @precondition
 *   a_argv != NULL
 */
Arguments validerEtLireArguments(int a_argn, char * a_argv[]) {
    assert(a_argv != NULL);

    if (a_argn < 2) {
        fprintf(stderr, "main : lireArguments : pas assez d'arguments sur la ligne de commande.\n");
        exit(-1);
    }

    int compteur_a = 0;
    int compteur_f = 0;
    int position = 1;
    Arguments resultat = {200, 200, 10000, NULL, NULL, NULL, 0, NULL, -1, -1, -1};

    while (position < a_argn) {
        if ('-' == a_argv[ position ][ 0 ]) {
            position++;
            if (a_argn == position) {
                fprintf(stderr, "main : lireArguments : argument manquant.\n");
                exit(-1);
            }
            switch (a_argv[ position - 1 ][ 1 ]) {
                case 'x':
                    resultat.tailleX = atoi(a_argv[position]);
                    if (resultat.tailleX < 100 || resultat.tailleX > 10000) {
                        fprintf(stderr, "main: lireArguments : l'argument -x doit etre entre 100 et 10000.\n");
                        exit(-1);
                    }
                    break;
                case 'y':
                    resultat.tailleY = atoi(a_argv[position]);
                    if (resultat.tailleY < 100 || resultat.tailleY > 10000) {
                        fprintf(stderr, "main: lireArguments : l'argument -y doit etre entre 100 et 10000.\n");
                        exit(-1);
                    }
                    break;
                case 'n':
                    resultat.nbrIteration = atoi(a_argv[position]);
                    if (resultat.nbrIteration < 100 || resultat.nbrIteration > 10000000) {
                        fprintf(stderr, "main: lireArguments : l'argument -n doit etre entre 100 et 10000000.\n");
                        exit(-1);
                    }
                    break;
                case 'o':
                    if (!extentionEstValide(".ppm", a_argv[ position ])) {
                        fprintf(stderr, "main : lireArguments : le nom du fichier de sorties doit se terminer par .ppm.\n");
                        exit(-1);
                    }
                    resultat.nomFichierPpm = a_argv[ position ];
                    break;
                case 'p':
                    if (!extentionEstValide(".pal", a_argv[ position ])) {
                        fprintf(stderr, "main : lireArguments : le nom du fichier de couleur doit se terminer par .pal.\n");
                        exit(-1);
                    }
                    resultat.nomFichierPalette = a_argv[ position ];
                    break;
                case 'a':
                    resultat.nbrImagesGen = atoi(a_argv[position]);
                    if (resultat.nbrImagesGen < 2 || resultat.nbrImagesGen > 250) {
                        fprintf(stderr, "main: lireArguments : l'argument -a doit etre entre 2 et 250.\n");
                        exit(-1);
                    }
                    compteur_a = 1;
                    break;
                case 'c':
                    resultat.numRouge = atoi(a_argv[position]);
                    if (resultat.numRouge < 0 || resultat.numRouge > 255) {
                        fprintf(stderr, "main: lireArguments : Chaque composantes de l'argument -c doit etre entre 0 et 255.\n");
                        exit(-1);
                    }

                    resultat.numVert = atoi(a_argv[++position]);
                    if (resultat.numVert < 0 || resultat.numVert > 255) {
                        fprintf(stderr, "main: lireArguments : Chaque composantes de l'argument -c doit etre entre 0 et 255.\n");
                        exit(-1);
                    }
                    resultat.numBleu = atoi(a_argv[++position]);
                    if (resultat.numBleu < 0 || resultat.numBleu > 255) {
                        fprintf(stderr, "main: lireArguments : Chaque composantes de l'argument -c doit etre entre 0 et 255.\n");
                        exit(-1);
                    }
                    break;
                case 'f':
                    if (!extentionEstValide(".ifs", a_argv[ position ])) {
                        fprintf(stderr, "main : lireArguments : le nom du fichier ifs doit se terminer par .ifs.\n");
                        exit(-1);
                    }
                    resultat.nomFichierFinalIfs = a_argv[ position ];
                    compteur_f = 1;
                    break;
                default:
                    fprintf(stderr, "main : lireArgument : argument non valide.\n");
                    break;
            }
        } else {
            if (!extentionEstValide(".ifs", a_argv[ position ])) {
                fprintf(stderr, "main : lireArguments : le nom du fichier ifs doit se terminer par .ifs.\n");
                exit(-1);
            }
            resultat.nomFichierIfs = a_argv[ position ];
        }
        position++;
    }
    if (NULL == resultat.nomFichierIfs) {
        fprintf(stderr, "main : lireArguments : le nom du fichier ifs n'est pas specifie.\n");
        exit(-1);
    } else if ((compteur_a + compteur_f) % 2 != 0) {
        fprintf(stderr, "main: lireArguments : l'argument -a et l'argument -f ne peuvent etre utilises un sans l'autre.\n");
        exit(-1);
    }

    return resultat;
}

/**
 * (main_c) Le programme principal.
 */
int main(int argn, char * argv[]) {
    // multiplier par 8 la taille de la memoire RAM accessible au
    // processus :
    struct rlimit rlp;
    getrlimit(RLIMIT_DATA, & rlp);
    rlp.rlim_cur *= 8;
    setrlimit(RLIMIT_DATA, & rlp);

    Arguments args = validerEtLireArguments(argn, argv);

    Sequence * ifs;

    Image * image = creerImage(args.tailleX, args.tailleY, 3);

    Palette * paletteCouleur = NULL;
    if (NULL != args.nomFichierPalette) {
        paletteCouleur = lirePalette(args.nomFichierPalette);
    } else if (-1 != args.numRouge || -1 != args.numVert || -1 != args.numBleu) {
        paletteCouleur = construirePalette(args.numRouge, args.numVert, args.numBleu);
    } else {
        paletteCouleur = construirePalette(1, 1, 1);
    }

    if (NULL == args.nomFichierFinalIfs) {
        ifs = lireFichierIfs(args.nomFichierIfs);
        genererFlame(ifs, args.nbrIteration, image, paletteCouleur);

        convertionAlpha(image);

        if (args.nomFichierPpm != NULL) {
            sauvegarderImage(image, args.nomFichierPpm);
        } else {
            sauvegarderImage(image, "a.ppm");
        }
    } else {
        int gradiant = 0;
        do {
            ifs = calculerIfsIntermediaire(args.nomFichierIfs, args.nomFichierFinalIfs, args.nbrImagesGen, gradiant);
            genererFlame(ifs, args.nbrIteration, image, paletteCouleur);

            convertionAlpha(image);

            char nomSauvegarde[10];
            sprintf(nomSauvegarde, "%s%04d%s", "a", gradiant, ".ppm");

            sauvegarderImage(image, nomSauvegarde);
            gradiant++;
        } while (gradiant < args.nbrImagesGen);
    }
    return 0;
}

//@}
