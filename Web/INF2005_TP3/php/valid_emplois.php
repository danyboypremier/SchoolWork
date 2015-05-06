<?php

/*
 * Traitement premier emploi
 */
function emplois_valid_first_content() {
    $errMsgList = array();
    $emploiNb = 1; // Numéro de l'emploi
    
    if (has_emploi($emploiNb)) {
        if (!has_all_emploi_fields($emploiNb)) {
            array_push($errMsgList, "Renseignements sur le premier emploi incomplets");
        } else {
            // Premier emploi valide, vérification des dates
            if (!has_valid_duration_dates($emploiNb)) {
                array_push($errMsgList, "Les dates pour la durée du premier emploi non sont pas cohérentes");
            }
            
            if (!is_ISO8601_date($_POST["emploi_date_attestation_1"])) {
                array_push($errMsgList, "La date d'expédition de l'attestation du premier emploi "
                        . "doit être au format AAAA-MM-JJ");
            }
        }
    }

    return $errMsgList;
}


/*
 * Traitement deuxième emploi
 */
function emplois_valid_second_content() {
    $errMsgList = array();
    $emploiNb = 2; // Numéro de l'emploi
    
    if (has_emploi($emploiNb)) {
        if (!has_all_emploi_fields($emploiNb)) {
            array_push($errMsgList, "Renseignements sur le second emploi incomplets");
        } else {
            // Second emploi valide, vérification des dates
            if (!has_valid_duration_dates($emploiNb)) {
                array_push($errMsgList, "Les dates pour la durée du second emploi non sont pas cohérentes");
            }
            
            if (!is_ISO8601_date($_POST["emploi_date_attestation_2"])) {
                array_push($errMsgList, "La date d'expédition de l'attestation du second emploi "
                        . "doit être au format AAAA-MM-JJ");
            }
        }
    }

    return $errMsgList;
}


/*
 * Traitement troisième emploi
 */
function emplois_valid_third_content() {
    $errMsgList = array();
    $emploiNb = 3; // Numéro de l'emploi
    
    if (has_emploi($emploiNb)) {
        if (!has_all_emploi_fields($emploiNb)) {
            array_push($errMsgList, "Renseignements sur le troisième emploi incomplets");
        } else {
            // Troisième emploi valide, vérification des dates
            if (!has_valid_duration_dates($emploiNb)) {
                array_push($errMsgList, "Les dates pour la durée du troisième emploi non sont pas cohérentes");
            }
            
            if (!is_ISO8601_date($_POST["emploi_date_attestation_3"])) {
                array_push($errMsgList, "La date d'expédition de l'attestation du troisième emploi "
                        . "doit être au format AAAA-MM-JJ");
            }
        }
    }

    return $errMsgList;
}


/*
 * Fonction utile à cette class
 */
// Valide si un champs d'un emploi est utilisé
function has_emploi($emploiNb) {
    if (!empty($_POST["emploi_nom_employeur_".$emploiNb]) 
            || !empty($_POST["emploi_duree_de_mois_".$emploiNb]) 
            || !empty($_POST["emploi_duree_de_annee_".$emploiNb]) 
            || !empty($_POST["emploi_type_emploi_".$emploiNb]) 
            || !empty($_POST["emploi_duree_a_mois_".$emploiNb]) 
            || !empty($_POST["emploi_duree_a_annee_".$emploiNb]) 
            || !empty($_POST["emploi_date_attestation_".$emploiNb])) {
        
        return true;
    }

    return false;
}

// Valide que tous les champs d'un emploi sont utilisés
function has_all_emploi_fields($emploiNb) {
    if (!empty($_POST["emploi_nom_employeur_".$emploiNb]) 
            && !empty($_POST["emploi_duree_de_mois_".$emploiNb]) 
            && !empty($_POST["emploi_duree_de_annee_".$emploiNb]) 
            && !empty($_POST["emploi_type_emploi_".$emploiNb]) 
            && !empty($_POST["emploi_duree_a_mois_".$emploiNb]) 
            && !empty($_POST["emploi_duree_a_annee_".$emploiNb]) 
            && !empty($_POST["emploi_date_attestation_".$emploiNb])) {
        
        return true;
    }

    return false;
}

// Valide que la date de durée d'un emploi est valide
function has_valid_duration_dates($emploiNb) {
    if ($_POST["emploi_duree_de_annee_".$emploiNb] < $_POST["emploi_duree_a_annee_".$emploiNb]) {
        // Si année de début plus petite, automatiquement valide.
        return true;
    } else if ($_POST["emploi_duree_de_annee_".$emploiNb] == $_POST["emploi_duree_a_annee_".$emploiNb]) {
        // Si année identique, le mois de début doit être inférieur ou égal à celui de fin
        if ($_POST["emploi_duree_de_mois_".$emploiNb] <= $_POST["emploi_duree_a_mois_".$emploiNb]) {
            return true;
        }
    }
    
    return false;
}
