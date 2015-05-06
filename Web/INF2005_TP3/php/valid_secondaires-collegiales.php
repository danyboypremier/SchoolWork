<?php

/*
 *  Validation de la section renseignements sur les études secondaires au Québec
 */
function secondcollege_valid_secondaire_content() {
    $errMsgList = array();

    if (has_secondaire_study_data()) {
        if (!has_all_secondaire_study_data()) {
            array_push($errMsgList, "Renseignements sur les études secondaires incomplets");
        } else {
            // Études secondaires valides. Validation de la logique des dates
            if ($_POST["secondcollege_annee_debut_1"] >= $_POST["secondcollege_annee_fin_1"]) {
                array_push($errMsgList, "La date de début d'études secondaires au Québec ne doit pas "
                        . "être supérieur ou égal à celle de fin");
            }
            
            if ($_POST["secondcollege_annee_debut_2"] >= $_POST["secondcollege_annee_fin_2"]) {
                array_push($errMsgList, "La date de début d'une spécialisation au secondaires"
                        . " ne doit pas être supérieur ou égal à celle de fin");
            }
            
            if (($_POST["secondcollege_annee_fin_1"] > $_POST["secondcollege_obtention_annee_1"])
                    || $_POST["secondcollege_annee_fin_2"] > $_POST["secondcollege_obtention_annee_1"]) {
                array_push($errMsgList, "La date de l'obtention d'un diplôme d'études secondaires "
                        . "ne doit pas être inférieur à celle de la fin d'une période de fréquentation");
            }
        }
    }

    return $errMsgList;
}


/*
 *  Validation de la section renseignements sur les études collégiales
 */
function secondcollege_valid_collegiale_content() {
    $errMsgList = array();

    // Traitement si un des champs dec/aec est sélectionné
    if (has_collegiale_study_fields()) {
        if (!has_all_collegiale_study_fields()) {
            array_push($errMsgList, "Renseignements sur les études collégiales vide ou incomplets");
        } else {
            // Étude collégiales valide. Validation des dates de fréquentation
            if ($_POST["secondcollege_annee_debut_3"] >= $_POST["secondcollege_annee_fin_3"]) {
                array_push($errMsgList, "La date de début d'études collégiales ne doit pas être "
                        . "supérieur ou égal à celle de fin");
            }
            
            if (strcmp($_POST["secondcollege_dec_obtention"], "obtenu") === 0) {
                // Diplôme obtenu, une date d'obtention doit être spécifiée
                if (empty($_POST["secondcollege_obtention_mois_2"]) || empty($_POST["secondcollege_obtention_annee_2"])) {
                    array_push($errMsgList, "Une date d'obtention pour le diplôme d'études collégiales doit être spécifiée");
                // Date d'obtention présente, valide la logique
                } else if ($_POST["secondcollege_annee_fin_3"] > $_POST["secondcollege_obtention_annee_2"]) {
                    array_push($errMsgList, "La date de l'obtention d'un diplôme d'études collégiales "
                            . "ne doit pas être inférieur à celle de la fin de la période de fréquentation");
                }
            } else {
                // Aucune diplôme complété, les champs d'obtention doivent être vides
                if (!empty($_POST["secondcollege_obtention_mois_2"]) || !empty($_POST["secondcollege_obtention_annee_2"])) {
                    array_push($errMsgList, "Aucun diplôme d'études collégiales complété. La date d'obtention doit être vide");
                }
            }
        }
    }
    
    return $errMsgList;
}


/*
 * Fonctions utiles à cette classe
 */

// Valide si un champs des études secondaires est utilisé
function has_secondaire_study_data() {
    if (!empty($_POST["secondcollege_check_etude"]) 
            || !empty($_POST["secondcollege_derniere_annee_sec"]) 
            || !empty($_POST["secondcollege_annee_debut_1"]) 
            || !empty($_POST["secondcollege_annee_fin_1"])
            || !empty($_POST["secondcollege_check_etude_sec_exterieur"]) 
            || !empty($_POST["secondcollege_discipline_1"]) 
            || !empty($_POST["secondcollege_annee_debut_2"]) 
            || !empty($_POST["secondcollege_annee_fin_2"])
            || !empty($_POST["secondcollege_institution_1"])
            || !empty($_POST["secondcollege_obtention_mois_1"])
            || !empty($_POST["secondcollege_obtention_annee_1"])) {
        return true;
    }
    
    return false;
}

// Valide que tous les champs des études secondaires sont utilisés
function has_all_secondaire_study_data() {
    if (!empty($_POST["secondcollege_check_etude"]) 
            && !empty($_POST["secondcollege_derniere_annee_sec"]) 
            && !empty($_POST["secondcollege_annee_debut_1"]) 
            && !empty($_POST["secondcollege_annee_fin_1"])
            && !empty($_POST["secondcollege_discipline_1"]) 
            && !empty($_POST["secondcollege_annee_debut_2"]) 
            && !empty($_POST["secondcollege_annee_fin_2"])
            && !empty($_POST["secondcollege_institution_1"])
            && !empty($_POST["secondcollege_obtention_mois_1"])
            && !empty($_POST["secondcollege_obtention_annee_1"])) {
        return true;
    }
    
    return false;
}

// Valide si un champs des études collégiales/aec est utilisé
function has_collegiale_study_fields() {
    if (!empty($_POST["secondcollege_dec_aec"]) 
            || !empty($_POST["secondcollege_nom_diplome_dec_aec"]) 
            || !empty($_POST["secondcollege_dec_obtention"]) 
            || !empty($_POST["secondcollege_institution_dec_aec"]) 
            || !empty($_POST["secondcollege_annee_debut_3"])
            || !empty($_POST["secondcollege_annee_fin_3"])
            || !empty($_POST["secondcollege_discipline_dec_aec"])
            || !empty($_POST["secondcollege_obtention_mois_2"])
            || !empty($_POST["secondcollege_obtention_annee_2"])) {
        return true;
    }
    
    return false;
}

// Valide si tous les champs des études collégiales/aec sont utilisés
function has_all_collegiale_study_fields() {  
    if (!empty($_POST["secondcollege_dec_aec"]) 
            && !empty($_POST["secondcollege_nom_diplome_dec_aec"]) 
            && !empty($_POST["secondcollege_dec_obtention"]) 
            && !empty($_POST["secondcollege_institution_dec_aec"]) 
            && !empty($_POST["secondcollege_annee_debut_3"])
            && !empty($_POST["secondcollege_annee_fin_3"])
            && !empty($_POST["secondcollege_discipline_dec_aec"])) {
        return true;
    }
    
    return false;
}
