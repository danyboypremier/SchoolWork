/* fichierBalises.hpp : Module implementant la lecture sequentielle d'un fichier de balises (style HTML ou XML) (lecture element d'information par element d'information, ou un element d'information est soit une balise, soit un morceau de texte de taille maximale)

On suppose que les caracteres < et > ne servent qu'a specifier des balises, et qu'ils sont representes par &lt; et &gt; pour designer le caractere lui-meme.

Emmanuel Chieze, UQAM, INF3105, TP2
*/

#ifndef FICHIERBALISES_HPP
#	define FICHIERBALISES_HPP
#include <fstream>
#include "balise.hpp"
using namespace std;

class FichierBalises{
    public:
    /* FichierBalises
	Ouvre un fichier texte qui sera interprete comme un fichier de balises.
	L�ve une exception de type runtime_error en cas d'impossibilit� d'ouvrir le fichier
    */
    FichierBalises(char * nomFichier);

    /* fichierBalisesFerme :
	Ferme un fichier prealablement ouvert par fichierBalisesOuvre
    */
    ~FichierBalises();

    /* litProchaineBalise :
    Renvoie la prochaine balise pr�sente dans le fichier non encore retourn�e par litProchaineBalise.
    Saute par-dessus d'�ventuelles zones textuelles le cas �ch�ant.
    L�ve une exception de type range_error lorsqu'on atteint la fin du fichier (avant qu'une balise n'ait commenc� � �tre sp�cifi�e)
            (par exemple dans le cas d'un fichier se terminant par <TOTO attr1="toto">)
    L�ve une exception de type  lorsqu'on atteint la fin du fichier alors qu'une balise �tait en cours de lecture
        (par exemple dans le cas d'un fichier se terminant par <TOTO attr1="toto")
    */
    Balise litProchaineBalise();

    private :
        ifstream fichier;
};
#endif /* FICHIERBALISES_HPP */
