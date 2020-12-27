                                *******************************************
                                ******                               ******
                                **       Fonctionnalité Stop_Words       **
                                **           pour GrandPy Bot	         **
                                *****                                 *****
                                *******************************************

-----------------
-- Utilisation --
-----------------

Cette fonctionnalité est permet l'ajout ou la recherche de stop_words dans le fichier nommé "final_stop_words.fic"
utilisé par l'application GrandPy Bot.

Pour utiliser ce programme, executer simplement la commande suivante :

	Python.exe stop_words.py


-----------------
-- Description --
-----------------

Un menu s'affiche alors proposant différentes options. La première permet d'ajouter un nouveau mot dans la liste de
stop words, en vérifiant préalablement son existence.

La deuxième option permet de comparer le contenu des fichiers .txt éventuellement présents dans le sous dossier
.\stop_words\. Si ces fichiers contiennent des mots qui n'apparaissent pas dans le fichier final_stop_words.fic, ils
seront alors ajoutés. Cela permet d'ajouter plusieurs mots en une fois.

La dernière option permet de consulter l'existence éventuelle d'un mot dans le fichier final utilisé par l'application.
