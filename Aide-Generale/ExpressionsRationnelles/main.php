<?php
/*
+------------------------------------------------------+
| Vérification d'un format de donnée suivant une REGEX |
| Syntaxe : PCRE (Perl)                                |
+------------------------------------------------------+
*/

$data = 'game/the-legend-of-zelda/8';
$regex = '#game\/[a-zA-Z0-9-_]+\/[0-9]+#';

if(preg_match($regex, $data))
	echo 'OUI';
else
	echo 'NON';