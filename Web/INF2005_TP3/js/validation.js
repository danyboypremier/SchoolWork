/********************************************************************************************************
 * fichier javascript pour la validation
 ********************************************************************************************************/

/********************************************************************************************************
 * constantes et varables
 ********************************************************************************************************/
/* constantes */
REGEX_STUDENT_CODE = /^[a-zA-Z]{4}[0-9]{8}$/; // XXXX99999999
REGEX_PHONE_AREA = /^[0-9]{3}$/; // 999
REGEX_PHONE = /^[0-9]{3}-[0-9]{4}$/; // 999-9999
REGEX_POSTAL_CODE = /^[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{1}[0-9]{1}$/; // X9X9X9
REGEX_EMAIL = /^[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+\.[a-zA-Z]{2,4}$/;
REGEX_DATE = /^[0-9]{4}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$/; // 9999-99-99
REGEX_ASSURANCE_SO = /^[0-9]{9}$/; // 999999999
REGEX_CHIFFRE = /^[0-9]+$/; // uniquement des chiffres

/* variables */
progChoix2 = document.getElementsByClassName("choix_2");
progChoix3 = document.getElementsByClassName("choix_3");

/********************************************************************************************************
 * fonctions principales
 ********************************************************************************************************/

/* appeler la validation en fonction de la section complétée */
function appelerValidation(ident) {
    switch (ident.id) {
        case "div_formulaire_1_1":
            return validerFormulaire_1_1();
        case "div_formulaire_1_2":
            return validerFormulaire_1_2();
        case "div_formulaire_1_3":
            return validerFormulaire_1_3();
        case "div_formulaire_1_4":
            return validerFormulaire_1_4();
        case "div_formulaire_1_5":
            return validerFormulaire_1_5();
        case "div_formulaire_2_1":
            return validerFormulaire_2_1();
        case "div_formulaire_3_1":
            return validerFormulaire_3_1();
        case "div_formulaire_3_2":
            return validerFormulaire_3_2();
        case "div_formulaire_4_1":
            return validerFormulaire_4_1();
        case "div_formulaire_5_1":
            return validerFormulaire_5_1();
        case "div_formulaire_5_2":
            return validerFormulaire_5_2();
        case "div_formulaire_6_1":
            return true; // Rien à valider ici pour l'instant
        case "div_formulaire_7_1":
            return validerFormulaire_7_1();
    }
}

/********************************************************************************************************
 * fonctions de validation par section
 ********************************************************************************************************/

function validerFormulaire_1_1() {
    miseAZeroErreur(document.getElementsByClassName("erreur_1_1"));
    document.getElementById("div_erreur_1_1").style.display = "none";
    var valide = true;

    // champs nom
    if (estChaineVide("ident_nom")) {
        valide = false;
        activerErreur("erreur_nom");
    }

    // champs prénom
    if (estChaineVide("ident_prenom")) {
        valide = false;
        activerErreur("erreur_prenom");
    }

    // code UQAM
    if (!estChaineVide("ident_code_uqam") && !testerRegex("ident_code_uqam", REGEX_STUDENT_CODE)) {
        valide = false;
        activerErreur("erreur_code_uqam");
    }

    // code permanent
    if (estChaineVide("ident_code") || !testerRegex("ident_code", REGEX_STUDENT_CODE)) {
        valide = false;
        activerErreur("erreur_code");
    }

    // ville naissance
    if (estChaineVide("ident_ville_naissance")) {
        valide = false;
        activerErreur("erreur_ville_naissance");
    }

    // citoyenneté
    var x = $("input[type='radio'][name='ident_citoyennete']:checked").val();
    if ( (x !== "autre" && x !== "canadienne") || (x === "autre" && estChaineVide("ident_citoyennete_texte")) ) {
        valide = false;
        document.getElementById("erreur_citoyennete").style.display = "inline";
    }

    if (!valide) {
        document.getElementById("div_erreur_1_1").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_1_2() {
    miseAZeroErreur(document.getElementsByClassName("erreur_1_2"));
    document.getElementById("div_erreur_1_2").style.display = "none";
    var valide = true;

    // nom et prénom père
    if (unSurDeuxVide("ident_nom_pere", "ident_prenom_pere")) {
        valide = false;
        activerErreur("erreur_nom_pere");
    }

    // nom et prénom mère
    if (unSurDeuxVide("ident_nom_mere", "ident_prenom_mere")) {
        valide = false;
        activerErreur("erreur_nom_mere");
    }

    if (!valide) {
        document.getElementById("div_erreur_1_2").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_1_3() {
    miseAZeroErreur(document.getElementsByClassName("erreur_1_3"));
    document.getElementById("div_erreur_1_3").style.display = "none";
    var valide = true;

    var telephone = false;
    // téléphone domicile
    if (unSurDeuxVide("ident_telephone_dom_1", "ident_telephone_dom_2")) {
        valide = false;
        activerErreur("erreur_telephone_dom");
    } else if (estDependantRempli("ident_telephone_dom_1", "ident_telephone_dom_2") &&
        (!testerRegex("ident_telephone_dom_1", REGEX_PHONE_AREA) || !testerRegex("ident_telephone_dom_2", REGEX_PHONE))) {
        valide = false;
        activerErreur("erreur_telephone_dom");
    }

    if (!estChaineVide("ident_telephone_dom_1")) {
        telephone = true;
    }

    // téléphone travail
    if (unSurDeuxVide("ident_telephone_tra_1", "ident_telephone_tra_2")) {
        valide = false;
        activerErreur("erreur_telephone_tra");
    } else if (estDependantRempli("ident_telephone_tra_1", "ident_telephone_tra_2") &&
            (!testerRegex("ident_telephone_tra_1", REGEX_PHONE_AREA) || !testerRegex("ident_telephone_tra_2", REGEX_PHONE))) {
        valide = false;
        activerErreur("erreur_telephone_tra");
    }

    if (!estChaineVide("ident_telephone_tra_1")) {
        telephone = true;
    }

    // téléphone cellulaire
    if (unSurDeuxVide("ident_telephone_cel_1", "ident_telephone_cel_2")) {
        valide = false;
        activerErreur("erreur_telephone_cel");
    } else if (estDependantRempli("ident_telephone_cel_1", "ident_telephone_cel_2") &&
            (!testerRegex("ident_telephone_cel_1", REGEX_PHONE_AREA) || !testerRegex("ident_telephone_cel_2", REGEX_PHONE))) {
        valide = false;
        activerErreur("erreur_telephone_cel");
    }

    if (!estChaineVide("ident_telephone_cel_1")) {
        telephone = true;
    }

    // téléphone parents
    if (unSurDeuxVide("ident_telephone_parents_1", "ident_telephone_parents_2")) {
        valide = false;
        activerErreur("erreur_telephone_parents");
    } else if (estDependantRempli("ident_telephone_parents_1", "ident_telephone_parents_2") &&
            (!testerRegex("ident_telephone_parents_1", REGEX_PHONE_AREA) || !testerRegex("ident_telephone_parents_2", REGEX_PHONE))) {
        valide = false;
        activerErreur("erreur_telephone_parents");
    }

    // adresse courriel
    if (!estChaineVide("ident_courriel") && !testerRegex("ident_courriel", REGEX_EMAIL)) {
        valide = false;
        activerErreur("erreur_courriel");
    }

    if (!telephone) {
        valide = false;
        activerErreur("erreur_telephone");
    }
    if (!valide) {
        document.getElementById("div_erreur_1_3").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_1_4() {
    miseAZeroErreur(document.getElementsByClassName("erreur_1_4"));
    document.getElementById("div_erreur_1_4").style.display = "none";
    var valide = true;

    // numéro civique
    if (estChaineVide("ident_num_civique") || !testerRegex("ident_num_civique", REGEX_CHIFFRE)) {
        valide = false;
        activerErreur("erreur_num_civique");
    }

    // nom de la rue
    if (estChaineVide("ident_rue")) {
        valide = false;
        activerErreur("erreur_rue");
    }

    // nom de ville
    if (estChaineVide("ident_municipalite")) {
        valide = false;
        activerErreur("erreur_municipalite");
    }

    // code postale
    if (!testerRegex("ident_code_postal", REGEX_POSTAL_CODE)) {
        valide = false;
        activerErreur("erreur_code_postal");
    }

    if (document.getElementById("ident_check_adresse_res").checked) {
        // numéro civique 2
        if (estChaineVide("ident_num_civique_2")) {
            valide = false;
            activerErreur("erreur_num_civique_2");
        }

        // nom de la rue 2
        if (estChaineVide("ident_rue_2")) {
            valide = false;
            activerErreur("erreur_rue_2");
        }

        // nom de ville 2
        if (estChaineVide("ident_municipalite_2")) {
            valide = false;
            activerErreur("erreur_municipalite_2");
        }

        // code postale 2
        if (!testerRegex("ident_code_postal_2", REGEX_POSTAL_CODE)) {
            valide = false;
            activerErreur("erreur_code_postal_2");
        }
    }

    if (!valide) {
        document.getElementById("div_erreur_1_4").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_1_5() {
    miseAZeroErreur(document.getElementsByClassName("erreur_1_5"));
    document.getElementById("div_erreur_1_5").style.display = "none";
    var valide = true;

    // date de naissance
    if (estChaineVide("ident_date_naissance") || !testerRegex("ident_date_naissance", REGEX_DATE) ||
            !validerDateInferieure("ident_date_naissance")) {
        valide = false;
        activerErreur("erreur_date_naissance");
    }

    // champs sexe
    if (document.getElementById("ident_sexe").value === "") {
        valide = false;
        activerErreur("erreur_sexe");
    }

    // numéro d'assurance social
    if (!estChaineVide("ident_assurance_so") && !testerRegex("ident_assurance_so", REGEX_ASSURANCE_SO)) {
        valide = false;
        activerErreur("erreur_assurance_so");
    }

    // status
    if (document.getElementById("ident_statut").value === "") {
        valide = false;
        activerErreur("erreur_statut");
    }

    // langue usage
    if (document.getElementById("ident_langue_usage").value === "") {
        valide = false;
        activerErreur("erreur_langue_usage");
    } else if (document.getElementById("ident_langue_usage").value === "autre" && estChaineVide("ident_langue_usage_autre")) {
        valide = false;
        activerErreur("erreur_langue_usage_autre");
    }

    // langue maternelle
    if (document.getElementById("ident_langue_mater").value === "") {
        valide = false;
        activerErreur("erreur_langue_mater");
    } else if (document.getElementById("ident_langue_mater").value === "autre" && estChaineVide("ident_langue_mater_autre")) {
        valide = false;
        activerErreur("erreur_langue_mater_autre");
    }

    if (!valide) {
        document.getElementById("div_erreur_1_5").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_2_1() {
    miseAZeroErreur(document.getElementsByClassName("erreur_2_1"));
    document.getElementById("div_erreur_2_1").style.display = "none";
    var valide = true;

    // saison trimestre
    if (document.getElementById("progdemande_trimestre").value === "") {
        valide = false;
        activerErreur("erreur_progdemande_trimestre");
    }

    // année trimestre
    if (document.getElementById("progdemande_trimestre_annee").value === "") {
        valide = false;
        activerErreur("erreur_progdemande_trimestre_annee");
    }

    // choix 1 titre
    if (estChaineVide("progdemande_choix_1_titre")) {
        valide = false;
        activerErreur("erreur_progdemande_choix_1_titre");
    }

    // choix 1 type
    if (document.getElementById("progdemande_choix_1_type").value === "") {
        valide = false;
        activerErreur("erreur_progdemande_choix_1_type");
    }

    // choix 1 temps
    if (document.getElementById("progdemande_choix_1_temps").value === "") {
        valide = false;
        activerErreur("erreur_progdemande_choix_1_temps");
    }

    // choix 1 code
    if (estChaineVide("progdemande_choix_1_code")) {
        valide = false;
        activerErreur("erreur_progdemande_choix_1_code");
    }

    if (!estChaineVide("progdemande_choix_2_titre") || !estChaineVide("progdemande_choix_2_code") ||
            document.getElementById("progdemande_choix_2_type").value !== "" || document.getElementById("progdemande_choix_2_temps").value !== "") {
        // choix 2 titre
        if (estChaineVide("progdemande_choix_2_titre")) {
            valide = false;
            activerErreur("erreur_progdemande_choix_2_titre");
        }

        // choix 2 type
        if (document.getElementById("progdemande_choix_2_type").value === "") {
            valide = false;
            activerErreur("erreur_progdemande_choix_2_type");
        }

        // choix 2 temps
        if (document.getElementById("progdemande_choix_2_temps").value === "") {
            valide = false;
            activerErreur("erreur_progdemande_choix_2_temps");
        }

        // choix 2 code
        if (estChaineVide("progdemande_choix_2_code")) {
            valide = false;
            activerErreur("erreur_progdemande_choix_2_code");
        }
    }

    if (!estChaineVide("progdemande_choix_3_titre") || !estChaineVide("progdemande_choix_3_code") ||
            document.getElementById("progdemande_choix_3_type").value !== "" || document.getElementById("progdemande_choix_3_temps").value !== "") {
        // choix 2 titre
        if (estChaineVide("progdemande_choix_3_titre")) {
            valide = false;
            activerErreur("erreur_progdemande_choix_3_titre");
        }

        // choix 2 type
        if (document.getElementById("progdemande_choix_3_type").value === "") {
            valide = false;
            activerErreur("erreur_progdemande_choix_3_type");
        }

        // choix 2 temps
        if (document.getElementById("progdemande_choix_3_temps").value === "") {
            valide = false;
            activerErreur("erreur_progdemande_choix_3_temps");
        }

        // choix 2 code
        if (estChaineVide("progdemande_choix_3_code")) {
            valide = false;
            activerErreur("erreur_progdemande_choix_3_code");
        }
    }

    if (document.getElementById("progdemande_presence").value === "") {
        valide = false;
        activerErreur("erreur_progdemande_presence");
    } else if (document.getElementById("progdemande_presence").value === "non" && estChaineVide("progdemande_presence_autre")) {
        valide = false;
        activerErreur("erreur_progdemande_presence_autre");
    }

    if (!valide) {
        document.getElementById("div_erreur_2_1").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_3_1() {
    miseAZeroErreur(document.getElementsByClassName("erreur_3_1"));
    document.getElementById("div_erreur_3_1").style.display = "none";
    var valide = true;

    // si étude secondaire
    if (document.getElementById("secondcollege_check_etude").checked) {

        // année complétée
        if (estChaineVide("secondcollege_derniere_annee_sec")) {
            valide = false;
            activerErreur("erreur_secondcollege_derniere_annee_sec");
        }

        // fréquentation début et fin
        if (isChiffre("secondcollege_annee_debut_1") && isChiffre("secondcollege_annee_fin_1")) {
            if (!retourneDateInferieure("secondcollege_annee_debut_1", "secondcollege_annee_fin_1")) {
                valide = false;
                activerErreur("erreur_secondcollege_annee_logic_1");
            }
        } else {
            valide = false;
            activerErreur("erreur_secondcollege_annee_1");
        }

        // discipline
        if (estChaineVide("secondcollege_discipline_1")) {
            valide = false;
            activerErreur("erreur_secondcollege_discipline");
        }

        // fréquentation discipline
        if (isChiffre("secondcollege_annee_debut_2") && isChiffre("secondcollege_annee_fin_2")) {
            if (!retourneDateInferieure("secondcollege_annee_debut_2", "secondcollege_annee_fin_2")) {
                valide = false;
                activerErreur("erreur_secondcollege_annee_logic_2");
            }
        } else {
            valide = false;
            activerErreur("erreur_secondcollege_annee_2");
        }

        // établissement
        if (estChaineVide("secondcollege_institution_1")) {
            valide = false;
            activerErreur("erreur_secondcollege_institution");
        }

        // date d'obtention mois
        if (!isChiffre("secondcollege_obtention_mois_1")) {
            valide = false;
            activerErreur("erreur_secondcollege_obtention_mois");
        }

        // date d'obtention année
        if (!isChiffre("secondcollege_obtention_annee_1")) {
            valide = false;
            activerErreur("erreur_secondcollege_obtention_annee");
        }
    }

    if (!valide) {
        document.getElementById("div_erreur_3_1").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_3_2() {
    miseAZeroErreur(document.getElementsByClassName("erreur_3_2"));
    document.getElementById("div_erreur_3_2").style.display = "none";
    var valide = true;

    if($("input[type='radio'][name='secondcollege_dec_aec']:checked").val() !== "") {

        // nom du diplôme
        if (estChaineVide("secondcollege_nom_diplome_dec_aec")) {
            valide = false;
            activerErreur("erreur_secondcollege_nom_diplome_dec_aec");
        }

        // radio obtention
        var radio = $("input[type='radio'][name='secondcollege_dec_obtention']:checked").val();
        if(radio === "obtenu") {
            // date d'obtention
            if (!isChiffre("secondcollege_obtention_mois_2") || !isChiffre("secondcollege_obtention_annee_2")) {
                valide = false;
                activerErreur("erreur_secondcollege_obtention");
            }
        } else if (radio !== "a_obtenir" && radio !== "pas_termine") {
            valide = false;
            activerErreur("erreur_secondcollege_radio_dec_aec");
        }

        // institution
        if (estChaineVide("secondcollege_institution_dec_aec")) {
            valide = false;
            activerErreur("erreur_secondcollege_institution_dec_aec");
        }

        // discipline
        if (estChaineVide("secondcollege_discipline_dec_aec")) {
            valide = false;
            activerErreur("erreur_secondcollege_discipline_dec_aec");
        }

        // période de fréquentation
        if (isChiffre("secondcollege_annee_debut_3") && isChiffre("secondcollege_annee_fin_3")) {
            if (!retourneDateInferieure("secondcollege_annee_debut_3", "secondcollege_annee_fin_3")) {
                valide = false;
                activerErreur("erreur_secondcollege_annee_logic_3");
            }
        } else {
            valide = false;
            activerErreur("erreur_secondcollege_annee_3");
        }
    }

    if (!valide) {
        document.getElementById("div_erreur_3_2").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_4_1() {
    miseAZeroErreur(document.getElementsByClassName("erreur_4_1"));
    document.getElementById("div_erreur_4_1").style.display = "none";
    var valide = true;

    // section université
    if (document.getElementById("universitaires_check_universite").checked) {

        // nom du diplôme uni 1
        if (estChaineVide("universitaires_nom_diplome")) {
            valide = false;
            activerErreur("erreur_uni_diplome_1");
        }

        // radio obtention uni 1
        var radio_1 = $("input[type='radio'][name='universitaires_obtention']:checked").val();
        if(radio_1 === "obtenu") {
            // date d'obtention
            if (!isChiffre("universitaires_obtention_mois") || !isChiffre("universitaires_obtention_annee")) {
                valide = false;
                activerErreur("erreur_uni_obtention_1");
            }
        } else if (radio_1 !== "a_obtenir" && radio_1 !== "pas_termine") {
            valide = false;
            activerErreur("erreur_uni_radio_1");
        }

        // institution uni 1
        if (estChaineVide("universitaires_institution")) {
            valide = false;
            activerErreur("erreur_uni_institution_1");
        }

        // discipline uni 1
        if (estChaineVide("universitaires_discipline")) {
            valide = false;
            activerErreur("erreur_uni_discipline_1");
        }

        // période de fréquentation uni 1
        if (isChiffre("universitaires_annee_debut") && isChiffre("universitaires_annee_fin")) {
            if (!retourneDateInferieure("universitaires_annee_debut", "universitaires_annee_fin")) {
                valide = false;
                activerErreur("erreur_uni_annee_logic_1");
            }
        } else {
            valide = false;
            activerErreur("erreur_uni_annee_1");
        }

        // section université autre
        if (document.getElementById("universitaires_check_autre").checked) {

            // nom du diplôme uni 1
            if (estChaineVide("universitaires_nom_diplome_autre")) {
                valide = false;
                activerErreur("erreur_uni_diplome_2");
            }

            // radio obtention uni 1
            var radio_2 = $("input[type='radio'][name='universitaires_obtention_autre']:checked").val();
            if (radio_2 === "obtenu") {
                // date d'obtention
                if (!isChiffre("universitaires_obtention_mois_autre") || !isChiffre("universitaires_obtention_annee_autre")) {
                    valide = false;
                    activerErreur("erreur_uni_obtention_2");
                }
            } else if (radio_2 !== "a_obtenir" && radio_2 !== "pas_termine") {
                valide = false;
                activerErreur("erreur_uni_radio_2");
            }

            // institution uni 1
            if (estChaineVide("universitaires_institution_autre")) {
                valide = false;
                activerErreur("erreur_uni_institution_2");
            }

            // discipline uni 1
            if (estChaineVide("universitaires_discipline_autre")) {
                valide = false;
                activerErreur("erreur_uni_discipline_2");
            }

            // période de fréquentation uni 1
            if (isChiffre("universitaires_annee_debut_autre") && isChiffre("universitaires_annee_fin_autre")) {
                if (!retourneDateInferieure("universitaires_annee_debut_autre", "universitaires_annee_fin_autre")) {
                    valide = false;
                    activerErreur("erreur_uni_annee_logic_2");
                }
            } else {
                valide = false;
                activerErreur("erreur_uni_annee_2");
            }
        }
    }

    if (!valide) {
        document.getElementById("div_erreur_4_1").style.display = "inline";
    }
    return valide;
}

function validerFormulaire_5_1() {
    miseAZeroErreur(document.getElementsByClassName("erreur_5_1"));
    document.getElementById("div_erreur_5_1").style.display = "none";
    var valide = true;
    
    // Emploi 1
    if (document.getElementById("emploi_check_emploi_1").checked) {
        if (estChaineVide("emploi_nom_employeur_1")) {
            valide = false;
            activerErreur("erreur_emploi_nom_employeur_1");
        }
        
        if (estChaineVide("emploi_duree_de_mois_1")) {
            valide = false;
            activerErreur("erreur_emploi_duree_de_mois_1");
        }
        
        if (estChaineVide("emploi_duree_de_annee_1")) {
            valide = false;
            activerErreur("erreur_emploi_duree_de_annee_1");
        }
        
        if (estChaineVide("emploi_type_emploi_1")) {
            valide = false;
            activerErreur("erreur_emploi_type_emploi_1");
        }
        
        if (estChaineVide("emploi_duree_a_mois_1")) {
            valide = false;
            activerErreur("erreur_emploi_duree_a_mois_1");
        }
        
        if (estChaineVide("emploi_duree_a_annee_1")) {
            valide = false;
            activerErreur("erreur_emploi_duree_a_annee_1");
        }
        
        if (estChaineVide("emploi_date_attestation_1") 
                || !testerRegex("emploi_date_attestation_1", REGEX_DATE)) {
            valide = false;
            activerErreur("erreur_emploi_date_attestation_1");
        }

        // durée emploi logique
        if(!estChaineVide("emploi_duree_de_mois_1") && !estChaineVide("emploi_duree_de_annee_1") &&
            !estChaineVide("emploi_duree_a_mois_1") && !estChaineVide("emploi_duree_a_annee_1")) {

            if(isChiffre("emploi_duree_de_annee_1") > isChiffre("emploi_duree_a_annee_1")) {
                valide = false;
                activerErreur("erreur_emploi_duree_logic_1");
            } else if (isChiffre("emploi_duree_de_mois_1") > isChiffre("emploi_duree_a_mois_1") &&
                isChiffre("emploi_duree_de_annee_1") === isChiffre("emploi_duree_a_annee_1")) {
                valide = false;
                activerErreur("erreur_emploi_duree_logic_1");
            }
        }
    }
    
    if (!valide) {
        document.getElementById("div_erreur_5_1").style.display = "inline";
    }
    
    return valide;
}

function validerFormulaire_5_2() {
    miseAZeroErreur(document.getElementsByClassName("erreur_5_2"));
    document.getElementById("div_erreur_5_2").style.display = "none";
    var valide = true;
    
    // Emploi 2
    if (document.getElementById("emploi_check_emploi_2").checked) {
        if (estChaineVide("emploi_nom_employeur_2")) {
            valide = false;
            activerErreur("erreur_emploi_nom_employeur_2");
        }
        
        if (estChaineVide("emploi_duree_de_mois_2")) {
            valide = false;
            activerErreur("erreur_emploi_duree_de_mois_2");
        }
        
        if (estChaineVide("emploi_duree_de_annee_2")) {
            valide = false;
            activerErreur("erreur_emploi_duree_de_annee_2");
        }
        
        if (estChaineVide("emploi_type_emploi_2")) {
            valide = false;
            activerErreur("erreur_emploi_type_emploi_2");
        }
        
        if (estChaineVide("emploi_duree_a_mois_2")) {
            valide = false;
            activerErreur("erreur_emploi_duree_a_mois_2");
        }
        
        if (estChaineVide("emploi_duree_a_annee_2")) {
            valide = false;
            activerErreur("erreur_emploi_duree_a_annee_2");
        }
        
        if (estChaineVide("emploi_date_attestation_2") 
                || !testerRegex("emploi_date_attestation_2", REGEX_DATE)) {
            valide = false;
            activerErreur("erreur_emploi_date_attestation_2");
        }

        // durée emploi logique
        if(!estChaineVide("emploi_duree_de_mois_2") && !estChaineVide("emploi_duree_de_annee_2") &&
            !estChaineVide("emploi_duree_a_mois_2") && !estChaineVide("emploi_duree_a_annee_2")) {

            if(isChiffre("emploi_duree_de_annee_2") > isChiffre("emploi_duree_a_annee_2")) {
                valide = false;
                activerErreur("erreur_emploi_duree_logic_2");
            } else if (isChiffre("emploi_duree_de_mois_2") > isChiffre("emploi_duree_a_mois_2") &&
                isChiffre("emploi_duree_de_annee_2") === isChiffre("emploi_duree_a_annee_2")) {
                valide = false;
                activerErreur("erreur_emploi_duree_logic_2");
            }
        }
    }
    
    // Emploi 3
    if (document.getElementById("emploi_check_emploi_3").checked) {
        if (estChaineVide("emploi_nom_employeur_3")) {
            valide = false;
            activerErreur("erreur_emploi_nom_employeur_3");
        }
        
        if (estChaineVide("emploi_duree_de_mois_3")) {
            valide = false;
            activerErreur("erreur_emploi_duree_de_mois_3");
        }
        
        if (estChaineVide("emploi_duree_de_annee_3")) {
            valide = false;
            activerErreur("erreur_emploi_duree_de_annee_3");
        }
        
        if (estChaineVide("emploi_type_emploi_3")) {
            valide = false;
            activerErreur("erreur_emploi_type_emploi_3");
        }
        
        if (estChaineVide("emploi_duree_a_mois_3")) {
            valide = false;
            activerErreur("erreur_emploi_duree_a_mois_3");
        }
        
        if (estChaineVide("emploi_duree_a_annee_3")) {
            valide = false;
            activerErreur("erreur_emploi_duree_a_annee_3");
        }
        
        if (estChaineVide("emploi_date_attestation_3") 
                || !testerRegex("emploi_date_attestation_3", REGEX_DATE)) {
            valide = false;
            activerErreur("erreur_emploi_date_attestation_3");
        }

        // durée emploi logique
        if(!estChaineVide("emploi_duree_de_mois_3") && !estChaineVide("emploi_duree_de_annee_3") &&
            !estChaineVide("emploi_duree_a_mois_3") && !estChaineVide("emploi_duree_a_annee_3")) {

            if(isChiffre("emploi_duree_de_annee_3") > isChiffre("emploi_duree_a_annee_3")) {
                valide = false;
                activerErreur("erreur_emploi_duree_logic_3");
            } else if (isChiffre("emploi_duree_de_mois_3") > isChiffre("emploi_duree_a_mois_3") &&
                isChiffre("emploi_duree_de_annee_3") === isChiffre("emploi_duree_a_annee_3")) {
                valide = false;
                activerErreur("erreur_emploi_duree_logic_3");
            }
        }
    }
    
    if (!valide) {
        document.getElementById("div_erreur_5_2").style.display = "inline";
    }
    
    return valide;
}



function validerFormulaire_7_1() {
    miseAZeroErreur(document.getElementsByClassName("erreur_7_1"));
    document.getElementById("div_erreur_7_1").style.display = "none";
    var valide = true;
    
    if (estChaineVide("supplement_accept_1")) {
            valide = false;
            activerErreur("erreur_supplement_accept_1");
    }
    
    if (estChaineVide("supplement_accept_2")) {
            valide = false;
            activerErreur("erreur_supplement_accept_2");
    }
    
    if (!valide) {
        document.getElementById("div_erreur_7_1").style.display = "inline";
    }
    
    return valide;
}


/********************************************************************************************************
 * petites fonctions pour diminuer le nombre de répétitions
 ********************************************************************************************************/

/* remet les erreurs de la pages et cache la zone des erreurs */
function miseAZeroErreur(listeIdErreur) {
    for (var i = 0; i < listeIdErreur.length; i++) {
        listeIdErreur[i].style.display = "none";
    }
}

/* retourne true quand la chaine est vide */
function estChaineVide(ident) {
    var chaine = document.getElementById(ident).value;
    chaine = chaine.trim();
    chaine = chaine.replace(/\s+/g, " ");
    return (chaine === null || chaine === "");
}

/* compare 2 champs et retourne true lorsque les 2 champs sont remplis */
function estDependantRempli(ident1, ident2) {
    var chaine1 = document.getElementById(ident1).value;
    chaine1 = chaine1.trim();
    chaine1 = chaine1.replace(/\s+/g, " ");
    var chaine2 = document.getElementById(ident2).value;
    chaine2 = chaine2.trim();
    chaine2 = chaine2.replace(/\s+/g, " ");

    return (chaine1 !== null && chaine1 !== "") && (chaine2 !== null && chaine2 !== "");
}

/* trim les entrées et retourne true lorsqu'un champs sur les deux est vide */
function unSurDeuxVide(ident1, ident2) {
    var chaine1 = document.getElementById(ident1).value;
    chaine1 = chaine1.trim();
    chaine1 = chaine1.replace(/\s+/g, " ");
    var chaine2 = document.getElementById(ident2).value;
    chaine2 = chaine2.trim();
    chaine2 = chaine2.replace(/\s+/g, " ");

    return (chaine1 !== null && chaine1 !== "") && (chaine2 === null || chaine2 === "") ||
            (chaine1 === null || chaine1 === "") && (chaine2 !== null && chaine2 !== "");
}

/* retourne true lorsque la date est inférieure à la date actuelle */
function validerDateInferieure(ident) {
    var chaineDate = document.getElementById(ident).value;
    var d = new Date(chaineDate.substring(0, 4), chaineDate.substring(5, 7) - 1, chaineDate.substring(8, 10));
    return d < new Date();
}

/* retourne true si la première date est inférieure à la deuxième date */
function retourneDateInferieure(ident1, ident2) {
    var chaineDate1 = document.getElementById(ident1).value;
    var chaineDate2 = document.getElementById(ident2).value;
    var d1 = new Date(chaineDate1.substring(0, 4), chaineDate1.substring(5, 7) - 1, chaineDate1.substring(8, 10));
    var d2 = new Date(chaineDate2.substring(0, 4), chaineDate2.substring(5, 7) - 1, chaineDate2.substring(8, 10));
    return d1 < d2;
}

/* active la division de l'erreur */
function activerErreur(ident) {
    document.getElementById(ident).style.display = "inline";
}

/* trim l'entrée et retourne true lorsque le champs respecte le regex */
function testerRegex(ident, regex) {
    var chaine = document.getElementById(ident).value;
    chaine = chaine.trim();
    chaine = chaine.replace(/\s+/g, " ");
    return regex.test(chaine);
}

/* Retourne vrai si est un chiffre */
function isChiffre(ident) {
    return parseInt(document.getElementById(ident).value);
}
