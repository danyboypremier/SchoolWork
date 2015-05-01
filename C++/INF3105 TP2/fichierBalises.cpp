/* fichierBalises.cpp
 *
 *
 *
 * Auteur : Dany Deroy
 * Code permanent : DERD02088403
 * Date : 2015
 */

#ifndef FICHIERBALISE_CPP
#define FICHIERBALISE_CPP

#include "fichierBalises.hpp"
#include <string>
#include <stdexcept>

using namespace std;

/* messages d'erreurs */
const string MSG_ERREUR_LECTURE_FICHIER  = "ERREUR : Impossible d'ouvrir le fichier xml";
const string MSG_ERREUR_BALISE_INCOMPLETE = "ERREUR : Balise de fin de fichier incomplète";


FichierBalises::FichierBalises(char * nomFichier) {
    fichier.open(nomFichier);

    if (! fichier) {
        throw runtime_error (MSG_ERREUR_LECTURE_FICHIER);
    }
}

FichierBalises::~FichierBalises() {
    fichier.close();
}

/* lit les balises et passe par dessus les zone de texte et les balises de commentaires <!-- */
Balise FichierBalises::litProchaineBalise() {
    char car_temp;
    string chaineBalise = "";
    bool baliseComplete = false;

    unsigned int i = 0;
    while (fichier.get(car_temp)) {
        if (i == 0 && car_temp == '<') {
            chaineBalise += car_temp;
            i++;
        } else if ( (i == 1 && car_temp == '!') || (i == 0 && car_temp != '<') ) {
            chaineBalise = "";
            i = 0;
        } else if (car_temp == '>') {
            chaineBalise += car_temp;
            baliseComplete = true;
            break;
        } else {
            chaineBalise += car_temp;
            i++;
        }
    }
    if (chaineBalise == "") {
        // fin de lecture du fichier
        throw range_error ("");
    } else if (!baliseComplete) {
        throw runtime_error (MSG_ERREUR_BALISE_INCOMPLETE);
    }
    return Balise(chaineBalise);
}

#endif
