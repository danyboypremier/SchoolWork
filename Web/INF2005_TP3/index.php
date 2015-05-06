<?php
define("MIN_COMBOBOX_YEAR", 1960); // Année min disponible dans les <select>
define("MAX_COMBOBOX_YEAR", 2015); // Année max disponible dans les <select>

// Génération des nombres X à Y dans un combobox
function buildSelectNumbersElements($startYear, $endYear)
{
    echo '<option selected value="">--svp choisir--</option>';
    while ($startYear <= $endYear) {
        echo '<option value="' . $startYear . '">' . $startYear . '</option>';
        $startYear++;
    }
}

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Demande d'admission - UQAM</title>
    <link href="CSS/formulaire.css" rel="stylesheet" type="text/css">
    <link href="CSS/bootstrap_mod.css" rel="stylesheet" type="text/css">
    <link href="http://code.jquery.com/ui/1.10.4/themes/ui-lightness/jquery-ui.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.2.js"></script>
    <script src="http://code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
    <script src="js/validation.js" charset="UTF-8"></script>
    <script src="js/index_transition.js" charset="UTF-8"></script>
</head>
<body>
<header>
    <br>
    <h1>Demande d'admission UQAM</h1>
    <br>
    <hr>
</header>
<nav>
    <div>
        <p id="menu_1" class="slide_menu_nav">
            <a>Identification</a>
        </p>
        <ul class="section_menu_nav" style="display:none">
            <li><a id="lien_div_formulaire_1_1" class="liens_nav identification">Nom et prénom</a></li>
            <li><a id="lien_div_formulaire_1_2" class="liens_nav identification a_disable" style="pointer-events: none">Information des parents</a></li>
            <li><a id="lien_div_formulaire_1_3" class="liens_nav identification a_disable" style="pointer-events: none">Téléphone</a></li>
            <li><a id="lien_div_formulaire_1_4" class="liens_nav identification a_disable" style="pointer-events: none">Adresse</a></li>
            <li><a id="lien_div_formulaire_1_5" class="liens_nav identification a_disable" style="pointer-events: none">Statut et langue</a></li>
        </ul>
    </div>
    <hr>
    <div>
        <p id="menu_2" class="slide_menu_nav">
            <a>Programmes demandés</a>
        </p>
        <ul class="section_menu_nav" style="display:none">
            <li><a id="lien_div_formulaire_2_1" class="liens_nav a_disable" style="pointer-events: none">Programmes</a></li>
        </ul>
    </div>
    <hr>
    <div>
        <p id="menu_3" class="slide_menu_nav">
            <a>Renseignements sur les études secondaire et collégiales</a>
        </p>
        <ul class="section_menu_nav" style="display:none">
            <li><a id="lien_div_formulaire_3_1" class="liens_nav a_disable" style="pointer-events: none">Secondaire</a></li>
            <li><a id="lien_div_formulaire_3_2" class="liens_nav a_disable" style="pointer-events: none">Collégiale</a></li>
        </ul>
    </div>
    <hr>
    <div>
        <p id="menu_4" class="slide_menu_nav">
            <a>Renseignements sur les études universitaires</a>
        </p>
        <ul class="section_menu_nav" style="display:none">
            <li><a id="lien_div_formulaire_4_1" class="liens_nav a_disable" style="pointer-events: none">Universitaire</a></li>
        </ul>
    </div>
    <hr>
    <div>
        <p id="menu_5" class="slide_menu_nav">
            <a>Renseignements sur les emplois</a>
        </p>
        <ul class="section_menu_nav" style="display:none">
            <li><a id="lien_div_formulaire_5_1" class="liens_nav a_disable" style="pointer-events: none">Premier emploi</a></li>
            <li><a id="lien_div_formulaire_5_2" class="liens_nav a_disable" style="pointer-events: none">Deuxième et troisième emploi</a></li>
        </ul>
    </div>
    <hr>
    <div>
        <p id="menu_6" class="slide_menu_nav">
            <a>Renseignements supplémentaires</a>
        </p>
        <ul class="section_menu_nav" style="display:none">
            <li><a id="lien_div_formulaire_6_1" class="liens_nav a_disable" style="pointer-events: none">Autre</a></li>

        </ul>
    </div>
    <hr>
    <div>
        <p id="menu_7" class="slide_menu_nav">
            <a>À lire attentivement</a>
        </p>
        <ul class="section_menu_nav" style="display:none">
            <li><a id="lien_div_formulaire_7_1" class="liens_nav a_disable" style="pointer-events: none">Confirmation</a></li>
        </ul>
    </div>
    <hr>
</nav>
<div id="centre">
    <form method="post" onsubmit="return validerAvantSubmit();" action="validation.php">

        <div class="formulaire">

            <table class="tab_ajust_contenu boutons">
                <tr>
                    <td>
                        <button id="precedent" class="class_bouton btn btn-primary" type="button" disabled>Précédent</button>
                    </td>
                    <td>
                        <button id="suivant" class="class_bouton btn btn-primary" type="button">Suivant</button>
                    </td>
                    <td>
                        <button id="soumettre" class="class_bouton btn btn-primary" type="submit" disabled>Soumettre</button>
                    </td>
                    <td>
                        <span>Complété à : <span id="completion">0 %</span></span>
                    </td>
                </tr>
            </table>

            <!-- ########################################################################################### -->
            <!-- ############################### Section Identification #################################### -->
            <!-- ########################################################################################### -->

            <div id="div_formulaire_1_1" class="div_formulaire">
                <div id="div_erreur_1_1" style="display:none">
                    <div id="erreur_nom" class="erreur_1_1 div_erreur" style="display:none">*Nom de famille requis<br>
                    </div>
                    <div id="erreur_prenom" class="erreur_1_1 div_erreur" style="display:none">*Prénom requis<br>
                    </div>
                    <div id="erreur_code_uqam" class="erreur_1_1 div_erreur" style="display:none">*Code permanent de
                        l'UQAM de format invalide<br></div>
                    <div id="erreur_code" class="erreur_1_1 div_erreur" style="display:none">*Code permanent du ministère absent ou de format
                        invalide<br></div>
                    <div id="erreur_ville_naissance" class="erreur_1_1 div_erreur" style="display:none">*Ville de naissance requise<br></div>
                    <div id="erreur_citoyennete" class="erreur_1_1 div_erreur" style="display:none">
                        *Vous devez choisir votre citoyenneté
                        et si vous choisissez autre, veuillez la spécifier<br>
                    </div>
                </div>
                <table class="table_50">
                    <tr class="sous_titre">
                        <td>
                            Identification
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_nom">Nom de famille à la naissance</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_nom" name="ident_nom" size="30">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_prenom">Prénom usuel</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_prenom" name="ident_prenom" size="60">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_code_uqam">Code permanent (alphanumérique) si vous avez déjà étudié à
                                l'UQAM (facultatif)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_code_uqam" name="ident_code_uqam" size="60">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_code">Code permanent (alphanumérique) du ministère de l'Enseignement
                                supérieur, de la Recherche et de
                                la Science</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_code" name="ident_code" size="60">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_ville_naissance">Lieu de naissance (ville)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_ville_naissance" name="ident_ville_naissance" size="60">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td colspan="3">
                            Citoyenneté:
                        </td>
                    </tr>
                    <tr>
                        <td class="tab_right">
                            <input type="radio" id="ident_citoyennete_ca" name="ident_citoyennete" value="canadienne">
                        </td>
                        <td colspan="2">
                            <label for="ident_citoyennete_ca">Canadienne</label>
                        </td>
                    </tr>
                    <tr>
                        <td class="tab_right">
                            <input type="radio" id="ident_citoyennete_autre" name="ident_citoyennete" value="autre">
                        </td>
                        <td>
                            <label for="ident_citoyennete_autre">Autre (précisez)</label>
                        </td>
                        <td>
                            <input type="text" id="ident_citoyennete_texte" name="ident_citoyennete_texte" size="40"
                                   disabled>
                        </td>
                    </tr>
                </table>
            </div>

            <div id="div_formulaire_1_2" class="div_formulaire" style="display:none">
                <div id="div_erreur_1_2" style="display:none">
                    <div id="erreur_nom_pere" class="erreur_1_2 div_erreur" style="display:none">*Nom du père n'est pas
                        complet<br></div>
                    <div id="erreur_nom_mere" class="erreur_1_2 div_erreur" style="display:none">*Nom de la mère n'est pas
                        complet<br></div>
                </div>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_nom_pere">Nom de famille du père à la naissance (facultatif)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_nom_pere" name="ident_nom_pere" size="60">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_prenom_pere">Prénom usuel du père (facultatif)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_prenom_pere" name="ident_prenom_pere" size="60">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_nom_mere">Nom de famille de la mère à la naissance (facultatif)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_nom_mere" name="ident_nom_mere" size="60">
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_prenom_mere">Prénom usuel de la mère (facultatif)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_prenom_mere" name="ident_prenom_mere" size="60">
                        </td>
                    </tr>
                </table>
            </div>

            <div id="div_formulaire_1_3" class="div_formulaire" style="display:none">
                <div id="div_erreur_1_3" style="display:none">
                    <div id="erreur_telephone_dom" class="erreur_1_3 div_erreur" style="display:none">*Numéro de
                        téléphone invalide<br></div>
                    <div id="erreur_telephone_tra" class="erreur_1_3 div_erreur" style="display:none">*Numéro de
                        téléphone au travail invalide<br></div>
                    <div id="erreur_telephone_cel" class="erreur_1_3 div_erreur" style="display:none">*Numéro de
                        téléphone cellulaire invalide<br></div>
                    <div id="erreur_telephone_parents" class="erreur_1_3 div_erreur" style="display:none">*Numéro de
                        téléphone des parents invalide<br></div>
                    <div id="erreur_courriel" class="erreur_1_3 div_erreur" style="display:none">*Adresse courriel
                        invalide<br></div>
                    <div id="erreur_telephone" class="erreur_1_3 div_erreur" style="display:none">*Veuillez donner au moins un numéro de téléphone<br></div>
                </div>
                <table class="table_50">
                    <tr>
                        <td>
                            <span>Veuillez donner au moins un numéro de téléphone<br>
                            Format 999 999-9999</span>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td>
                            <span>Téléphone à domicile</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <input type="text" id="ident_telephone_dom_1" name="ident_telephone_dom_1" size="2"><br>
                                <label for="ident_telephone_dom_1" class="police_11px">Ind. régional</label>
                            </div>
                            <div>
                                <input type="text" id="ident_telephone_dom_2" name="ident_telephone_dom_2" size="6"><br>
                                <label for="ident_telephone_dom_2" class="police_11px">Numéro</label>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td>
                            <span>Téléphone au travail</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <input type="text" id="ident_telephone_tra_1" name="ident_telephone_tra_1" size="2"><br>
                                <label for="ident_telephone_tra_1" class="police_11px">Ind. régional</label>
                            </div>
                            <div>
                                <input type="text" id="ident_telephone_tra_2" name="ident_telephone_tra_2" size="6"><br>
                                <label for="ident_telephone_tra_2" class="police_11px">Numéro</label>
                            </div>
                            <div>
                                <input type="text" id="ident_telephone_tra_3" name="ident_telephone_tra_3" size="2"><br>
                                <label for="ident_telephone_tra_3" class="police_11px">Poste</label>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td>
                            <span>Cellulaire</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <input type="text" id="ident_telephone_cel_1" name="ident_telephone_cel_1" size="2"><br>
                                <label for="ident_telephone_cel_1" class="police_11px">Ind. régional</label>
                            </div>
                            <div>
                                <input type="text" id="ident_telephone_cel_2" name="ident_telephone_cel_2" size="6"><br>
                                <label for="ident_telephone_cel_2" class="police_11px">Numéro</label>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td>
                            <span>Téléphone des parents (facultatif)</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <input type="text" id="ident_telephone_parents_1" name="ident_telephone_parents_1"
                                       size="2"><br>
                                <label for="ident_telephone_parents_1" class="police_11px">Ind. régional</label>
                            </div>
                            <div>
                                <input type="text" id="ident_telephone_parents_2" name="ident_telephone_parents_2"
                                       size="6"><br>
                                <label for="ident_telephone_parents_2" class="police_11px">Numéro</label>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td>
                            <label for="ident_courriel">Courriel (facultatif)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="email" id="ident_courriel" name="ident_courriel" size="60">
                        </td>
                    </tr>
                </table>
            </div>

            <div id="div_formulaire_1_4" class="div_formulaire" style="display:none">
                <div id="div_erreur_1_4" style="display:none">
                    <div id="erreur_num_civique" class="erreur_1_4 div_erreur" style="display:none">*Numéro civique doit
                        être identifié ou de format numérique<br></div>
                    <div id="erreur_rue" class="erreur_1_4 div_erreur" style="display:none">*Le champs rue doit être
                        rempli<br></div>
                    <div id="erreur_municipalite" class="erreur_1_4 div_erreur" style="display:none">*Le champs
                        municipalité doit être rempli<br></div>
                    <div id="erreur_code_postal" class="erreur_1_4 div_erreur" style="display:none">*Le code postal
                        canadien doit être de format X9X9X9<br></div>
                    <div id="erreur_num_civique_2" class="erreur_1_4 div_erreur" style="display:none">*Numéro civique de
                        résidence doit être identifié<br></div>
                    <div id="erreur_rue_2" class="erreur_1_4 div_erreur" style="display:none">*Le champs rue de
                        résidence doit être rempli<br></div>
                    <div id="erreur_municipalite_2" class="erreur_1_4 div_erreur" style="display:none">*Le champs
                        municipalité de résidence doit être rempli<br></div>
                    <div id="erreur_code_postal_2" class="erreur_1_4 div_erreur" style="display:none">*Le code postal
                        canadien de résidence doit être de format X9X9X9<br></div>
                </div>
                <table class="table_50">
                    <tr>
                        <td colspan="4">
                            <span>Adresse de correspondance</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_num_civique" name="ident_num_civique" size="1">
                        </td>
                        <td>
                            <input type="text" id="ident_rue" name="ident_rue" size="20">
                        </td>
                        <td>
                            <input type="text" id="ident_direction" name="ident_direction" size="1">
                        </td>
                        <td>
                            <input type="text" id="ident_appartement" name="ident_appartement" size="1">
                        </td>
                    </tr>
                    <tr class="police_11px">
                        <td>
                            <label for="ident_num_civique">N° civique</label>
                        </td>
                        <td>
                            <label for="ident_rue">Type et nom de la rue</label>
                        </td>
                        <td>
                            <label for="ident_direction">Direction de rue</label>
                        </td>
                        <td>
                            <label for="ident_appartement">N° d'appartement ou d'unité</label>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td>
                            <input type="text" id="ident_municipalite" name="ident_municipalite" size="20">
                        </td>
                        <td>
                            <input type="text" id="ident_pays" name="ident_pays" size="20">
                        </td>
                        <td>
                            <input type="text" id="ident_code_postal" name="ident_code_postal" size="2">
                        </td>
                    </tr>
                    <tr class="police_11px">
                        <td>
                            <label for="ident_municipalite">Municipalité</label>
                        </td>
                        <td>
                            <label for="ident_pays">Pays (si autre que le Canada)</label>
                        </td>
                        <td>
                            <label for="ident_code_postal">Code Postal</label>
                        </td>
                    </tr>
                </table>
                <table class="tab_ajust_contenu">
                    <tr>
                        <td>
                            <input id="ident_check_adresse_res" name="ident_check_adresse_res" value="select"
                                   type="checkbox">
                        </td>
                        <td>
                            <label for="ident_check_adresse_res">
                                Adresse où vous résidez actuellement (si différente de l'adresse de correspondance)
                            </label>
                        </td>
                    </tr>
                </table>
                <table class="adresse_res table_50" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="ident_num_civique_2" name="ident_num_civique_2" size="1">
                        </td>
                        <td>
                            <input type="text" id="ident_rue_2" name="ident_rue_2" size="20">
                        </td>
                        <td>
                            <input type="text" id="ident_direction_2" name="ident_direction_2" size="1">
                        </td>
                        <td>
                            <input type="text" id="ident_appartement_2" name="ident_appartement_2" size="1">
                        </td>
                    </tr>
                    <tr class="police_11px">
                        <td>
                            <label for="ident_num_civique_2">N° civique</label>
                        </td>
                        <td>
                            <label for="ident_rue_2">Type et nom de la rue</label>
                        </td>
                        <td>
                            <label for="ident_direction_2">Direction de rue</label>
                        </td>
                        <td>
                            <label for="ident_appartement_2">N° d'appartement ou d'unité</label>
                        </td>
                    </tr>
                </table>
                <table class="adresse_res table_50" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="ident_municipalite_2" name="ident_municipalite_2" size="20">
                        </td>
                        <td>
                            <input type="text" id="ident_pays_2" name="ident_pays_2" size="20">
                        </td>
                        <td>
                            <input type="text" id="ident_code_postal_2" name="ident_code_postal_2" size="2">
                        </td>
                    </tr>
                    <tr class="police_11px">
                        <td>
                            <label for="ident_municipalite_2">Municipalité</label>
                        </td>
                        <td>
                            <label for="ident_pays_2">Pays (si autre que le Canada)</label>
                        </td>
                        <td>
                            <label for="ident_code_postal_2">Code Postal</label>
                        </td>
                    </tr>
                </table>
            </div>

            <div id="div_formulaire_1_5" class="div_formulaire" style="display:none">
                <div id="div_erreur_1_5" style="display:none">
                    <div id="erreur_date_naissance" class="erreur_1_5 div_erreur" style="display:none">*Date de naissance vide ou invalide<br></div>
                    <div id="erreur_sexe" class="erreur_1_5 div_erreur" style="display:none">*Veuillez choisir votre sexe<br></div>
                    <div id="erreur_assurance_so" class="erreur_1_5 div_erreur" style="display:none">*Numéro d'assurance sociale invalide<br></div>
                    <div id="erreur_statut" class="erreur_1_5 div_erreur" style="display:none">*Veuillez choisir votre statut<br></div>
                    <div id="erreur_langue_usage" class="erreur_1_5 div_erreur" style="display:none">*Veuillez choisir votre langue d'usage<br></div>
                    <div id="erreur_langue_usage_autre" class="erreur_1_5 div_erreur" style="display:none">*Veuillez identifier la langue d'usage "autre"<br></div>
                    <div id="erreur_langue_mater" class="erreur_1_5 div_erreur" style="display:none">*Veuillez choisir votre langue maternelle<br></div>
                    <div id="erreur_langue_mater_autre" class="erreur_1_5 div_erreur" style="display:none">*Veuillez identifier la langue maternelle "autre"<br></div>
                </div>
                <table class="table_50">
                    <tr>
                        <td>
                            <label for="ident_date_naissance">Date de naissance</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_date_naissance" name="ident_date_naissance">
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td>
                            <label for="ident_sexe">Sexe</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <select id="ident_sexe" name="ident_sexe">
                                <option value="">--svp choisir--</option>
                                <option value="femme">Femme</option>
                                <option value="homme">Homme</option>
                            </select>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td>
                            <label for="ident_assurance_so">N° d'assurance social</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="ident_assurance_so" name="ident_assurance_so" size="30">
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <label for="ident_statut">Statut au Canada</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <select id="ident_statut" name="ident_statut">
                                <option value="">--svp choisir--</option>
                                <option value="citoyen_canadien">Citoyen canadien</option>
                                <option value="resident_permanent">Résident permanent</option>
                                <option value="permis_etude">Permis d'étude</option>
                                <option value="permis_travail">Permis de travail</option>
                                <option value="amerindien">Amérindien</option>
                                <option value="visa">Visa d'iplomatique</option>
                                <option value="permis_sejour">Permis de séjour temporaire</option>
                                <option value="refugie">Réfugié</option>
                            </select>
                        </td>
                        <td>
                                <span class="police_rouge">
                                    Si vous n'êtes pas né au Québec, veuillez vous référer au texte de l'encadré gris de la
                                    <a id="ouvrir_page4">page 4.</a>
                                </span>
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td colspan="2">
                            <label for="ident_langue_usage">Langue d'usage (Langue parlée le plus souvent à la
                                maison)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <select id="ident_langue_usage" name="ident_langue_usage">
                                <option value="">--svp choisir--</option>
                                <option value="francais">Français</option>
                                <option value="anglais">Anglais</option>
                                <option value="amerindien">Amérindien ou Inukitut</option>
                                <option value="autre">Autre (précisez)</option>
                            </select>
                        </td>
                        <td>
                            <input type="text" id="ident_langue_usage_autre" name="ident_langue_usage_autre" size="30"
                                   disabled>
                        </td>
                    </tr>
                </table>
                <table class="tab_text_100 table_50">
                    <tr>
                        <td colspan="2">
                            <label for="ident_langue_mater">Langue maternelle (Première langue apprise et encore
                                comprise)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <select id="ident_langue_mater" name="ident_langue_mater">
                                <option value="">--svp choisir--</option>
                                <option value="francais">Français</option>
                                <option value="anglais">Anglais</option>
                                <option value="amerindien">Amérindien ou Inukitut</option>
                                <option value="autre">Autre (précisez)</option>
                            </select>
                        </td>
                        <td>
                            <input type="text" id="ident_langue_mater_autre" name="ident_langue_mater_autre" size="30"
                                   disabled>
                        </td>
                    </tr>
                </table>
            </div>

            <!-- ########################################################################################### -->
            <!-- ############################### Section Programmes Demandés ############################### -->
            <!-- ########################################################################################### -->

            <div id="div_formulaire_2_1" class="div_formulaire" style="display:none">
                <div id="div_erreur_2_1" style="display:none">
                    <div id="erreur_progdemande_trimestre" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir le trimestre<br></div>
                    <div id="erreur_progdemande_trimestre_annee" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir l'année du trimestre<br></div>
                    <div id="erreur_progdemande_choix_1_titre" class="erreur_2_1 div_erreur" style="display:none">*Veuillez entrer le titre du premier choix<br></div>
                    <div id="erreur_progdemande_choix_1_type" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir le type de diplôme du premier choix<br></div>
                    <div id="erreur_progdemande_choix_1_temps" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir l'horaire désiré du premier choix<br></div>
                    <div id="erreur_progdemande_choix_1_code" class="erreur_2_1 div_erreur" style="display:none">*Veuillez entrer le code du programme du premier choix<br></div>
                    <div id="erreur_progdemande_choix_2_titre" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir le type de diplôme du deuxième choix<br></div>
                    <div id="erreur_progdemande_choix_2_type" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir le type de diplôme du deuxième choix<br></div>
                    <div id="erreur_progdemande_choix_2_temps" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir l'horaire désiré du deuxième choix<br></div>
                    <div id="erreur_progdemande_choix_2_code" class="erreur_2_1 div_erreur" style="display:none">*Veuillez entrer le code du programme du deuxième choix<br></div>
                    <div id="erreur_progdemande_choix_3_titre" class="erreur_2_1 div_erreur" style="display:none">*Veuillez entrer le titre du troisième choix<br></div>
                    <div id="erreur_progdemande_choix_3_type" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir le type de diplôme du troisième choix<br></div>
                    <div id="erreur_progdemande_choix_3_temps" class="erreur_2_1 div_erreur" style="display:none">*Veuillez choisir l'horaire désiré du troisième choix<br></div>
                    <div id="erreur_progdemande_choix_3_code" class="erreur_2_1 div_erreur" style="display:none">*Veuillez entrer le code du programme du troisième choix<br></div>
                    <div id="erreur_progdemande_presence" class="erreur_2_1 div_erreur" style="display:none">*Veuillez sélectionner si vous êtes disponible pour un examen<br></div>
                    <div id="erreur_progdemande_presence_autre" class="erreur_2_1 div_erreur" style="display:none">*Veuillez donner la date de votre retour<br></div>
                </div>
                <table class="table_50">
                    <tr class="sous_titre">
                        <td>
                            Programmes demandés
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <label for="progdemande_trimestre">Je désire entreprendre mes études au trimestre</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <select id="progdemande_trimestre" name="progdemande_trimestre">
                                <option value="">--svp choisir--</option>
                                <option value="hiver">Hiver</option>
                                <option value="ete">Été</option>
                                <option value="automne">Automne</option>
                            </select>
                        </td>
                        <td>
                            <label for="progdemande_trimestre_annee">Année</label>
                            <select id="progdemande_trimestre_annee" name="progdemande_trimestre_annee" disabled>
                                <?php buildSelectNumbersElements(2015, 2030); ?>
                            </select>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <span>Premier choix</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <input type="text" id="progdemande_choix_1_titre" name="progdemande_choix_1_titre"
                                       size="60"><br>
                                <label for="progdemande_choix_1_titre" class="police_11px">Titre</label>
                            </div>
                        </td>
                        <td>
                            <div>
                                <input type="text" id="progdemande_choix_1_code" name="progdemande_choix_1_code"
                                       size="3"><br>
                                <label for="progdemande_choix_1_code" class="police_11px">Code</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <div>
                                <select id="progdemande_choix_1_type" name="progdemande_choix_1_type">
                                    <option value="">--svp choisir--</option>
                                    <option value="bac">Baccalauréat</option>
                                    <option value="maj">Majeure</option>
                                    <option value="min">Mineure</option>
                                    <option value="cer">Certificat</option>
                                    <option value="cou">Programme court</option>
                                </select><br>
                                <span class="police_11px">Diplôme</span>
                            </div>
                            <div>
                                <select id="progdemande_choix_1_temps" name="progdemande_choix_1_temps">
                                    <option value="">--svp choisir--</option>
                                    <option value="complet">Temps complet</option>
                                    <option value="partiel">Temps partiel</option>
                                </select><br>
                                <span class="police_11px">Horaire</span>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <span>Deuxième choix (optionnelle)</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <input type="text" id="progdemande_choix_2_titre" class="choix_2" name="progdemande_choix_2_titre"
                                       size="60"><br>
                                <label for="progdemande_choix_2_titre" class="police_11px">Titre</label>
                            </div>
                        </td>
                        <td>
                            <div>
                                <input type="text" id="progdemande_choix_2_code" class="choix_2" name="progdemande_choix_2_code"
                                       size="3"><br>
                                <label for="progdemande_choix_2_code" class="police_11px">Code</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <div>
                                <select id="progdemande_choix_2_type" name="progdemande_choix_2_type">
                                    <option value="">--svp choisir--</option>
                                    <option value="bac">Baccalauréat</option>
                                    <option value="maj">Majeure</option>
                                    <option value="min">Mineure</option>
                                    <option value="cer">Certificat</option>
                                    <option value="cou">Programme court</option>
                                </select><br>
                                <span class="police_11px">Diplôme</span>
                            </div>
                            <div>
                                <select id="progdemande_choix_2_temps" name="progdemande_choix_2_temps">
                                    <option value="">--svp choisir--</option>
                                    <option value="complet">Temps complet</option>
                                    <option value="partiel">Temps partiel</option>
                                </select><br>
                                <span class="police_11px">Horaire</span>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <span>Troisième choix (nous vous suggérons fortement un programme non contingenté) (optionnelle)</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <input type="text" id="progdemande_choix_3_titre" class="choix_3" name="progdemande_choix_3_titre"
                                       size="60"><br>
                                <label for="progdemande_choix_3_titre" class="police_11px">Titre</label>
                            </div>
                        </td>
                        <td>
                            <div>
                                <input type="text" id="progdemande_choix_3_code" class="choix_3" name="progdemande_choix_3_code"
                                       size="3"><br>
                                <label for="progdemande_choix_3_code" class="police_11px">Code</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <div>
                                <select id="progdemande_choix_3_type" name="progdemande_choix_3_type">
                                    <option value="">--svp choisir--</option>
                                    <option value="bac">Baccalauréat</option>
                                    <option value="maj">Majeure</option>
                                    <option value="min">Mineure</option>
                                    <option value="cer">Certificat</option>
                                    <option value="cou">Programme court</option>
                                </select><br>
                                <span class="police_11px">Diplôme</span>
                            </div>
                            <div>
                                <select id="progdemande_choix_3_temps" name="progdemande_choix_3_temps">
                                    <option value="">--svp choisir--</option>
                                    <option value="complet">Temps complet</option>
                                    <option value="partiel">Temps partiel</option>
                                </select><br>
                                <span class="police_11px">Horaire</span>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <span class="police_rouge">
                                Certains programmes exigent des tests de sélection ou comportent des exigences particulières.
                                Consultez le site <a id="ouvrir_etudier_uqam">www.etudier.uqam.ca</a>.
                                Votre présence peut être obligatoire en
                                mars, en avril ou en mai pour l’admission au trimestre d’automne.
                            </span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>Serez-vous au Québec à ce moment ?</span>
                        </td>
                        <td>
                            <select id="progdemande_presence" name="progdemande_presence">
                                <option value="">--svp choisir--</option>
                                <option value="oui">Oui</option>
                                <option value="non">Non</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="progdemande_presence_autre">Si non, date d'arrivé</label>
                        </td>
                        <td>
                            <input type="text" id="progdemande_presence_autre" name="progdemande_presence_autre"
                                   disabled>
                        </td>
                    </tr>
                </table>
            </div>

            <!-- ########################################################################################### -->
            <!-- ############################### Section Études Secondaires et Collégiales ################# -->
            <!-- ########################################################################################### -->

            <div id="div_formulaire_3_1" class="div_formulaire" style="display:none">
                <div id="div_erreur_3_1" style="display:none">
                    <div id="erreur_secondcollege_derniere_annee_sec" class="erreur_3_1 div_erreur" style="display:none">*Veuillez spécifier la dernière année complétée<br></div>
                    <div id="erreur_secondcollege_annee_1" class="erreur_3_1 div_erreur" style="display:none">*Veuillez spécifier la période de fréquentation de la dernière année d'étude<br></div>
                    <div id="erreur_secondcollege_annee_logic_1" class="erreur_3_1 div_erreur" style="display:none">*L'année de fréquentation de début doit précéder l'année de fréquentation de fin<br></div>
                    <div id="erreur_secondcollege_discipline" class="erreur_3_1 div_erreur" style="display:none">*Veuillez spécifier la discipline<br></div>
                    <div id="erreur_secondcollege_annee_logic_2" class="erreur_3_1 div_erreur" style="display:none">*L'année de fréquentation de la discipline de début doit précéder l'année de fréquentation de fin<br></div>
                    <div id="erreur_secondcollege_annee_2" class="erreur_3_1 div_erreur" style="display:none">*Veuillez spécifier pour la discipline la période de fréquentation de la dernière année d'étude<br></div>
                    <div id="erreur_secondcollege_institution" class="erreur_3_1 div_erreur" style="display:none">*Veuillez spécifier l'institution d'études<br></div>
                    <div id="erreur_secondcollege_obtention_mois" class="erreur_3_1 div_erreur" style="display:none">*Veuiller spécifier le mois d'obtention du diplôme<br></div>
                    <div id="erreur_secondcollege_obtention_annee" class="erreur_3_1 div_erreur" style="display:none">*Veuiller spécifier l'année d'obtention du diplôme<br></div>
                </div>
                <table class="table_50">
                    <tr class="sous_titre">
                        <td>
                            Renseignements sur les études secondaires et collégiales (facultatif)
                        </td>
                    </tr>
                </table>
                <table class="tab_ajust_contenu">
                    <tr>
                        <td>
                            <input id="secondcollege_check_etude"
                                   name="secondcollege_check_etude" type="checkbox">
                        </td>
                        <td>
                            <label for="secondcollege_check_etude">J'ai un diplôme d'étude secondaire (DES)</label>
                        </td>
                    </tr>
                </table>
                <table class="table_50 etude_secondaire" style="display:none">
                    <tr>
                        <td></td>
                        <td>
                            <span>Période de fréquentation</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="secondcollege_derniere_annee_sec"
                                   name="secondcollege_derniere_annee_sec" size="40"><br>
                            <label for="secondcollege_derniere_annee_sec" class="police_11px">
                                Dernière année complétée
                            </label>
                        </td>
                        <td>
                            <div class="text_centre">
                                <select id="secondcollege_annee_debut_1" name="secondcollege_annee_debut_1">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_annee_debut_1" class="police_11px">De (AAAA)</label>
                            </div>
                            <div class="text_centre">
                                <select id="secondcollege_annee_fin_1" name="secondcollege_annee_fin_1">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_annee_fin_1" class="police_11px">À (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="tab_ajust_contenu etude_secondaire" style="display:none">
                    <tr>
                        <td>
                            <input id="secondcollege_check_etude_sec_exterieur"
                                   name="secondcollege_check_etude_sec_exterieur" type="checkbox">
                        </td>
                        <td>
                            <label for="secondcollege_check_etude_sec_exterieur">Diplôme d'études secondaires
                                poursuivies à l'extérieur du Québec</label>
                        </td>
                    </tr>
                </table>
                <table id="etude_secondaire_exterieure" class="table_50 etude_secondaire" style="display:none">
                    <tr>
                        <td></td>
                        <td>
                            <span>Période de fréquentation</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="secondcollege_discipline_1"
                                   name="secondcollege_discipline_1" size="40"><br>
                            <label for="secondcollege_discipline_1" class="police_11px">
                                Discipline ou spécialisation</label> 
                        </td>
                        <td class="text_centre">
                            <div>
                                <select id="secondcollege_annee_debut_2" name="secondcollege_annee_debut_2">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_annee_debut_2" class="police_11px">De (AAAA)</label>
                            </div>
                            <div class="text_centre">
                                <select id="secondcollege_annee_fin_2" name="secondcollege_annee_fin_2">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_annee_fin_2" class="police_11px">À (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <span>Date d'obtention</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="secondcollege_institution_1"
                                   name="secondcollege_institution_1" size="40"><br>
                            <label for="secondcollege_institution_1" class="police_11px">Institution où vous
                                avez poursuivi vos études</label>
                        </td>
                        <td>
                            <div class="text_centre">
                                <select id="secondcollege_obtention_mois_1" name="secondcollege_obtention_mois_1">
                                    <?php buildSelectNumbersElements(1, 12) ?>
                                </select><br>
                                <label for="secondcollege_obtention_mois_1" class="police_11px">Mois (MM)</label>
                            </div>
                            <div class="text_centre">
                                <select id="secondcollege_obtention_annee_1" name="secondcollege_obtention_annee_1">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_obtention_annee_1" class="police_11px">Année (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>

            <div id="div_formulaire_3_2" class="div_formulaire" style="display:none">
                <div id="div_erreur_3_2" style="display:none">
                    <div id="erreur_secondcollege_nom_diplome_dec_aec" class="erreur_3_2 div_erreur" style="display:none">*Veuillez spécifier le diplôme d'étude<br></div>
                    <div id="erreur_secondcollege_radio_dec_aec" class="erreur_3_2 div_erreur" style="display:none">*Veuillez spécifier si le diplôme a été obtenu/en cours/ne sera pas obtenu<br></div>
                    <div id="erreur_secondcollege_institution_dec_aec" class="erreur_3_2 div_erreur" style="display:none">*Veuillez spécifier l'établissement<br></div>
                    <div id="erreur_secondcollege_annee_3" class="erreur_3_2 div_erreur" style="display:none">*Veuillez spécifier l'année du début et de finde la fréquentation de l'établissement<br></div>
                    <div id="erreur_secondcollege_annee_logic_3" class="erreur_3_2 div_erreur" style="display:none">*L'année de fréquentation de début doit précéder l'année de fréquentation de fin<br></div>
                    <div id="erreur_secondcollege_discipline_dec_aec" class="erreur_3_2 div_erreur" style="display:none">*Veuillez spécifier le nom de la discipline<br></div>
                    <div id="erreur_secondcollege_obtention" class="erreur_3_2 div_erreur" style="display:none">*Veuillez spécifier la date d'obtention du diplôme<br></div>
                </div>
                <table class="tab_ajust_contenu">
                    <tr>
                        <td>
                            <input id="secondcollege_radio_dec" name="secondcollege_dec_aec" type="radio" value="dec">
                        </td>
                        <td>
                            <label for="secondcollege_radio_dec">DEC</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input id="secondcollege_radio_aec" name="secondcollege_dec_aec" type="radio" value="aec">
                        </td>
                        <td>
                            <label for="secondcollege_radio_aec">Autre diplôme de niveau collégial (AEC,
                                CEC,...)</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input id="secondcollege_radio_aucun" name="secondcollege_dec_aec" type="radio" value=""
                                   checked="checked">
                        </td>
                        <td>
                            <label for="secondcollege_radio_dec">Aucun</label>
                        </td>
                    </tr>
                </table>
                <table id="etude_collegiale" class="table_50" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="secondcollege_nom_diplome_dec_aec"
                                   name="secondcollege_nom_diplome_dec_aec" size="40"><br>
                            <label for="secondcollege_nom_diplome_dec_aec" class="police_11px">Nom du diplôme</label>
                        </td>
                        <td>
                            <input id="secondcollege_radio_dec_obtention" name="secondcollege_dec_obtention"
                                   type="radio" value="obtenu">
                            <label for="secondcollege_radio_dec_obtention" class="police_11px">Obtenu</label><br>
                            <input id="secondcollege_radio_dec_a_obtenir" name="secondcollege_dec_obtention"
                                   type="radio" value="a_obtenir">
                            <label for="secondcollege_radio_dec_a_obtenir" class="police_11px">À obtenir</label><br>
                            <input id="secondcollege_radio_dec_pas_obtenu" name="secondcollege_dec_obtention"
                                   type="radio" value="pas_termine">
                            <label for="secondcollege_radio_dec_pas_obtenu" class="police_11px">Ne sera pas
                                obtenu</label>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <span>Période de fréquentation</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="secondcollege_institution_dec_aec"
                                   name="secondcollege_institution_dec_aec" size="40"><br>
                            <label for="secondcollege_institution_dec_aec" class="police_11px">
                                Institution où vous avez poursuivi vos études en vue de l'obtention<br>
                                de ce diplôme
                            </label>
                        </td>
                        <td class="text_centre">
                            <div>
                                <select id="secondcollege_annee_debut_3" name="secondcollege_annee_debut_3">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_annee_debut_3" class="police_11px">De (AAAA)</label>
                            </div>
                            <div class="text_centre">
                                <select id="secondcollege_annee_fin_3" name="secondcollege_annee_fin_3">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_annee_fin_3" class="police_11px">À (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <span>Date d'obtention</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="secondcollege_discipline_dec_aec"
                                   name="secondcollege_discipline_dec_aec" size="40"><br>
                            <label for="secondcollege_discipline_dec_aec" class="police_11px">Discipline ou
                                spécialisation</label>
                        </td>
                        <td>
                            <div class="text_centre">
                                <select id="secondcollege_obtention_mois_2" name="secondcollege_obtention_mois_2" disabled>
                                    <?php buildSelectNumbersElements(1, 12) ?>
                                </select><br>
                                <label for="secondcollege_obtention_mois_2" class="police_11px">Mois (MM)</label>
                            </div>
                            <div class="text_centre">
                                <select id="secondcollege_obtention_annee_2" name="secondcollege_obtention_annee_2" disabled>
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="secondcollege_obtention_annee_2" class="police_11px">Année (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>

            <!-- ########################################################################################### -->
            <!-- ############################### Section Études Universitaires ############################# -->
            <!-- ########################################################################################### -->

            <div id="div_formulaire_4_1" class="div_formulaire" style="display:none">
                <div id="div_erreur_4_1" style="display:none">
                    <div id="erreur_uni_diplome_1" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier le diplôme d'étude universitaire du choix 1<br></div>
                    <div id="erreur_uni_radio_1" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier si le diplôme du choix 1 a été obtenu/en cours/ne sera pas obtenu<br></div>
                    <div id="erreur_uni_institution_1" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier l'établissement du choix 1<br></div>
                    <div id="erreur_uni_annee_1" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier l'année du début et de finde la fréquentation de l'établissement du choix 1<br></div>
                    <div id="erreur_uni_annee_logic_1" class="erreur_4_1 div_erreur" style="display:none">*L'année de fréquentation de début doit précéder l'année de fréquentation de fin pour le choix 1<br></div>
                    <div id="erreur_uni_discipline_1" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier le nom de la discipline pour le choix 1<br></div>
                    <div id="erreur_uni_obtention_1" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier la date d'obtention du diplôme pour le choix 1<br></div>

                    <div id="erreur_uni_diplome_2" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier le diplôme d'étude universitaire du choix 2<br></div>
                    <div id="erreur_uni_radio_2" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier si le diplôme du choix 2 a été obtenu/en cours/ne sera pas obtenu<br></div>
                    <div id="erreur_uni_institution_2" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier l'établissement du choix 2<br></div>
                    <div id="erreur_uni_annee_2" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier l'année du début et de finde la fréquentation de l'établissement du choix 2<br></div>
                    <div id="erreur_uni_annee_logic_2" class="erreur_4_1 div_erreur" style="display:none">*L'année de fréquentation de début doit précéder l'année de fréquentation de fin pour le choix 2<br></div>
                    <div id="erreur_uni_discipline_2" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier le nom de la discipline pour le choix 2<br></div>
                    <div id="erreur_uni_obtention_2" class="erreur_4_1 div_erreur" style="display:none">*Veuillez spécifier la date d'obtention du diplôme pour le choix 2<br></div>
                </div>
                <table class="table_50">
                    <tr class="sous_titre">
                        <td>
                            Renseignements sur les études universitaires
                        </td>
                    </tr>
                </table>
                <table class="tab_ajust_contenu">
                    <tr>
                        <td>
                            <input id="universitaires_check_universite" name="universitaires_check_universite"
                                   type="checkbox">
                        </td>
                        <td>
                            <label for="universitaires_check_universite">Grade ou diplôme de niveau universitaire le
                                plus récent
                                entrepris ou complété</label>
                        </td>
                    </tr>
                </table>
                <table class="table_50 grade_universitaire" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="universitaires_nom_diplome" name="universitaires_nom_diplome"
                                   size="40"><br>
                            <label for="universitaires_nom_diplome" class="police_11px">Nom du diplôme</label>
                        </td>
                        <td>
                            <input id="universitaires_radio_obtention" name="universitaires_obtention" type="radio"
                                   value="obtenu">
                            <label for="universitaires_radio_obtention" class="police_11px">Obtenu</label><br>
                            <input id="universitaires_radio_a_obtenir" name="universitaires_obtention" type="radio"
                                   value="a_obtenir">
                            <label for="universitaires_radio_a_obtenir" class="police_11px">À obtenir</label><br>
                            <input id="universitaires_radio_pas_obtenu" name="universitaires_obtention" type="radio"
                                   value="pas_termine">
                            <label for="universitaires_radio_pas_obtenu" class="police_11px">Ne sera pas obtenu</label>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <span>Période de fréquentation</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="universitaires_institution" name="universitaires_institution"
                                   size="40"><br>
                            <label for="universitaires_institution" class="police_11px">
                                Institution où vous avez poursuivi vos études en vue de l'obtention<br>
                                de ce diplôme
                            </label>
                        </td>
                        <td class="text_centre">
                            <div>
                                <select id="universitaires_annee_debut" name="universitaires_annee_debut">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="universitaires_annee_debut" class="police_11px">De (AAAA)</label>
                            </div>
                            <div class="text_centre">
                                <select id="universitaires_annee_fin" name="universitaires_annee_fin">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="universitaires_annee_fin" class="police_11px">À (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <span>Date d'obtention</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="universitaires_discipline" name="universitaires_discipline"
                                   size="40"><br>
                            <label for="universitaires_discipline" class="police_11px">Discipline ou
                                spécialisation</label>
                        </td>
                        <td>
                            <div class="text_centre">
                                <select id="universitaires_obtention_mois" name="universitaires_obtention_mois" disabled>
                                    <?php buildSelectNumbersElements(1, 12) ?>
                                </select><br>
                                <label for="universitaires_obtention_mois" class="police_11px">Mois (MM)</label>
                            </div>
                            <div class="text_centre">
                                <select id="universitaires_obtention_annee" name="universitaires_obtention_annee" disabled>
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="universitaires_obtention_annee" class="police_11px">Année (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                </table>
                <table class="tab_ajust_contenu grade_universitaire" style="display:none">
                    <tr>
                        <td>
                            <input id="universitaires_check_autre" name="universitaires_check_autre" type="checkbox">
                        </td>
                        <td>
                            <label for="universitaires_check_autre">Autre grade ou diplôme de niveau universitaire
                                entrepris
                                ou complété</label>
                        </td>
                    </tr>
                </table>
                <table id="grade_universitaire_autre" class="table_50" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="universitaires_nom_diplome_autre"
                                   name="universitaires_nom_diplome_autre" size="40"><br>
                            <label for="universitaires_nom_diplome_autre" class="police_11px">Nom du diplôme</label>
                        </td>
                        <td>
                            <input id="universitaires_radio_obtention_autre" name="universitaires_obtention_autre"
                                   type="radio"
                                   value="obtenu">
                            <label for="universitaires_radio_obtention_autre" class="police_11px">Obtenu</label><br>
                            <input id="universitaires_radio_a_obtenir_autre" name="universitaires_obtention_autre"
                                   type="radio"
                                   value="a_obtenir">
                            <label for="universitaires_radio_a_obtenir_autre" class="police_11px">À obtenir</label><br>
                            <input id="universitaires_radio_pas_obtenu_autre" name="universitaires_obtention_autre"
                                   type="radio"
                                   value="pas_termine">
                            <label for="universitaires_radio_pas_obtenu_autre" class="police_11px">Ne sera pas
                                obtenu</label>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <span>Période de fréquentation</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="universitaires_institution_autre"
                                   name="universitaires_institution_autre" size="40"><br>
                            <label for="universitaires_institution_autre" class="police_11px">
                                Institution où vous avez poursuivi vos études en vue de l'obtention<br>
                                de ce diplôme
                            </label>
                        </td>
                        <td class="text_centre">
                            <div>
                                <select id="universitaires_annee_debut_autre" name="universitaires_annee_debut_autre">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="universitaires_annee_debut_autre" class="police_11px">De (AAAA)</label>
                            </div>
                            <div class="text_centre">
                                <select id="universitaires_annee_fin_autre" name="universitaires_annee_fin_autre">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="universitaires_annee_fin_autre" class="police_11px">À (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <span>Date d'obtention</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="universitaires_discipline_autre"
                                   name="universitaires_discipline_autre" size="40"><br>
                            <label for="universitaires_discipline_autre" class="police_11px">Discipline ou
                                spécialisation</label>
                        </td>
                        <td>
                            <div class="text_centre">
                                <select id="universitaires_obtention_mois_autre" name="universitaires_obtention_mois_autre" disabled>
                                    <?php buildSelectNumbersElements(1, 12) ?>
                                </select><br>
                                <label for="universitaires_obtention_mois_autre" class="police_11px">Mois (MM)</label>
                            </div>
                            <div class="text_centre">
                                <select id="universitaires_obtention_annee_autre" name="universitaires_obtention_annee_autre" disabled>
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="universitaires_obtention_annee_autre" class="police_11px">Année
                                    (AAAA)</label>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>

            <!-- ########################################################################################### -->
            <!-- ############################### Section Emplois ########################################### -->
            <!-- ########################################################################################### -->

            <div id="div_formulaire_5_1" class="div_formulaire" style="display:none">
                <div id="div_erreur_5_1" style="display:none">
                    <div id="erreur_emploi_nom_employeur_1" class="erreur_5_1 div_erreur" style="display:none">*Veuillez spécifier le nom de l'employeur pour le premier emploi<br></div>
                    <div id="erreur_emploi_duree_de_mois_1" class="erreur_5_1 div_erreur" style="display:none">*Veuillez spécifier le mois du début pour le premier emploi<br></div>
                    <div id="erreur_emploi_duree_de_annee_1" class="erreur_5_1 div_erreur" style="display:none">*Veuillez spécifier l'année de début pour le premier emploi<br></div>
                    <div id="erreur_emploi_type_emploi_1" class="erreur_5_1 div_erreur" style="display:none">*Veuillez spécifier le type du premier emploi<br></div>
                    <div id="erreur_emploi_duree_a_mois_1" class="erreur_5_1 div_erreur" style="display:none">*Veuillez spécifier le mois de fin pour le premier emploi<br></div>
                    <div id="erreur_emploi_duree_a_annee_1" class="erreur_5_1 div_erreur" style="display:none">*Veuillez spécifier l'année de fin du premier emploi<br></div>
                    <div id="erreur_emploi_date_attestation_1" class="erreur_5_1 div_erreur" style="display:none">*Veuillez spécifier une date valide pour l'expédition de l'attestation du premier emploi<br></div>
                    <div id="erreur_emploi_duree_logic_1" class="erreur_5_1 div_erreur" style="display:none">*La période d'emploi doit commencer avant la fin<br></div>
                </div>
                <table class="table_50">
                    <tr class="sous_titre">
                        <td>
                            Renseignements sur les emplois
                        </td>
                    </tr>
                    <tr>
                        <td class="test_justifie">
                            <p>
                                Si cette section ne s'applique pas à votre cas, veuillez passer à la section suivante.
                            </p>

                            <p>
                                Veuillez indiquer les emplois que vous avez occupés en commençant par le plus récent.
                                Les expériences professionnelles et le bénévolat peuvent parfois être considérés aux
                                fins de
                                l’admission.
                            </p>

                            <p>
                                Il est essentiel de joindre les attestations des employeurs ou des responsables. En plus
                                de
                                confirmer la durée et la nature des emplois occupés, les attestations doivent contenir
                                une
                                brève description des fonctions ou des tâches accomplies. Le curriculum vitæ ne peut
                                d’aucune
                                manière être considéré comme une preuve d’emploi. L’absence d’attestation(s) peut
                                entraîner
                                le
                                refus d’admission.
                            </p>
                        </td>
                    </tr>
                </table>
                <table class="tab_ajust_contenu">
                    <tr>
                        <td>
                            <input id="emploi_check_emploi_1" name="emploi_check_emploi_1" type="checkbox">
                        </td>
                        <td>
                            <label for="emploi_check_emploi_1">Premier emploi</label>
                        </td>
                    </tr>
                </table>
                <table id="section_emploi_1" class="table_50" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="emploi_nom_employeur_1" name="emploi_nom_employeur_1" size="40"><br>
                            <label for="emploi_nom_employeur_1" class="police_11px">Nom de l'employeur</label>
                        </td>
                        <td>
                            <div>
                                <span class="police_11px">de</span>
                            </div>
                            <div>
                                <select id="emploi_duree_de_mois_1" name="emploi_duree_de_mois_1">
                                    <?php buildSelectNumbersElements(1, 12) ?>
                                </select><br>
                                <label for="emploi_duree_de_mois_1" class="police_11px">Mois</label>
                            </div>
                            <div>
                                <select id="emploi_duree_de_annee_1" name="emploi_duree_de_annee_1">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="emploi_duree_de_annee_1" class="police_11px">Année</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="emploi_type_emploi_1" name="emploi_type_emploi_1" size="40"><br>
                            <label for="emploi_type_emploi_1" class="police_11px">Type d'emploi</label>
                        </td>
                        <td>
                            <div>
                                <span class="police_11px">à</span>
                            </div>
                            <div>
                                <select id="emploi_duree_a_mois_1" name="emploi_duree_a_mois_1">
                                    <?php buildSelectNumbersElements(1, 12); ?>
                                </select><br>
                                <label for="emploi_duree_a_mois_1" class="police_11px">Mois</label>
                            </div>
                            <div>
                                <select id="emploi_duree_a_annee_1" name="emploi_duree_a_annee_1">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="emploi_duree_a_annee_1" class="police_11px">Année</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <div>
                                <input type="text" id="emploi_date_attestation_1" name="emploi_date_attestation_1"><br>
                                <label for="emploi_date_attestation_1" class="police_11px">Date d'expédition de
                                    l'attestation prévue</label>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>

            <div id="div_formulaire_5_2" class="div_formulaire" style="display:none">
                <div id="div_erreur_5_2" style="display:none">
                    <div id="erreur_emploi_nom_employeur_2" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le nom de l'employeur pour le deuxième emploi<br></div>
                    <div id="erreur_emploi_duree_de_mois_2" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le mois du début pour le deuxième emploi<br></div>
                    <div id="erreur_emploi_duree_de_annee_2" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier l'année de début pour le deuxième emploi<br></div>
                    <div id="erreur_emploi_type_emploi_2" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le type du deuxième emploi<br></div>
                    <div id="erreur_emploi_duree_a_mois_2" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le mois de fin pour le deuxième emploi<br></div>
                    <div id="erreur_emploi_duree_a_annee_2" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier l'année de fin du deuxième emploi<br></div>
                    <div id="erreur_emploi_date_attestation_2" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier une date valide pour l'expédition de l'attestation du deuxième emploi<br></div>
                    <div id="erreur_emploi_duree_logic_2" class="erreur_5_1 div_erreur" style="display:none">*La période d'emploi du premier choix doit commencer avant la fin<br></div>


                    <div id="erreur_emploi_nom_employeur_3" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le nom de l'employeur pour le troisième emploi<br></div>
                    <div id="erreur_emploi_duree_de_mois_3" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le mois du début pour le troisième emploi<br></div>
                    <div id="erreur_emploi_duree_de_annee_3" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier l'année de début pour le troisième emploi<br></div>
                    <div id="erreur_emploi_type_emploi_3" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le type du troisième emploi<br></div>
                    <div id="erreur_emploi_duree_a_mois_3" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier le mois de fin pour le troisième emploi<br></div>
                    <div id="erreur_emploi_duree_a_annee_3" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier l'année de fin du troisième emploi<br></div>
                    <div id="erreur_emploi_date_attestation_3" class="erreur_5_2 div_erreur" style="display:none">*Veuillez spécifier une date valide pour l'expédition de l'attestation du troisième emploi<br></div>
                    <div id="erreur_emploi_duree_logic_3" class="erreur_5_1 div_erreur" style="display:none">*La période d'emploi du deuxième choix doit commencer avant la fin<br></div>
                </div>
                <table class="tab_ajust_contenu">
                    <tr>
                        <td>
                            <input id="emploi_check_emploi_2" name="emploi_check_emploi_2" type="checkbox">
                        </td>
                        <td>
                            <label for="emploi_check_emploi_2">Deuxième emploi</label>
                        </td>
                    </tr>
                </table>
                <table id="section_emploi_2" class="table_50" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="emploi_nom_employeur_2" name="emploi_nom_employeur_2" size="40"><br>
                            <label for="emploi_nom_employeur_2" class="police_11px">Nom de l'employeur</label>
                        </td>
                        <td>
                            <div>
                                <span class="police_11px">de</span>
                            </div>
                            <div>
                                <select id="emploi_duree_de_mois_2" name="emploi_duree_de_mois_2">
                                    <?php buildSelectNumbersElements(1, 12); ?>
                                </select><br>
                                <label for="emploi_duree_de_mois_2" class="police_11px">Mois</label>
                            </div>
                            <div>
                                <select id="emploi_duree_de_annee_2" name="emploi_duree_de_annee_2">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="emploi_duree_de_annee_2" class="police_11px">Année</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="emploi_type_emploi_2" name="emploi_type_emploi_2" size="40"><br>
                            <label for="emploi_type_emploi_2" class="police_11px">Type d'emploi</label>
                        </td>
                        <td>
                            <div>
                                <span class="police_11px">à</span>
                            </div>
                            <div>
                                <select id="emploi_duree_a_mois_2" name="emploi_duree_a_mois_2">
                                    <?php buildSelectNumbersElements(1, 12); ?>
                                </select><br>
                                <label for="emploi_duree_a_mois_2" class="police_11px">Mois</label>
                            </div>
                            <div>
                                <select id="emploi_duree_a_annee_2" name="emploi_duree_a_annee_2">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="emploi_duree_a_annee_2" class="police_11px">Année</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <div>
                                <input type="text" id="emploi_date_attestation_2" name="emploi_date_attestation_2"><br>
                                <label for="emploi_date_attestation_2" class="police_11px">Date d'expédition de
                                    l'attestation prévue</label>
                            </div>
                        </td>
                    </tr>
                </table>
                <table id="section_emploi_2_1" class="tab_ajust_contenu" style="display:none">
                    <tr>
                        <td>
                            <input id="emploi_check_emploi_3" name="emploi_check_emploi_3" type="checkbox">
                        </td>
                        <td>
                            <label for="emploi_check_emploi_3">Troisième emploi</label>
                        </td>
                    </tr>
                </table>
                <table id="section_emploi_3" class="table_50" style="display:none">
                    <tr>
                        <td>
                            <input type="text" id="emploi_nom_employeur_3" name="emploi_nom_employeur_3" size="40"><br>
                            <label for="emploi_nom_employeur_3" class="police_11px">Nom de l'employeur</label>
                        </td>
                        <td>
                            <div>
                                <span class="police_11px">de</span>
                            </div>
                            <div>
                                <select id="emploi_duree_de_mois_3" name="emploi_duree_de_mois_3">
                                    <?php buildSelectNumbersElements(1, 12); ?>
                                </select><br>
                                <label for="emploi_duree_de_mois_3" class="police_11px">Mois</label>
                            </div>
                            <div>
                                <select id="emploi_duree_de_annee_3" name="emploi_duree_de_annee_3">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="emploi_duree_de_annee_3" class="police_11px">Année</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" id="emploi_type_emploi_3" name="emploi_type_emploi_3" size="40"><br>
                            <label for="emploi_type_emploi_3" class="police_11px">Type d'emploi</label>
                        </td>
                        <td>
                            <div>
                                <span class="police_11px">à</span>
                            </div>
                            <div>
                                <select id="emploi_duree_a_mois_3" name="emploi_duree_a_mois_3">
                                    <?php buildSelectNumbersElements(1, 12); ?>
                                </select><br>
                                <label for="emploi_duree_a_mois_3" class="police_11px">Mois</label>
                            </div>
                            <div>
                                <select id="emploi_duree_a_annee_3" name="emploi_duree_a_annee_3">
                                    <?php buildSelectNumbersElements(MIN_COMBOBOX_YEAR, MAX_COMBOBOX_YEAR); ?>
                                </select><br>
                                <label for="emploi_duree_a_annee_3" class="police_11px">Année</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <div>
                                <input type="text" id="emploi_date_attestation_3" name="emploi_date_attestation_3"><br>
                                <label for="emploi_date_attestation_3" class="police_11px">Date d'expédition de
                                    l'attestation prévue</label>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>

            <!-- ########################################################################################### -->
            <!-- ############################### Section Supplémentaires ################################### -->
            <!-- ########################################################################################### -->

            <div id="div_formulaire_6_1" class="div_formulaire" style="display:none">
                <table class="table_50">
                    <tr class="sous_titre">
                        <td>
                            Renseignements supplémentaires
                        </td>
                    </tr>
                    <tr>
                        <td class="test_justifie">
                            <p>
                                Veuillez indiquer toute autre expérience, différente d’un emploi, qui vous semble
                                pertinente à votre demande d’admission.
                                Il peut s’agir de publications, de recherches, de contributions intellectuelles ou
                                professionnelles.
                            </p>
                        </td>
                    </tr>
                </table>
                <textarea id="supplement_text" name="supplement_text"></textarea>
            </div>

            <div id="div_formulaire_7_1" class="div_formulaire" style="display:none">
                <div id="div_erreur_7_1" style="display:none">
                    <div id="erreur_supplement_accept_1" class="erreur_7_1 div_erreur" style="display:none">*Veuillez accepter d'avoir pris connaissance<br></div>
                    <div id="erreur_supplement_accept_2" class="erreur_7_1 div_erreur" style="display:none">*Veuillez accepter le partage d'informations par l'UQAM<br></div>
                </div>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <p class="police_rouge test_justifie">
                                J’ai pris connaissance des renseignements concernant la Loi sur
                                l’accès aux
                                documents des organismes publics et sur la
                                protection des renseignements personnels. Je consens à ce que l’UQAM transmette aux
                                parties énumérées dans les instructions
                                d’admission les informations qui y sont décrites.
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="supplement_accept_1">J'accepte</label>
                        </td>
                        <td>
                            <select id="supplement_accept_1" name="supplement_accept_1">
                                <option value="">--svp choisir--</option>
                                <option value="oui">oui</option>
                                <option value="non">non</option>
                            </select>
                        </td>
                    </tr>
                </table>
                <table class="table_50">
                    <tr>
                        <td colspan="2">
                            <p class="police_rouge test_justifie">
                                J’autorise les établissements d’enseignement collégial que j’ai fréquentés, ainsi que le
                                ministère de l’Enseignement supérieur, de la
                                Recherche et de la Science (MESRS) à communiquer à l’UQAM, par l’entremise du Bureau de
                                coopération interuniversitaire (BCI),
                                les relevés de notes nécessaires à l’évaluation de mon dossier. J’autorise, en tout
                                temps, les établissements d’enseignement que
                                j’ai fréquentés, au Québec ou ailleurs, à transmettre à l’UQAM, copie officielle des
                                documents nécessaires à l’évaluation de mon
                                dossier en vue d’une admission, d’une inscription ou d’une reconnaissance d’acquis, ou
                                de tout autre document versé à mon
                                dossier à ces fins et ce, même si les documents qui ont déjà été déposés à mon dossier
                                étaient des originaux.
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <p class="police_rouge test_justifie">
                                J’autorise l’UQAM à transmettre au BCI les renseignements nécessaires à la gestion des
                                admissions et à la production de statistiques
                                qui pourraient requérir le couplage des fichiers d’établissements. En vertu d’une
                                entente autorisée par la Commission d’accès
                                à l’information, les renseignements nécessaires à la création et à la validation du code
                                permanent seront transmis au MESRS;
                                j’autorise l’UQAM à obtenir du MESRS ces renseignements. J’autorise aussi que les
                                renseignements nécessaires à la gestion des
                                admissions relatifs à l’établissement fréquenté, et ceux sur la citoyenneté pour établir
                                mes droits de scolarité, puissent faire l’objet
                                d’une validation auprès du MESRS. J’autorise également le ministère de l’Immigration, de
                                la Diversité et de l’Inclusion (MIDI) à
                                transmettre à l’UQAM la confirmation de l’émission, le cas échéant, d’un Certificat
                                d’acceptation du Québec (CAQ) à mon nom.
                                Je déclare que les renseignements donnés dans ce formulaire sont exacts et je m’engage à
                                respecter les règlements de l’UQAM .
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="supplement_accept_2">J'accepte</label>
                        </td>
                        <td>
                            <select id="supplement_accept_2" name="supplement_accept_2">
                                <option value="">--svp choisir--</option>
                                <option value="oui">oui</option>
                                <option value="non">non</option>
                            </select>
                        </td>
                    </tr>
                </table>
            </div>

        </div>
    </form>
</div>
<footer>
    <h6>
        GUILLAUME GAGNON - DANY DEROY - 2015 TP3 INF2005 PROGRAMMATION WEB
    </h6>
</footer>
</body>
</html>
