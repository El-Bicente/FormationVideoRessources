#coding:utf-8
"""
+------------------------------------------------------+
| Vérification d'un format de donnée suivant une REGEX |
| Syntaxe : Perl                                       |
+------------------------------------------------------+
"""
import re

data = "game/the-legend-of-zelda/8"
regex = r"^game\/[a-z0-9-_]+\/[0-9]+$"

if re.search(regex, data, re.IGNORECASE) is not None:
	print("OUI")
else:
	print("NON")