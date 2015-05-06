 /* derd02088403_frequencier.cpp
 *
 * Evaluateur de frequence de mots dans un fichier text
 * tries par frequence et ordre alphanumerique
 * Auteur : Dany Deroy
 *
 * Code permanent : DERD02088403
 * Date : 2015-02-04
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdexcept>
#include <iomanip>

using namespace std;

 /*
  * structure qui sera utilise dans le vecteur
  * le mot rencontre et la frequence du mot rencontre
  */
struct motFrequence {
    string mot;
    unsigned int frequence;
};

void validerNbArguments (int);
void validerFichierEntre (string);
void convTextAString (ifstream&, string&);
void enleverPonctuation (string&);
void ajouterMot (vector<motFrequence>&, motFrequence&);
int motExiste (vector<motFrequence>&, motFrequence&);
void trierFrequence (vector<motFrequence>&);
void trierAlpha (vector<motFrequence>&);
void afficherResultat (vector<motFrequence>&);

int main (int argc, char *argv[]) {
    string ficIn = argv[1];
    vector<motFrequence> listeMot;
    string buffer = "";
    motFrequence element;

    try {
        validerNbArguments(argc);
        validerFichierEntre(ficIn);

        ifstream texte(ficIn.c_str());
        if (! texte) {
            throw runtime_error ("ERREUR : Impossible d'ouvrir le fichier texte");
        }

        convTextAString(texte, buffer);

        istringstream bufferStream(buffer);
        while (bufferStream >> element.mot){
            ajouterMot(listeMot, element);
        }

        trierFrequence(listeMot);
        afficherResultat(listeMot);
    }
    catch (runtime_error e) {
        cerr << argv[0] << ' ' << e.what() << endl;
        return 1;
    }
    catch (invalid_argument e) {
        cerr << argv[0] << ' ' << e.what() << endl;
        return 1;
    }

    return 0;
}

void validerNbArguments (int argc) {
    if (argc != 2) {
        throw invalid_argument ("ERREUR : Mauvais arguments entres a la console");
    }
}

 /*
  * verifie que le fichier entre est valide (extension .txt)
  */
void validerFichierEntre(string ficIn) {
    string extension = ".txt";
    if (extension.compare(ficIn.substr(ficIn.length()-4, ficIn.length())) != 0) {
        throw invalid_argument ("ERREUR : Fichier entre n'est pas de format txt");
    }
}

 /*
  * converti le texte entre en string
  * fait l'appelle de enleverPonctuation
  */
void convTextAString (ifstream &flux, string &buffer) {
    string temp;
    while (flux >> temp) {
        enleverPonctuation(temp);
        buffer += temp + " ";
    }
}

 /*
  * change les caracteres ponctues d'une chaine de caracteres en espace
  */
void enleverPonctuation (string &mot) {
    for (unsigned int i = 0; i < mot.size(); i++) {
        if (ispunct(mot[i])) {
            mot[i] = ' ';
        }
    }
}

 /*
  * ajoute le mot dans le vecteur et ajout l'occurance de ce mot
  */
void ajouterMot (vector<motFrequence> &liste, motFrequence &element) {
    int index;

    if (liste.empty()) {
        element.frequence = 1;
        liste.push_back(element);
    } else {
        index = motExiste(liste, element);
        if (index == -1) {
            element.frequence = 1;
            liste.push_back(element);
        } else {
            liste[index].frequence++;
        }
    }
}

 /*
  * retourne la position du mot dans le vecteur
  * retourne -1 s'il n'est pas trouve
  */
int motExiste (vector<motFrequence> &liste, motFrequence &element) {
    vector<motFrequence>::const_iterator iterateur = liste.begin();

    while (iterateur != liste.end()) {
        if (element.mot == iterateur->mot) {
            return iterateur - liste.begin();
        }
        iterateur++;
    }

    return -1;
}

 /*
  * trie les mot par frequence decroissante ET par ordre alphanumerique (ASCII)
  */
void trierFrequence (vector<motFrequence> &liste) {
    motFrequence temp;

    for (unsigned int i = 0; i < liste.size(); i++) {
        unsigned int j = i;
        while ( (j > 0 && liste[j].frequence > liste[j-1].frequence) ||
              (j > 0 && liste[j].mot < liste[j-1].mot && liste[j].frequence == liste[j-1].frequence) )
        {
            temp = liste[j];
            liste[j] = liste[j-1];
            liste[j-1] = temp;
            j--;
        }
    }
}

 /*
  * affiche le vecteur frequence ajustee à droite ET mot ajuste a gauche
  */
void afficherResultat (vector<motFrequence> &liste) {
    vector<motFrequence>::iterator iterateur = liste.begin();

    while (iterateur != liste.end()) {
        cout << setw(10) << iterateur->frequence << setfill(' ')<< ' ';
        cout << iterateur->mot << endl;
        iterateur++;
    }
}
