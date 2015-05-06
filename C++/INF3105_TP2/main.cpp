/* main.cpp
    *
    * Petit programme qui traite un fichier.xml représentant une matrice
    *
    * Auteur : Dany Deroy
    * Code permanent : DERD02088403
    * Date : 2015
    */

#include "balise.hpp"
#include "fichierBalises.hpp"
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <stdexcept>
#include <iomanip>

void validerNbArguments (int);
void validerFichierEntre (string);
map<string,set<string> > creationMap(const vector <Balise>&);
void ajouterDirections(const vector <Balise>&, map<string,set<string> >&);
void afficherMatrice(const map<string,set<string> >&);
string tronquer(string, unsigned int);

/* largeur des colomnes pour affichage */
const int setwMax = 8;
/* extension acceptee */
const string EXTENSION = ".xml";
/* messages erreurs */
const string MSG_ERREUR_NBARGUMENT_INVALIDE = "ERREUR : Mauvais arguments entres a la console";
const string MSG_ERREUR_EXTENSION_ENTREE_INVALIDE = "ERREUR : Fichier entre n'est pas de format ";

int main (int argc, char *argv[]) {
    char * ficIn = argv[1];
    string ficInString = ficIn;

    vector <Balise> balise;
    map<string,set<string> > direction;

    try {
        validerNbArguments(argc);
        validerFichierEntre(ficInString);

        FichierBalises * graph = new FichierBalises(ficIn);
        while (true) {
            balise.push_back(Balise(graph->litProchaineBalise()));
        }
    }
    catch (range_error e) {
        // lecture des balises terminï¿½es
    }
    catch (runtime_error e) {
        cerr << argv[0] << ' ' << e.what() << endl;
        return 1;
    }
    catch (invalid_argument e) {
        cerr << argv[0] << ' ' << e.what() << endl;
        return 1;
    }

    try {
        direction = creationMap(balise);
        ajouterDirections(balise, direction);
    }
    catch (runtime_error e) {
        cerr << argv[0] << ' ' << e.what() << endl;
        return 1;
    }

    afficherMatrice(direction);

    return 0;
}

void validerNbArguments (int argc) {
    if (argc != 2) {
        throw invalid_argument (MSG_ERREUR_NBARGUMENT_INVALIDE);
    }
}

void validerFichierEntre(string ficIn) {
    string extension = EXTENSION;
    if (extension.compare(ficIn.substr(ficIn.length()-EXTENSION.length(), ficIn.length())) != 0) {
        throw invalid_argument (MSG_ERREUR_EXTENSION_ENTREE_INVALIDE + EXTENSION);
    }
}

/* création d'un map qui possèdera comme clé les nodes */
map<string,set<string> > creationMap(const vector <Balise>& balise) {
    vector<Balise>::const_iterator baliseIterateur;
    map<string,set<string> > direction;
    string nom;
    set<string> target;

    for (baliseIterateur = balise.begin(); baliseIterateur != balise.end(); baliseIterateur++) {
        if (baliseIterateur->litNom() == "node") {
            nom = baliseIterateur->litValeurAttribut("id");

            direction.insert(pair<string,set<string> >(nom, target));
        }
    }
    return direction;
}

/* ajouter dans le map les directions où les nodes se dirigent */
void ajouterDirections(const vector <Balise>& balise, map<string,set<string> >& direction) {
    vector<Balise>::const_iterator baliseIterateur;
    map<string,set<string> >::iterator directionIterateur;

    for (baliseIterateur = balise.begin(); baliseIterateur != balise.end(); baliseIterateur++) {

        if (baliseIterateur->litNom() == "edge") {
            directionIterateur = direction.find(baliseIterateur->litValeurAttribut("source"));
            directionIterateur->second.insert(baliseIterateur->litValeurAttribut("target"));

            if (!baliseIterateur->estAttribut("directed") || baliseIterateur->litValeurAttribut("directed") == "false") {
                directionIterateur = direction.find(baliseIterateur->litValeurAttribut("target"));
                directionIterateur->second.insert(baliseIterateur->litValeurAttribut("source"));
            }
        }
    }
}

void afficherMatrice(const map<string,set<string> >& matrice) {
    map<string,set<string> >::const_iterator itClef, itDirection;

    cout << setw(setwMax) << " " << setfill(' ') << ' ';
    for (itClef = matrice.begin(); itClef != matrice.end(); itClef++) {
        cout << setw(setwMax) << tronquer(itClef->first, setwMax) << setfill(' ') << ' ';
    }
    cout << endl;
    for (itClef = matrice.begin(); itClef != matrice.end(); itClef++) {
        cout << setw(setwMax) << tronquer(itClef->first, setwMax) << setfill(' ') << ' ';

        for (itDirection = matrice.begin(); itDirection != matrice.end(); itDirection++) {
            if (itClef->second.find(itDirection->first) != itClef->second.end()) {
                cout << setw(setwMax) << '1' << setfill(' ') << ' ';
            }
            else {
                cout << setw(setwMax) << '0' << setfill(' ') << ' ';
            }
        }
        cout << endl;
    }
}

/* fonction pour tronquer les noms des nodes qui ont plus que carMax caractères */
string tronquer(string chaine, unsigned int carMax) {
    if (chaine.length() > carMax) {
        return chaine.substr(0,carMax);
    }
    return chaine;
}
