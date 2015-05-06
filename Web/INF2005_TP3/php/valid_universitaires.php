<?php

/*
 *  Validation du premier diplôme d'études universitaires
 */
function universitaires_valid_primary_content() {
    $errMsgList = array();
    
    if (has_university_study()) {
        if (!has_all_university_study_fields()) {
            array_push($errMsgList, "Renseignements sur le diplôme d'études universitaires incomplets");
        } else {
            // Premier diplôme d'études universitaires valide
            if ($_POST["universitaires_annee_debut"] >= $_POST["universitaires_annee_fin"]) {
                array_push($errMsgList, "La date de début d'études universitaires ne doit pas "
                        . "être supérieur ou égal à celle de fin");
            }
            
            if (strcmp($_POST["universitaires_obtention"], "obtenu") === 0) {
                // Diplôme obtenu, une date d'obtention doit être spécifiée
                if (empty($_POST["universitaires_obtention_mois"]) || empty($_POST["universitaires_obtention_annee"])) {
                    array_push($errMsgList, "Une date d'obtention pour le premier diplôme universitaire doit être spécifiée");
                // Date d'obtention présente, valide la logique
                } else if ($_POST["universitaires_annee_fin"] > $_POST["universitaires_obtention_annee"]) {
                    array_push($errMsgList, "La date de l'obtention du premier diplôme d'études universitaires "
                            . "ne doit pas être inférieur à celle de la fin de la période de fréquentation");
                }
            } else {
                // Aucune diplôme complété, les champs d'obtention doivent être vides
                if (!empty($_POST["universitaires_obtention_mois"]) || !empty($_POST["universitaires_obtention_annee"])) {
                    array_push($errMsgList, "Aucun premier diplôme d'études universitaires complété. La date d'obtention doit être vide");
                }
            }
        }
    }

    return $errMsgList;
}
            

/*
 *  Validation du second diplôme d'études universitaires
 */
function universitaires_valid_other_content() {
    $errMsgList = array();
    
    if (has_other_university_study()) {
        if (!has_all_other_university_study_fields()) {
            array_push($errMsgList, "Renseignements sur le second diplôme d'études universitaires incomplets");
        } else {
            // Second diplôme d'études universitaires valide
            if ($_POST["universitaires_annee_debut_autre"] >= $_POST["universitaires_annee_fin_autre"]) {
                array_push($errMsgList, "La date de début d'études universitaires pour le second diplôme"
                        . " ne doit pas être supérieur ou égal à celle de fin");
            }
            
            if (strcmp($_POST["universitaires_obtention_autre"], "obtenu") === 0) {
                // Diplôme obtenu, une date d'obtention doit être spécifiée
                if (empty($_POST["universitaires_obtention_mois_autre"]) || empty($_POST["universitaires_obtention_annee_autre"])) {
                    array_push($errMsgList, "Une date d'obtention pour le second diplôme universitaire doit être spécifiée");
                // Date d'obtention présente, valide la logique
                } else if ($_POST["universitaires_annee_fin_autre"] > $_POST["universitaires_obtention_annee_autre"]) {
                    array_push($errMsgList, "La date de l'obtention du second diplôme d'études universitaires "
                            . "ne doit pas être inférieur à celle de la fin de la période de fréquentation");
                }
            } else {
                // Aucune diplôme complété, les champs d'obtention doivent être vides
                if (!empty($_POST["universitaires_obtention_mois_autre"]) || !empty($_POST["universitaires_obtention_annee_autre"])) {
                    array_push($errMsgList, "Aucun second diplôme d'études universitaires complété. La date d'obtention doit être vide");
                }
            }
        }
    }

    return $errMsgList;
}


/*
 * Fonction utile à cette class
 */
// Valide si un champs du premier diplôme universitaire est utilisé
function has_university_study() { 
    if (!empty($_POST["universitaires_check_universite"]) 
            || !empty($_POST["universitaires_nom_diplome"]) 
            || !empty($_POST["universitaires_obtention"])
            || !empty($_POST["universitaires_institution"])
            || !empty($_POST["universitaires_annee_debut"])
            || !empty($_POST["universitaires_annee_fin"])
            || !empty($_POST["universitaires_discipline"])
            || !empty($_POST["universitaires_obtention_mois"])
            || !empty($_POST["universitaires_obtention_annee"])) {
        
        return true;
    }

    return false;
}

// Valide que tous les champs du premier diplôme universitaire sont utilisés
function  has_all_university_study_fields() {
    if (!empty($_POST["universitaires_check_universite"]) 
            && !empty($_POST["universitaires_nom_diplome"]) 
            && !empty($_POST["universitaires_obtention"])
            && !empty($_POST["universitaires_institution"])
            && !empty($_POST["universitaires_annee_debut"])
            && !empty($_POST["universitaires_annee_fin"])
            && !empty($_POST["universitaires_discipline"])) {
        
        return true;
    }

    return false;
}

// Valide si un champs du second diplôme universitaire est utilisé
function has_other_university_study() { 
    if (!empty($_POST["universitaires_check_autre"]) 
            || !empty($_POST["universitaires_nom_diplome_autre"])
            || !empty($_POST["universitaires_obtention_autre"])
            || !empty($_POST["universitaires_institution_autre"])
            || !empty($_POST["universitaires_annee_debut_autre"])
            || !empty($_POST["universitaires_annee_fin_autre"])
            || !empty($_POST["universitaires_discipline_autre"])
            || !empty($_POST["universitaires_obtention_mois_autre"])
            || !empty($_POST["universitaires_obtention_annee_autre"])) {
        
        return true;
    }

    return false;
}

// Valide que tous les champs du second diplôme universitaire sont utilisés
function  has_all_other_university_study_fields() {
    if (!empty($_POST["universitaires_check_autre"]) 
            && !empty($_POST["universitaires_nom_diplome_autre"]) 
            && !empty($_POST["universitaires_obtention_autre"])
            && !empty($_POST["universitaires_institution_autre"])
            && !empty($_POST["universitaires_annee_debut_autre"])
            && !empty($_POST["universitaires_annee_fin_autre"])
            && !empty($_POST["universitaires_discipline_autre"])) {
        
        return true;
    }

    return false;
}
