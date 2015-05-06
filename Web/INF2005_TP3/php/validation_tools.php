<?php
define("REGEX_DATE", "/^[0-9]{4}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$/"); // 9999-99-99

/*
 * Classe utilitaire pour l'ensemble des validations
 */

// Retourne vrai si la date est au format ISO8601
function is_ISO8601_date($date) {
    if (preg_match(REGEX_DATE, $date)) {
        $date = date_parse_from_format("Y.m.d", $date); // Str à array, utilisant le format ISO8601

        if (checkdate($date['month'], $date['day'], $date['year'])) {
            return true;
        }
    }
    
    return false;
}
