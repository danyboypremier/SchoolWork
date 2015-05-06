<?php

function display_results($errMsgList) {
    display_HTML_top();
    
    if (!empty($errMsgList)) {
        echo "<h2>Erreur! Le formulaire reçu n'est pas valide...</h2>";
        display_ErrMsgList($errMsgList);
    } else {
        echo "<h2>Votre inscription a bien été reçue. Bonne chance!</h2>";
    }

    display_HTML_bottom();
}


function display_HTML_top() {
    echo "<!DOCTYPE html><html>";
    echo '<head><meta charset="utf-8">';
    echo "<title>Demande d'admission - UQAM</title>";
    echo '<link href="CSS/formulaire.css" rel="stylesheet" type="text/css">';
    echo "<body><header><br>";
    echo "<h1>Demande d'admission UQAM</h1>";
    echo '<br><hr></header><div id="resultatcentre"><div id="resultat">';
}

function display_ErrMsgList($errMsgList) {
    echo "<p>Voici la liste des erreurs rencontrées:</p>";
    echo "<ul>";
    foreach ($errMsgList as $errMsg) {
        echo "<li>". $errMsg ."</li>";
    }
    echo "</ul>";
}

function display_HTML_bottom() {
    echo "</div></div><footer>";
    echo "<h6>GUILLAUME GAGNON - DANY DEROY - 2015 TP3 INF2005 PROGRAMMATION WEB</h6>";
    echo "</footer></body></html>";
}
