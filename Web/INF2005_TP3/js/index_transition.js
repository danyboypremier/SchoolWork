/********************************************************************************************************
 * Fonctions javascript pour l'utilisation du site
 ********************************************************************************************************/
$(document).ready(function () {

    var formulaire = document.getElementsByClassName("div_formulaire");
    var menuNavigable = document.getElementsByClassName("liens_nav");
    var titreMenuNavigable = document.getElementsByClassName("slide_menu_nav");
    var sectionMenuNavigable = document.getElementsByClassName("section_menu_nav");
    var delaisFadeOutIn = 400;
    var delaisBoutons = 1000;

/********************************************************************************************************
 * Gestion des boutons
 ********************************************************************************************************/
    $("#suivant").click(function () {
        // Pourquoi lorsque je mets var la variable n'entre pas dans le for loop
        etatSoumettre = document.getElementById("soumettre").disabled;
        etatSuivant = document.getElementById("suivant").disabled;
        etatPrecedent = document.getElementById("precedent").disabled;
        desactiverBoutons();

        for (var i = 0; i < formulaire.length; i++) {
            if (formulaire[i].style.display !== "none") {
                if (appelerValidation(formulaire[i])) {
                    $(formulaire[i]).fadeOut();
                    $(formulaire[i + 1]).delay(delaisFadeOutIn).fadeIn();
                    activerMenu(i + 1);
                    if (i + 1 !== 0) {
                        setTimeout("document.getElementById(\"precedent\").disabled = false;", delaisBoutons);
                    } else {
                        document.getElementById("precedent").disabled = true;
                    }
                    if (i + 1 === formulaire.length - 1) {
                        document.getElementById("suivant").disabled = true;
                        etatSoumettre = false;
                    } else {
                        setTimeout("document.getElementById(\"suivant\").disabled = false;", delaisBoutons);
                    }
                } else {
                    setTimeout("document.getElementById(\"suivant\").disabled = etatSuivant;", delaisBoutons);
                    setTimeout("document.getElementById(\"precedent\").disabled = etatPrecedent;", delaisBoutons);
                }
                setTimeout("document.getElementById(\"soumettre\").disabled = etatSoumettre;", delaisBoutons);
                break;
            }
        }
    });

    $("#precedent").click(function () {
        etatSoumettre = document.getElementById("soumettre").disabled;
        etatSuivant = document.getElementById("suivant").disabled;
        etatPrecedent = document.getElementById("precedent").disabled;
        desactiverBoutons();

        for (var i = 0; i < formulaire.length; i++) {
            if (formulaire[i].style.display !== "none") {
                if (appelerValidation(formulaire[i])) {
                    $(formulaire[i]).fadeOut();
                    $(formulaire[i - 1]).delay(delaisFadeOutIn).fadeIn();
                    if (i - 1 === 0) {
                        document.getElementById("precedent").disabled = true;
                    } else {
                        setTimeout("document.getElementById(\"precedent\").disabled = false;", delaisBoutons);
                    }
                    setTimeout("document.getElementById(\"suivant\").disabled = false;", delaisBoutons);
                    setTimeout("document.getElementById(\"soumettre\").disabled = etatSoumettre;", delaisBoutons);
                    break;
                } else {
                    setTimeout("document.getElementById(\"suivant\").disabled = etatSuivant;", delaisBoutons);
                    setTimeout("document.getElementById(\"precedent\").disabled = etatPrecedent;", delaisBoutons);
                    setTimeout("document.getElementById(\"soumettre\").disabled = etatSoumettre;", delaisBoutons);
                    break;
                }
            }
        }
    });

/********************************************************************************************************
 * Gestion des transitions de la zone du formulaire
 ********************************************************************************************************/
    $("#ident_check_adresse_res").click(function () {
        if (document.getElementById("ident_check_adresse_res").checked) {
            $(".adresse_res").fadeIn();
        } else {
            $(".adresse_res").fadeOut();
            document.getElementById("ident_num_civique_2").value = "";
            document.getElementById("ident_rue_2").value = "";
            document.getElementById("ident_direction_2").value = "";
            document.getElementById("ident_appartement_2").value = "";
            document.getElementById("ident_municipalite_2").value = "";
            document.getElementById("ident_pays_2").value = "";
            document.getElementById("ident_code_postal_2").value = "";
        }
    });

    $("#secondcollege_check_etude").click(function () {
        if (document.getElementById("secondcollege_check_etude").checked) {
            $(".etude_secondaire").fadeIn();
        } else {
            $(".etude_secondaire").fadeOut();
            document.getElementById("secondcollege_derniere_annee_sec").value = "";
            document.getElementById("secondcollege_annee_debut_1").value = "";
            document.getElementById("secondcollege_annee_fin_1").value = "";
            document.getElementById("secondcollege_check_etude_sec_exterieur").checked = false;
            document.getElementById("secondcollege_institution_1").value = "";
            document.getElementById("secondcollege_annee_debut_2").value = "";
            document.getElementById("secondcollege_annee_fin_2").value = "";
            document.getElementById("secondcollege_discipline_1").value = "";
            document.getElementById("secondcollege_obtention_mois_1").value = "";
            document.getElementById("secondcollege_obtention_annee_1").value = "";
        }
    });

    $("input[name=ident_citoyennete]:radio").change(function () {
        if (document.getElementById("ident_citoyennete_autre").checked) {
            document.getElementById("ident_citoyennete_texte").disabled = false;
        } else {
            document.getElementById("ident_citoyennete_texte").disabled = true;
            document.getElementById("ident_citoyennete_texte").value = "";
        }
    });

    $("#ident_langue_usage").change(function () {
        if (document.getElementById("ident_langue_usage").value === "autre") {
            document.getElementById("ident_langue_usage_autre").disabled = false;
        } else {
            document.getElementById("ident_langue_usage_autre").disabled = true;
            document.getElementById("ident_langue_usage_autre").value = "";
        }
    });

    $("#ident_langue_mater").change(function () {
        if (document.getElementById("ident_langue_mater").value === "autre") {
            document.getElementById("ident_langue_mater_autre").disabled = false;
        } else {
            document.getElementById("ident_langue_mater_autre").disabled = true;
            document.getElementById("ident_langue_mater_autre").value = "";
        }
    });

    $("#progdemande_trimestre").change(function () {
        if (document.getElementById("progdemande_trimestre").value === "") {
            document.getElementById("progdemande_trimestre_annee").disabled = true;
            document.getElementById("progdemande_trimestre_annee").value = "";
        } else {
            document.getElementById("progdemande_trimestre_annee").disabled = false;
        }
    });

    $("#progdemande_presence").change(function () {
        if (document.getElementById("progdemande_presence").value === "non") {
            document.getElementById("progdemande_presence_autre").disabled = false;
        } else {
            document.getElementById("progdemande_presence_autre").disabled = true;
            document.getElementById("progdemande_presence_autre").value = "";
        }
    });

    $("input[name=secondcollege_dec_aec]:radio").change(function () {
        if (document.getElementById("secondcollege_radio_aucun").checked) {
            document.getElementById("secondcollege_nom_diplome_dec_aec").value = "";
            $('input:radio[name="secondcollege_dec_obtention"]').removeAttr('checked');
            document.getElementById("secondcollege_institution_dec_aec").value = "";
            document.getElementById("secondcollege_annee_debut_3").value = "";
            document.getElementById("secondcollege_annee_fin_3").value = "";
            document.getElementById("secondcollege_discipline_dec_aec").value = "";
            document.getElementById("secondcollege_obtention_mois_2").value = "";
            document.getElementById("secondcollege_obtention_annee_2").value = "";
            $("#etude_collegiale").fadeOut();
        } else {
            $("#etude_collegiale").fadeIn();
        }
    });
    
    $("input[name=secondcollege_dec_obtention]:radio").change(function() {
        if (document.getElementById("secondcollege_radio_dec_obtention").checked) {
            $('select[name="secondcollege_obtention_mois_2"]').prop('disabled', false);
            $('select[name="secondcollege_obtention_annee_2"]').prop('disabled', false);
        } else {
            document.getElementById("secondcollege_obtention_mois_2").value = "";
            document.getElementById("secondcollege_obtention_annee_2").value = "";
            $('select[name="secondcollege_obtention_mois_2"]').prop('disabled', true);
            $('select[name="secondcollege_obtention_annee_2"]').prop('disabled', true);
        }
    });

    $("#universitaires_check_universite").change(function () {
        if (document.getElementById("universitaires_check_universite").checked) {
            $(".grade_universitaire").fadeIn();
        } else {
            if (document.getElementById("universitaires_check_autre").checked) {
                $("#grade_universitaire_autre").fadeOut().delay(delaisFadeOutIn);
                document.getElementById("universitaires_check_autre").checked = false;
                document.getElementById("universitaires_nom_diplome_autre").value = "";
                $('input:radio[name="universitaires_obtention_autre"]').removeAttr('checked');
                document.getElementById("universitaires_institution_autre").value = "";
                document.getElementById("universitaires_annee_debut_autre").value = "";
                document.getElementById("universitaires_annee_fin_autre").value = "";
                document.getElementById("universitaires_discipline_autre").value = "";
                document.getElementById("universitaires_obtention_mois_autre").value = "";
                document.getElementById("universitaires_obtention_annee_autre").value = "";
                $('select[name="universitaires_obtention_mois_autre"]').prop('disabled', true);
                $('select[name="universitaires_obtention_annee_autre"]').prop('disabled', true);
            }
            $(".grade_universitaire").fadeOut();
            document.getElementById("universitaires_check_universite").checked = false;
            document.getElementById("universitaires_nom_diplome").value = "";
            $('input:radio[name="universitaires_obtention"]').removeAttr('checked');
            document.getElementById("universitaires_institution").value = "";
            document.getElementById("universitaires_annee_debut").value = "";
            document.getElementById("universitaires_annee_fin").value = "";
            document.getElementById("universitaires_discipline").value = "";
            document.getElementById("universitaires_obtention_mois").value = "";
            document.getElementById("universitaires_obtention_annee").value = "";
            $('select[name="universitaires_obtention_mois"]').prop('disabled', true);
            $('select[name="universitaires_obtention_annee"]').prop('disabled', true);
        }
    });
    
    $("input[name=universitaires_obtention]:radio").change(function() {
        if (document.getElementById("universitaires_radio_obtention").checked) {
            $('select[name="universitaires_obtention_mois"]').prop('disabled', false);
            $('select[name="universitaires_obtention_annee"]').prop('disabled', false);
        } else {
            document.getElementById("universitaires_obtention_mois").value = "";
            document.getElementById("universitaires_obtention_annee").value = "";
            $('select[name="universitaires_obtention_mois"]').prop('disabled', true);
            $('select[name="universitaires_obtention_annee"]').prop('disabled', true);
        }
    });

    $("#universitaires_check_autre").change(function () {
        if (document.getElementById("universitaires_check_autre").checked) {
            $("#grade_universitaire_autre").fadeIn();
        } else {
            $("#grade_universitaire_autre").fadeOut();
            document.getElementById("universitaires_nom_diplome_autre").value = "";
            $('input:radio[name="universitaires_obtention_autre"]').removeAttr('checked');
            document.getElementById("universitaires_institution_autre").value = "";
            document.getElementById("universitaires_annee_debut_autre").value = "";
            document.getElementById("universitaires_annee_fin_autre").value = "";
            document.getElementById("universitaires_discipline_autre").value = "";
            document.getElementById("universitaires_obtention_mois_autre").value = "";
            document.getElementById("universitaires_obtention_annee_autre").value = "";
            $('select[name="universitaires_obtention_mois_autre"]').prop('disabled', true);
            $('select[name="universitaires_obtention_annee_autre"]').prop('disabled', true);
        }
    });
    
    $("input[name=universitaires_obtention_autre]:radio").change(function() {
        if (document.getElementById("universitaires_radio_obtention_autre").checked) {
            $('select[name="universitaires_obtention_mois_autre"]').prop('disabled', false);
            $('select[name="universitaires_obtention_annee_autre"]').prop('disabled', false);
        } else {
            document.getElementById("universitaires_obtention_mois_autre").value = "";
            document.getElementById("universitaires_obtention_annee_autre").value = "";
            $('select[name="universitaires_obtention_mois_autre"]').prop('disabled', true);
            $('select[name="universitaires_obtention_annee_autre"]').prop('disabled', true);
        }
    });

    $("#emploi_check_emploi_1").change(function () {
        if (document.getElementById("emploi_check_emploi_1").checked) {
            $("#section_emploi_1").fadeIn();
        } else {
            $("#section_emploi_1").fadeOut();
            document.getElementById("emploi_nom_employeur_1").value = "";
            document.getElementById("emploi_duree_de_mois_1").value = "";
            document.getElementById("emploi_duree_de_annee_1").value = "";
            document.getElementById("emploi_type_emploi_1").value = "";
            document.getElementById("emploi_duree_a_mois_1").value = "";
            document.getElementById("emploi_duree_a_annee_1").value = "";
            document.getElementById("emploi_date_attestation_1").value = "";
        }
    });

    $("#emploi_check_emploi_2").change(function () {
        if (document.getElementById("emploi_check_emploi_2").checked) {
            $("#section_emploi_2, #section_emploi_2_1").fadeIn();
        } else {
            if (document.getElementById("emploi_check_emploi_3").checked) {
                $("#section_emploi_3").fadeOut().delay(delaisFadeOutIn);
                document.getElementById("emploi_check_emploi_3").checked = false;
                document.getElementById("emploi_nom_employeur_3").value = "";
                document.getElementById("emploi_duree_de_mois_3").value = "";
                document.getElementById("emploi_duree_de_annee_3").value = "";
                document.getElementById("emploi_type_emploi_3").value = "";
                document.getElementById("emploi_duree_a_mois_3").value = "";
                document.getElementById("emploi_duree_a_annee_3").value = "";
                document.getElementById("emploi_date_attestation_3").value = "";
            }
            $("#section_emploi_2, #section_emploi_2_1").fadeOut();
            document.getElementById("emploi_nom_employeur_2").value = "";
            document.getElementById("emploi_duree_de_mois_2").value = "";
            document.getElementById("emploi_duree_de_annee_2").value = "";
            document.getElementById("emploi_type_emploi_2").value = "";
            document.getElementById("emploi_duree_a_mois_2").value = "";
            document.getElementById("emploi_duree_a_annee_2").value = "";
            document.getElementById("emploi_date_attestation_2").value = "";
        }
    });

    $("#emploi_check_emploi_3").change(function () {
        if (document.getElementById("emploi_check_emploi_3").checked) {
            $("#section_emploi_3").fadeIn();
        } else {
            $("#section_emploi_3").fadeOut();
            document.getElementById("emploi_nom_employeur_3").value = "";
            document.getElementById("emploi_duree_de_mois_3").value = "";
            document.getElementById("emploi_duree_de_annee_3").value = "";
            document.getElementById("emploi_type_emploi_3").value = "";
            document.getElementById("emploi_duree_a_mois_3").value = "";
            document.getElementById("emploi_duree_a_annee_3").value = "";
            document.getElementById("emploi_date_attestation_3").value = "";
        }
    });

/********************************************************************************************************
 * Gestion des transitions du menu de navigation
 ********************************************************************************************************/
    $(".liens_nav").click(function () {
        // Pourquoi lorsque je mets var la variable n'entre pas dans le for loop
        etatSoumettre = document.getElementById("soumettre").disabled;
        etatSuivant = document.getElementById("suivant").disabled;
        etatPrecedent = document.getElementById("precedent").disabled;
        desactiverBoutons();

        for (var i = 0; i < formulaire.length; i++) {
            if (formulaire[i].style.display !== "none") {
                if (appelerValidation(formulaire[i])) {

                    $(formulaire[i]).fadeOut();

                    for (var j = 0; j < menuNavigable.length; j++) {
                        if (menuNavigable[j].id === this.id) {
                            $(formulaire[j]).delay(delaisFadeOutIn).fadeIn();
                            if (j === 0) {
                                etatPrecedent = true;
                                etatSuivant = false;
                            } else if (j === formulaire.length - 1) {
                                etatSuivant = true;
                                etatPrecedent = false;
                            } else {
                                etatSuivant = false;
                                etatPrecedent = false;
                            }
                            break;
                        }
                    }
                }
                setTimeout("document.getElementById(\"soumettre\").disabled = etatSoumettre;", delaisBoutons);
                setTimeout("document.getElementById(\"suivant\").disabled = etatSuivant;", delaisBoutons);
                setTimeout("document.getElementById(\"precedent\").disabled = etatPrecedent;", delaisBoutons);
                break;
            }
        }
    });

    /* slide sur le menu navigable */
    $(".slide_menu_nav").click(function () {
        for (var i = 0; i < titreMenuNavigable.length; i++) {
            if (titreMenuNavigable[i].id === this.id) {
                $(sectionMenuNavigable[i]).slideToggle();
            }
        }
    });

/********************************************************************************************************
 * Faire ouvrir les liens dans des onglets pour ne pas briser le remplissage du formulaire
 * dépendant de la configuration du navigateur client
 ********************************************************************************************************/

    $("#ouvrir_page4").on("click", function () {
        window.open('http://www.regis.uqam.ca/Pdf/formulaires/DA_1.pdf', '_blank');
    });
    $("#ouvrir_etudier_uqam").on("click", function () {
        window.open('http://www.etudier.uqam.ca/', '_blank');
    });

/********************************************************************************************************
 * datepicker de JQuery UI
 ********************************************************************************************************/
    var datepickerValeurs = {
        altField: ".date",
        closeText: 'Fermer',
        prevText: 'Précédent',
        nextText: 'Suivant',
        monthNames: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
        monthNamesShort: ['Janv.', 'Févr.', 'Mars', 'Avril', 'Mai', 'Juin', 'Juil.', 'Ao�t', 'Sept.', 'Oct.', 'Nov.', 'Déc.'],
        dayNames: ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'],
        dayNamesShort: ['Dim.', 'Lun.', 'Mar.', 'Mer.', 'Jeu.', 'Ven.', 'Sam.'],
        dayNamesMin: ['D', 'L', 'M', 'M', 'J', 'V', 'S'],
        weekHeader: 'Sem.',
        dateFormat: 'yy-mm-dd',
        changeYear: true,
        yearRange: '1900:2100'
    };

    $(function () {
        $('#ident_date_naissance').datepicker(datepickerValeurs);
        $('#progdemande_presence_autre').datepicker(datepickerValeurs);
        $('#emploi_date_attestation_1').datepicker(datepickerValeurs);
        $('#emploi_date_attestation_2').datepicker(datepickerValeurs);
        $('#emploi_date_attestation_3').datepicker(datepickerValeurs);
    });
});

/********************************************************************************************************
 * Fonctions
 ********************************************************************************************************/

/* désactive tous les boutons */
function desactiverBoutons() {
    document.getElementById("precedent").disabled = true;
    document.getElementById("suivant").disabled = true;
    document.getElementById("soumettre").disabled = true;
}

/* valide la page du formulaire avant l'envoit */
function validerAvantSubmit() {

    // lorsque je mets var ça ne fonctionen pas...
    etatSoumettreSubmit = document.getElementById("soumettre").disabled;
    etatSuivantSubmit = document.getElementById("suivant").disabled;
    etatPrecedentSubmit = document.getElementById("precedent").disabled;
    desactiverBoutons();
    var formulaire = document.getElementsByClassName("div_formulaire");
    var delaisBoutons = 1000;

    for (var i = 0; i < formulaire.length; i++) {
        if (formulaire[i].style.display !== "none") {
            if (appelerValidation(formulaire[i])) {
                return true;
            } else {
                setTimeout("document.getElementById(\"suivant\").disabled = etatSuivantSubmit;", delaisBoutons);
                setTimeout("document.getElementById(\"precedent\").disabled = etatPrecedentSubmit;", delaisBoutons);
                setTimeout("document.getElementById(\"soumettre\").disabled = etatSoumettreSubmit;", delaisBoutons);
                return false;
            }
        }
    }
}

/* active le menu de navigation au fur et à mesure que l'on avance dans le formulaire */
function activerMenu(position) {
    var lien =  document.getElementsByClassName("liens_nav");
    lien[position].style.pointerEvents = "visiblePainted";
    lien[position].style.color = "#006c9e";

    var completion = Math.round(position / (lien.length-1) * 100);
    document.getElementById("completion").innerHTML = completion + "%";
}