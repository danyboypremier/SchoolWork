/*  balise.hpp : module de gestion de balises (style HTML ou XML)

    Seules les exceptions sp�cifi�es ci-dessous doivent �tre impl�ment�es
    Emmanuel Chieze, UQAM, INF3105, TP2
*/

#ifndef BALISE_HPP
#	define BALISE_HPP
#include <string>
#include <map>
using namespace std;

/*  TypeBalise :
    definit les quatre types de balises gerees :
        1) balises de debut (<TEXT>) : ne contiennent aucun / ni ? au d�but, et aucun / ni ? � la fin
        2) balises de fin (</TEXT>) : commencent pas un /
        3) balises de d�but qui se terminent (donc sans contenu) (<TEXT/>) : se terminent par un /
        4) balises directives (<?TEXT?>) : commencent et se terminent par ?
    Les commentaires et meta-commandes (<!...>) ne sont pas geres par le module
*/
typedef enum {DEBUT, FIN, DEBUTFIN, DIRECTIVE} TypeBalise;

class Balise {
    public:
    /* Balise :
    cree une balise a partir de son contenu textuel. chaineBalise contient le contenu de la balise (incluant < et >).
    Dans le cas de commentaires, une exception domain_error est lev�e.
    Dans le cas o� une balise mentionne un attribut mais aucune valeur associ�e, une exception runtime_error est lev�e.
    Dans le cas o� la valeur d'un attribut n'est pas entour�e de guillements, une exception runtime_error est lev�e.
    */
    Balise(string chaineBalise);

    // litNom : renvoie le nom d'une balise
    string litNom() const;

    // litType : renvoie le type d'une balise
    TypeBalise litType() const;

    // estAttribut : v�rifie si un attribut du nom fourni en param�tre existe dans la balise
    bool estAttribut(string nomAttribut) const;

    /* litValeurAttribut : retourne la valeur d'un attribut dont le nom est fourni en param�tre.
    Dans le cas o� cet attribut n'existe pas, une exception runtime_error est lev�e.
    */
    string litValeurAttribut(string nomAttribut) const;

    private:
        string nom;
        map<string,string> attributs;
        TypeBalise type;
};
#endif /* BALISE_HPP */