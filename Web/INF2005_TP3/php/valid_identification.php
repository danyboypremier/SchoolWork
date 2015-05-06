<?php

/*
 * Quelques constantes 
 */
define("REGEX_STUDENT_CODE", "/^[a-zA-Z]{4}[0-9]{8}$/"); // XXXX99999999
define("REGEX_PHONE_AREA", "/^[0-9]{3}$/"); // 999
define("REGEX_PHONE", "/^[0-9]{3}-[0-9]{4}$/"); // 999-9999
define("REGEX_POSTAL_CODE", "/^[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{1}[0-9]{1}$/"); // X9X9X9


/*
 * Validation des champs obligatoires
 */
function ident_valid_required() {
    $errMsgList = array();
    
    if (!has_first_and_last_name($_POST["ident_prenom"], $_POST["ident_nom"])) {
        array_push($errMsgList, "Champs du nom et du prenom de l'étudiant vides ou incomplets");
    }
    
    if (empty($_POST["ident_code"])) {
        array_push($errMsgList, "Champ du code permanent du ministère vide");
    } else {
        if (!preg_match(REGEX_STUDENT_CODE, $_POST["ident_code"])) {
            array_push($errMsgList, "Code du ministère non valide!");
        }
    }
    
    if (empty($_POST["ident_date_naissance"])) {
        array_push($errMsgList, "Champ de la date de naissance vide");
    } else {
        if (!is_ISO8601_date($_POST["ident_date_naissance"])) {
            array_push($errMsgList, "La date de naissance n'est pas valide");
        }
    }

    if (empty($_POST["ident_sexe"])) {
        array_push($errMsgList, "Champ du sexe vide");
    }

    if (empty($_POST["ident_citoyennete"])) {
        array_push($errMsgList, "Champ de citoyenneté vide");
    } else if (strcmp ($_POST["ident_citoyennete"], "autre") === 0 && empty($_POST["ident_citoyennete_texte"])) {
        array_push($errMsgList, 'À la sélection de "Autre Citoyenneté", son nom doit être précisé');
    }
    
    if (empty($_POST["ident_ville_naissance"])) {
        array_push($errMsgList, "Champ du lieu de naissance vide");
    }
    
    if (empty($_POST["ident_langue_usage"])) {
        array_push($errMsgList, "Champ de langue d'usage vide");
    } else if (strcmp ($_POST["ident_langue_usage"], "autre") === 0 && empty($_POST["ident_langue_usage_autre"])) {
        array_push($errMsgList, 'À la sélection de "Autre langue d' . "'". 'usage", son nom doit être précisé');
    }
    
    if (empty($_POST["ident_langue_mater"])) {
        array_push($errMsgList, "Champ de langue maternelle vide");
    } else if (strcmp ($_POST["ident_langue_mater"], "autre") === 0 && empty($_POST["ident_langue_mater_autre"])) {
        array_push($errMsgList, 'À la sélection de "Autre langue maternelle", son nom doit être précisé');
    }
    
    if (!has_phone_number()) {
        array_push($errMsgList, "Au moins un numéro de téléphone pour vous joindre est requis");
    }
     
    if (!is_address_complete()) {
        array_push($errMsgList, "Adresse de correspondance vide ou incomplète");
    } else {
        if (!preg_match(REGEX_POSTAL_CODE, str_replace(' ', '', $_POST["ident_code_postal"]))) {
            array_push($errMsgList, "Le format du code postal de correspondance n'est pas valide");
        }
        if (!is_numeric(str_replace(' ', '', $_POST["ident_num_civique"]))) {
            array_push($errMsgList, "Le numéro civique de l'adresse de correspondance doit être un nombre");
        }
    }

    if (empty($_POST["ident_statut"])) {
        array_push($errMsgList, "Champ de statut au Canada vide");
    }

    return $errMsgList;
}


/*
 * Champs non obligatoires. Validation seulement si le champs n'est pas vide
 */
function ident_valid_optional() {
    $errMsgList = array();
    
    // Le code permanent UQAM (format XXXX99999999)
    if (!empty($_POST["ident_code_uqam"])) {
        if (!preg_match(REGEX_STUDENT_CODE, $_POST["ident_code_uqam"])) {
            array_push($errMsgList, "Code du UQAM non valide");
        }
    }

    // Assurance Sociale (Chiffres seulement, espaces permises)
    if (!empty($_POST["ident_assurance_so"])) {
        if (!is_numeric(str_replace(' ', '', $_POST["ident_assurance_so"]))) {
            array_push($errMsgList, "Numéro d'assurance sociale non valide");
        }
    }

    // Nom père (doit comporter nom ET prénom)
    if (!empty($_POST["ident_nom_pere"]) || !empty($_POST["ident_prenom_pere"])) {
        if (!has_first_and_last_name($_POST["ident_prenom_pere"], $_POST["ident_nom_pere"])) {
            array_push($errMsgList, "Champs du nom et du prénom du père vides ou incomplets");
        }
    }

    // Nom mère (doit comporter nom ET prénom)
    if (!empty($_POST["ident_nom_mere"]) || !empty($_POST["ident_prenom_mere"])) {
        if (!has_first_and_last_name($_POST["ident_prenom_mere"], $_POST["ident_nom_mere"])) {
            array_push($errMsgList, "Champs du nom et du prénom de la mère vides ou incomplets");
        }
    }

    // Numéro des téléphones (format = 999-999-9999)
    if (!empty($_POST["ident_telephone_dom_1"]) && !empty($_POST["ident_telephone_dom_2"])) {
        if (!is_valid_phone_number($_POST["ident_telephone_dom_1"], $_POST["ident_telephone_dom_2"], null)) {
            array_push($errMsgList, "Le numéro de téléphone à domicile ne respecte pas le format XXX-XXX-XXXX");
        }
    }
    
    if (!empty($_POST["ident_telephone_tra_1"]) && !empty($_POST["ident_telephone_tra_2"])) {
        if (!is_valid_phone_number($_POST["ident_telephone_tra_1"], $_POST["ident_telephone_tra_2"], $_POST["ident_telephone_tra_3"])) {
            array_push($errMsgList, "Le numéro de téléphone au travail ne respecte pas le format XXX-XXX-XXXX");
        }
    }

    if (!empty($_POST["ident_telephone_cel_1"]) && !empty($_POST["ident_telephone_cel_2"])) {
        if (!is_valid_phone_number($_POST["ident_telephone_cel_1"], $_POST["ident_telephone_cel_2"], null)) {
            array_push($errMsgList, "Le numéro de cellulaire ne respecte pas le format XXX-XXX-XXXX");
        }
    }
    
    if (!empty($_POST["ident_telephone_parents_1"]) && !empty($_POST["ident_telephone_parents_2"])) {
        if (!is_valid_phone_number($_POST["ident_telephone_parents_1"], $_POST["ident_telephone_parents_2"], null)) {
            array_push($errMsgList, "Le numéro de téléphone des parents ne respecte pas le format XXX-XXX-XXXX");
        }
    }

    if (!empty($_POST["ident_courriel"])) {
        if (!filter_var($_POST["ident_courriel"], FILTER_VALIDATE_EMAIL)) {
            array_push($errMsgList, "Le courriel n'est pas valide");
        }
    }
    
    // Validation adresse de résidenace, si présente (Autre adresse)
    if (!empty($_POST["ident_check_adresse_res"])) {
        if (empty($_POST["ident_num_civique_2"]) || empty($_POST["ident_rue_2"]) 
            || empty($_POST["ident_municipalite_2"]) || empty($_POST["ident_code_postal_2"])) {
            array_push($errMsgList, "Adresse de résidence spécifiée mais vide ou incomplète");
        } else {
            if (!preg_match(REGEX_POSTAL_CODE, str_replace(' ', '', $_POST["ident_code_postal_2"]))) {
                array_push($errMsgList, "Le format du code postal de résidence n'est pas valide");
            }
            if (!is_numeric(str_replace(' ', '', $_POST["ident_num_civique_2"]))) {
                array_push($errMsgList, "Le numéro civique de l'adresse de résidence doit être un nombre");
            }
        }
    }
    
    return $errMsgList;
}


/*
 * Fonctions utiles à cette classe
 */

// Retourne vrai si les deux chaînes ne sont pas vides
function has_first_and_last_name($firstName, $lastName) {
    if (empty($firstName) || empty($lastName)) {
        return false;
    }
    
    return true;
}

// Retourne vrai si tous les champs requis d'une adresse ne sont pas vides
function is_address_complete() {
    if (empty($_POST["ident_num_civique"]) || empty($_POST["ident_rue"]) 
            || empty($_POST["ident_municipalite"]) || empty($_POST["ident_code_postal"])) {
        return false;
    }
    
    return true;
}

// Retourne vrai si au moins un des 3 téléphones est fournis
function has_phone_number() {
    if ((!empty($_POST["ident_telephone_dom_1"]) && !empty($_POST["ident_telephone_dom_2"])) 
            || (!empty($_POST["ident_telephone_tra_1"]) && !empty($_POST["ident_telephone_tra_2"])) 
            || (!empty($_POST["ident_telephone_cel_1"]) && !empty($_POST["ident_telephone_cel_2"]))) {
        return true;
    }
    
    return false;
}

// Retourne vrai si le numéro de téléphone respecte le format de l'énoncé
// Région:999 Numéro:999-9999 Extension:Un ou des chiffres
function is_valid_phone_number($area, $number, $ext) {
    if (preg_match(REGEX_PHONE_AREA, $area) && preg_match(REGEX_PHONE, $number)
            && ($ext == null || empty($ext) || is_numeric(str_replace(' ', '', $ext)))) {
        return true;
    }
    
    return false;
}
