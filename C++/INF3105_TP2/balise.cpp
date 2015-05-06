/* balise.cpp
 *
 *
 *
 * Auteur : Dany Deroy
 * Code permanent : DERD02088403
 * Date : 2015
 */

#ifndef BALISE_CPP
#define BALISE_CPP

#include "balise.hpp"
#include <stdexcept>

using namespace std;


string trouverNom(string);
map<string,string> trouverAttributs(string );
string retournerNomAttribut(unsigned int, string);
string retournerValeurAttribut(unsigned int, string);
TypeBalise trouverType(string);

/* messages d'erreurs */
const string MSG_ERREUR_ATTRIBUT_NEXISTE_PAS = "ERREUR : L'attribut demandé n'existe pas -> ";

Balise::Balise(string chaineBalise) {

    nom = trouverNom(chaineBalise);
    attributs = trouverAttributs(chaineBalise);
    type = trouverType(chaineBalise);
}

string Balise::litNom() const {
    return nom;
}

TypeBalise Balise::litType() const {
    return type;
}

bool Balise::estAttribut(string nomAttribut) const {
    map<string,string>::const_iterator it = attributs.find(nomAttribut);

    return it != attributs.end();
}

string Balise::litValeurAttribut(string nomAttribut) const {
    map<string,string>::const_iterator it = attributs.find(nomAttribut);

    if (it == attributs.end()) {
            throw runtime_error(MSG_ERREUR_ATTRIBUT_NEXISTE_PAS + nomAttribut);
        } else {
            return it->second;
        }
}

/*
 * fonction utilisé par le constructeur Balise()
 */

/* ignore les espaces entre '<' et le nom de la balise */
string trouverNom(string chaineBalise) {
    string nom = "";
    unsigned int compteur = 0;

    for (unsigned int i = 1; i < chaineBalise.length(); i++) {
        if (compteur == 0 && chaineBalise[i] == ' ') {
            compteur = 0;
        } else if (chaineBalise[i] == ' ' || chaineBalise[i] == '>' || chaineBalise[i] == '/' || chaineBalise[i] == '?') {
            break;
        } else {
            nom += chaineBalise[i];
            compteur++;
        }
    }
    return nom;
}

map<string,string> trouverAttributs(string chaineBalise) {
    map<string,string> attributs;
    string valeur;
    string nomAttribut;

    for (unsigned int i = 0; i < chaineBalise.length(); i++) {
        if (chaineBalise[i] == '=') {
            nomAttribut = retournerNomAttribut(i, chaineBalise);
            valeur = retournerValeurAttribut(i, chaineBalise);
            attributs.insert(pair<string,string>(nomAttribut, valeur));
        }
    }
    return attributs;
}

/* ignore les espaces entre le nom de l'attribut et '=' */
string retournerNomAttribut(unsigned int position, string chaineBalise) {
    string nomAttribut = "";
    unsigned int compteur = 0;

    for (unsigned int i = position-1; i >= 0; i--) {
        if (compteur == 0 && chaineBalise[i] == ' ') {
            compteur = 0;
        } else if (chaineBalise[i] != ' ') {
            nomAttribut = chaineBalise[i] + nomAttribut;
            compteur++;
        } else {
            break;
        }
    }
    return nomAttribut;
}

/* ignore les espaces entre le '=' et la valeur de l'attribut */
string retournerValeurAttribut(unsigned int position, string chaineBalise) {
    bool estValeur = false;
    string valeur = "";

    for (unsigned int i = position+1; i < chaineBalise.length(); i++) {
        if (chaineBalise[i] == '"') {
            if (estValeur) {
                break;
            } else {
                estValeur = true;
            }
        } else if (estValeur) {
            valeur += chaineBalise[i];
        }
    }
    return valeur;
}

TypeBalise trouverType(string chaineBalise) {

    if (chaineBalise.find("<?") != string::npos && chaineBalise.find("?>") != string::npos) {
        return DIRECTIVE;
    } else if (chaineBalise.find("</") != string::npos) {
        return FIN;
    } else if (chaineBalise.find("/>") != string::npos) {
        return DEBUTFIN;
    } else {
        return DEBUT;
    }
}

#endif
