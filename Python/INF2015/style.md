# Norme de codification #

Le style du projet est basé sur le [*Style Guide for Python Code*](http://legacy.python.org/dev/peps/pep-0008/) de la communauté Python.

Vous trouverez ici un petit résumé des points importants et un exemple de code comportant la majorité du formatage accepté.

## Langue utilisée pour le nommage et les descriptions ##
- Utilisez le français. ('get' et 'set' sont permis dans les noms de méthode)
- Utilisez des mots complets.

## Mise en forme verticale ##
- Taille maximale de 500 lignes.
- Dans les classes, il y a une ligne de séparation entre chaque bloc.
- Dans le fichier, il y a deux lignes de séparation entre chaque classe.

## Mise en forme horizontale ##
- 4 espaces par niveau d'indentation.
- Les fichiers de code ont une longueur de ligne de 120 caractères maximum.
- Quand la ligne dépasse les 120 caractères, il faut faire un saut de ligne et ajouter deux indentations.
- Les opérateurs sont entourés d'espaces. (sauf lors d'une affectation en paramètre)
- Il n'y a pas d'espace entre le nom de la fonction, la parenthèse et son paramètre.
- Lorsqu'il y a plusieurs paramètres, mettre un espace après chaque virgule.

## Casse utilisée pour le nommage des variables, classes, fonctions ##
- Nom de classe = PascalCase
- Nom de fonction = snake_case
- Nom de variable = snake_case
- Nom de dictionnaire = snake_case
- Constantes = MAJUSCULE_ET_SOULIGNEMENT

## Exemple de code ##
``` python
    def fonction_inutile (argument_inutile, autre_argument_inutile):
        variable_temporaire = (2 + argument_inutile) + (2 * autre_argument_inutile)
        variable_temporaire += 2
        if variable_temporaire == VALEUR_ZERO:
            faire_des_choses(variable_temporaire)
        else:
            faire_autre_chose(variable_temporaire + 
                    suite_de_la_meme_operation)
```
