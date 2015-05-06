<?php

/*
 * Validation des champs obligatoires pour le premier choix de programme
 */
function programme_valid_required() {
    $errMsgList = array();
    
    if (empty($_POST["progdemande_trimestre"])) {
        array_push($errMsgList, "Aucun trimestre sélectionné");
    }
    
    if (empty($_POST["progdemande_trimestre_annee"])) {
        array_push($errMsgList, "Aucune année précisée pour le trimestre");
    }
    
    if (!has_required_choice_fields($_POST["progdemande_choix_1_titre"], $_POST["progdemande_choix_1_code"], 
            $_POST["progdemande_choix_1_type"], $_POST["progdemande_choix_1_temps"])) {
        array_push($errMsgList, "Champs du premier choix vides ou incomplets");
    }
    
    if (empty($_POST["progdemande_presence"])) {
        array_push($errMsgList, "Présence au quebec non sélectionnée");
    } else if (strcmp ($_POST["progdemande_presence"], "non") === 0 && empty($_POST["progdemande_presence_autre"])) {
        array_push($errMsgList, "Date d'arrivée au Québec non spécifiée");
    } else if (!empty($_POST["progdemande_presence_autre"])) {
        if (!is_ISO8601_date($_POST["progdemande_presence_autre"])) {
            array_push($errMsgList, "La date d'arrivée au Québec n'est pas valide");
        }
    }

    return $errMsgList;
}


/*
 * Validation du deuxième choix
 */
function programme_valid_second_choice() {
    $errMsgList = array();
    
    if (!is_all_empty_choice_fields($_POST["progdemande_choix_2_titre"], $_POST["progdemande_choix_2_code"], 
            $_POST["progdemande_choix_2_type"], $_POST["progdemande_choix_2_temps"])) {
        if (!has_required_choice_fields($_POST["progdemande_choix_2_titre"], $_POST["progdemande_choix_2_code"], 
            $_POST["progdemande_choix_2_type"], $_POST["progdemande_choix_2_temps"])) {
            array_push($errMsgList, "Champs du deuxième choix vides ou incomplets");
        }
        
    }

    return $errMsgList;
}


/*
 * Validation du troisième choix
 */
function programme_valid_third_choice() {
    $errMsgList = array();

    if (!is_all_empty_choice_fields($_POST["progdemande_choix_3_titre"], $_POST["progdemande_choix_3_code"], 
            $_POST["progdemande_choix_3_type"], $_POST["progdemande_choix_3_temps"])) {
        if (!has_required_choice_fields($_POST["progdemande_choix_3_titre"], $_POST["progdemande_choix_3_code"], 
            $_POST["progdemande_choix_3_type"], $_POST["progdemande_choix_3_temps"])) {
            array_push($errMsgList, "Champs du troisième choix vides ou incomplets");
        }
        
    }

    return $errMsgList;
}


/*
 * Fonctions utiles à cette classe
 */
function has_required_choice_fields($titre, $code, $type, $temps) {
    if (empty($titre) || empty($code) || empty($type) || empty($temps)) {
        return false;
    }
    
    return true;
}

function is_all_empty_choice_fields($titre, $code, $type, $temps) {
    if (empty($titre) && empty($code) && empty($type) && empty($temps)) {
        return true;
    }
    
    return false;
}
