<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Traiteur Le berger</title>
    <link href="CSS/TP2_CSS.css" rel="stylesheet" type="text/css">
</head>
<body>
<?php
// constantes
define("CAR_NON_ACCEPTES", "/,/");
define("CAR_NUM_ACCEPTES", "/[0-9]/");

define("chemin_commande", "Pages/commande.html");

define("CHEMIN_FIC_SAUVEGARDE", "Data/commande.txt");
define("CHEMIN_HEADER", "Template/header.txt");
define("CHEMIN_FOOTER", "Template/footer.txt");

// déclaration des variables du formulaire
$nom_parent = ajuster_entree($_POST["nom_parent"]);
$nom_enfant = ajuster_entree($_POST["nom_enfant"]);
$ecole = ajuster_entree($_POST["ecole"]);
$age = ajuster_entree($_POST["age"]);

$lundi = $mardi = $mercredi = $jeudi = $vendredi = "";

// déclaration de la variable pour l'affichage des messages d'erreurs
$messageErreur = "";

// ouverture des templates pour l'affichage
$header = fopen(CHEMIN_HEADER, 'r');
$footer = fopen(CHEMIN_FOOTER, 'r');


// début du main
// validation des données du formulaire
if (empty($nom_parent) || preg_match(CAR_NON_ACCEPTES, $nom_parent)) {
    $messageErreur = $messageErreur . "Le champs 'Nom du parent' est vide ou contient un ','\n\t";
}

if (empty($nom_enfant) || preg_match(CAR_NON_ACCEPTES, $nom_enfant)) {
    $messageErreur = $messageErreur . "Le champs 'Nom de l'enfant' est vide ou contient un ','\n\t";
}

if (empty($ecole) || preg_match(CAR_NON_ACCEPTES, $ecole)) {
    $messageErreur = $messageErreur . "Le champs 'École' est vide ou contient un ','\n\t";
}

if (empty($age) || !preg_match(CAR_NUM_ACCEPTES, $age) || $age < 4 || $age > 12) {
    $messageErreur = $messageErreur . "Le champs 'Âge' est vide ou contient un caractère alphanumérique et doit " .
        "être entre 4 et 12 inclusivement\n\t";
}

if (isset($_POST["lundi"]) && isset($_POST["mardi"]) && isset($_POST["mercredi"])
    && isset($_POST["jeudi"]) && isset($_POST["vendredi"])
) {
    $lundi = $_POST["lundi"];
    $mardi = $_POST["mardi"];
    $mercredi = $_POST["mercredi"];
    $jeudi = $_POST["jeudi"];
    $vendredi = $_POST["vendredi"];
} else {
    $messageErreur = $messageErreur . "Vous devez selectionner un repas pour chaque jour de la semaine\n\t";
}

// traitement des données du formulaire
if (!empty($messageErreur)) {
    echo "<pre>";
    echo "<h2>ERREUR! :</h2>\n\t" . $messageErreur;
    echo "</pre>";
    echo "<p><a href=" . chemin_commande . ">Retourner au formulaire de commande</a></p>";

} else if (!enregistrer_commande(
    "Parent:" . $nom_parent . ", " .
    "Enfant:" . $nom_enfant . ", " .
    "Âge:" . $age . ", " .
    "École:" . $ecole . ", " .
    "Lundi:" . $lundi . ", " .
    "Mardi:" . $mardi . ", " .
    "Mercredi:" . $mercredi . ", " .
    "Jeudi:" . $jeudi . ", " .
    "Vendredi:" . $vendredi)) {
    echo "ERREUR lors de l'enregistrement du fichier... svp recommencer... <br>";
    echo "Si l'erreur se reproduit, veuillez communiquer avec nous le plus rapidement possible, merci.";

} else {
    echo fread($header, filesize(CHEMIN_HEADER));

    echo "<div class=\"contenu_resultat\">";
    echo "<h2>";
    echo "Confirmation de l'enregistrement de la commande";
    echo "</h2>";
    echo "<blockquote><p>";
    echo "Pour tout changement, veuillez nous téléphoner directement, aucun changement par e-mail ne sera accepté";
    echo "</p></blockquote>";
    echo "</div>";
    echo "<div class=\"resultat\">";
    echo "<pre >";

    echo "Parent:\t\t" . $nom_parent . "<br>" .
        "Enfant:\t\t" . $nom_enfant . "<br>" .
        "Âge:\t\t" . $age . "<br>" .
        "École:\t\t" . $ecole . "<br>" .
        "Lundi:\t\t" . $lundi . "<br>" .
        "Mardi:\t\t" . $mardi . "<br>" .
        "Mercredi:\t" . $mercredi . "<br>" .
        "Jeudi:\t\t" . $jeudi . "<br>" .
        "Vendredi:\t" . $vendredi;

    echo "</pre>";
    echo "</div>";

    echo fread($footer, filesize(CHEMIN_FOOTER));
}

// fermeture des fichiers template
fclose($header);
fclose($footer);


// fonction qui enlève les espaces au début, à la fin, et ceux superflus entre les mots
function ajuster_entree($donnee) {
    $donnee = trim($donnee, ' ');
    $donnee = preg_replace('/\s\s+/', ' ', $donnee);
    return $donnee;
}

// retourne false si il y a une erreur à l'enregistrement
function enregistrer_commande($chaine) {
    $doc = fopen(CHEMIN_FIC_SAUVEGARDE, 'a');

    return (fwrite($doc, "\n" . $chaine) || fclose($doc));
}

?>
</body>
</html>