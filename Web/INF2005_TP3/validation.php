<?php
require("php/display_results.php");
require("php/validation_tools.php");
require("php/valid_identification.php");
require("php/valid_programmes.php");
require("php/valid_secondaires-collegiales.php");
require("php/valid_universitaires.php");
require("php/valid_emplois.php");
require("php/write_form.php");

$errMsgList = array(); // Liste des messages à afficher pour l'ensemble des erreurs rencontrées


// Validation de la section "Identification"
$errMsgList = array_merge($errMsgList, ident_valid_required());
$errMsgList = array_merge($errMsgList, ident_valid_optional());

// Validation de la section "Programmes Demandés"
$errMsgList = array_merge($errMsgList, programme_valid_required());
$errMsgList = array_merge($errMsgList, programme_valid_second_choice());
$errMsgList = array_merge($errMsgList, programme_valid_third_choice());

// Validation des renseignements d'études secondaires et collégiales
$errMsgList = array_merge($errMsgList, secondcollege_valid_secondaire_content());
$errMsgList = array_merge($errMsgList, secondcollege_valid_collegiale_content());

// Validation des renseignements d'études universitaires
$errMsgList = array_merge($errMsgList, universitaires_valid_primary_content());
$errMsgList = array_merge($errMsgList, universitaires_valid_other_content());

// Validation des renseignements sur les emplois
$errMsgList = array_merge($errMsgList, emplois_valid_first_content());
$errMsgList = array_merge($errMsgList, emplois_valid_second_content());
$errMsgList = array_merge($errMsgList, emplois_valid_third_content());

// Affichage
display_results($errMsgList);

// Écriture dans un fichier si aucune erreurs
if (empty($errMsgList)) {
    write_form_data();
}
