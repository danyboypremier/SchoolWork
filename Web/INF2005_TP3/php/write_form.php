<?php

define("FILE_PATH", "demandes/"); // Dossier pour l'ensemble des demandes reçus

// Fonction d'écriture dans un fichier des données reçus de POST 
function write_form_data() {
    $file = FILE_PATH . $_POST["ident_code"] .".csv"; // Chemin et nom du fichier au format CSV
    $formCSV = ""; // Chaîne des données du formulaire au format CSV
    
    $formCSV = build_CSV_string();

    utf8_encode($formCSV);
    file_put_contents($file, $formCSV.PHP_EOL);
}


// Création d'une chaîne au format CSV avec le caractère ";" comme séparateur
function build_CSV_string() {
    $CSVStr = "";
    $replaceBy = "_"; // Remplacement pour le caractère ";", si celui-ci est présent dans une chaîne
    
    foreach ($_POST as $name => $value) {
        if (!empty($value)) {
            $CSVStr = $CSVStr . str_replace(";", $replaceBy, $value);
        }
        $CSVStr = $CSVStr . ";";
    }
    
    $CSVStr = substr_replace($CSVStr, "", -1); // Retire le dernier ";" ajouté en trop
    
    return $CSVStr;
}
