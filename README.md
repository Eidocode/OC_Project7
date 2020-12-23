# Créez GrandPy Bot, le papy-robot 🤖 👴

*Parcours développeur d'application Python : OpenClassrooms Projet n°7* 

### Sujet du projet

Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴

Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?

## Structure du projet

Pour la mise en place de ce projet, il était demandé de créer une page **HTML** permettant à l'utilisateur d'interagir avec le bot, ainsi qu'une application **Flask** (**Framework Python**) chargée de toute la partie "traitement". Pour faire la jonction entre l'application et la page **HTML**, nous utilisons un script **JavaScript** composé de **JQuery** ainsi que de requêtes **Ajax**.

### Déroulement de l'application

Lors de l'ouverture de l'application, l'utilisateur se retrouve face à une fenêtre de "chat", dans laquelle **GrandPy Bot** nous accueille. L'utilisateur est alors invité à poser une question par le biais d'un champ de saisie.
Lorsque l'utilisateur a posé sa question, celle-ci est envoyée par le biais d'une requête **POST**. La vue de notre application (<a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/views.py">*views.py*</a>) se charge alors de récupérer le contenu de cette requête (en l'occurrence la chaine de caractères envoyée par l'utilisateur).
A ce moment, l'application **Flask** prend le relai, et se charge de traiter les informations reçues. 

- **Parser** (<a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/bot/parser.py">*parser.py*</a>)
Le **parser**, qui est la première fonctionnalité de notre application, se charge de traiter la chaîne de caractères puis de retourner uniquement les mots qu'elle juge important. Pour cela, elle s'appuie sur une liste de "**Stop words**" (<a href=https://github.com/Eidocode/OC_Project7/blob/main/grandpy/bot/final_stop_words.fic>*final_stop_words.fic*</a>) contenant des mots jugés inutiles dans une phrase et permettant d'aider **GrandPy Bot** à la compréhension de celle-ci.
Une fois la ponctuation et les mots jugés superflus supprimés, le **Parser** retourne à la vue une liste des mots restants.

- **WikiAPI** (<a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/bot/wiki_api.py">*wiki_api.py*</a>)
La deuxième fonctionnalité qui consiste à communiquer avec l'**API Wikipedia** est ensuite utilisée. Les informations renvoyées par le **Parser** sont alors envoyées à l'**API Wikipedia**.
Wikipedia renvoi alors une liste de résultat à notre recherche. Un élément de la liste est sélectionné puis nous renvoyons à la vue les informations Wikipedia composées du **sommaire** de la page, de son **URL** ainsi que son **titre**.

- **GmapsAPI** (<a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/bot/gmaps_api.py">*gmaps_api.py*</a>)
La fonctionnalité suivante permet de communiquer directement avec l'**API Googlemaps**. De la même façon que la fonctionnalité précédente, les informations "**parsées**" sont envoyées à l'**API Googlemaps**.
Googlemaps retourne alors les coordonnées (**latitude** + **longitude**) ainsi que l'adresse postale de la recherche.

Une fois toutes les données récupérées, un traitement de celles-ci est effectuée dans <a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/views.py">*views.py*</a>. On vérifie que les API n'ont pas renvoyé une erreur, puis on construit le message de réponse du bot. La réponse se fait par le biais de deux messages, un premier composé d'une phrase aléatoire (déterminée par la fonction **get_answer**) ainsi que l'adresse postale retournée précédemment par l'**API Googlemaps**. Le deuxième message contient le sommaire retourné par l'**API Wikipédia**, ainsi que la carte Googlemaps.
On retourne alors le résultat de ce traitement au format **JSON**, qui sera ensuite exploité par le script **JavaScript** pour afficher les différents éléments dans la fenêtre de chat de l'utilisateur.

## Installation du projet

Pour mettre en place le projet il est recommandé de créer un **environnement virtuel python**. Les commandes ci-dessous sont à adapter selon le système d'exploitation. Il faut également avoir préalablement installé les dépendances éventuellement nécessaires.
***A savoir que le projet a été testé sur des versions 3.6 et 3.7 de Python. Il est donc recommandé de créer un environnement virtuel basé sur une version compatible.***

 1. **Installation de l'environnement virtuel** :

		Python -m venv (nom_environnement)
	
 2. **Clone du projet à l'intérieur de l'environnement virtuel** :

		Git clone git@github.com:Eidocode/OC_Project7.git

 3.  **Activation de l'environnement virtuel (à adapter selon l'OS)** :

		./Scripts/activate

 4. **Installation des dépendances (à adapter selon l'OS)** :
 
		pip install -r requirements.txt

 5. **Configuration de l'application** :

	 Le projet ne peut pas fonctionner si les variables renseignées dans le <a href="https://github.com/Eidocode/OC_Project7/blob/main/config.py">*config.py*</a> restent vides. Ce fichier contient deux variables nommées **SECRET_KEY** et **GMAPS_APP_ID**. La variable **SECRET_KEY** doit être généré aléatoirement une fois est liée uniquement au projet en cours. Il est donc indispensable de ne pas la diffuser une fois générée. Il est possible de le faire (depuis une console **Python**) de la façon suivante :

		>>> import random, string
		>>> "".join([random.choice(string.printable) for _ in range(24)])

	Il suffira alors de copier la chaîne de caractères générée dans le fichier <a href="https://github.com/Eidocode/OC_Project7/blob/main/config.py">*config.py*</a>.
	Concernant la variable **GMAPS_APP_ID**, celle-ci est en fait un **token** délivré par google pour pouvoir utiliser les **API**. De la même manière que la variable **SECRET_KEY** celle-ci doit rester secrète et liée uniquement à une instance du projet. Pour la créer, il est nécessaire de créer un compte sur **Google Cloud Platform**, voici un tutoriel détaillant les différentes étapes nécessaires à l'obtention de ce **Token** --> *https://developers.google.com/maps/gmp-get-started*
	Une fois la clé obtenue, il faudra la renseigner dans le fichier <a href="https://github.com/Eidocode/OC_Project7/blob/main/config.py">*config.py*</a>

 6. **Exécution de l'environnement Flask (à adapter selon l'OS)** :

		$env:FLASK_APP="run.py"
		flask run

	L'application **Flask** est alors exécutée, il ne reste plus qu'à ouvrir un navigateur et se rendre à l'adresse **127.0.0.1:5000** ou **localhost:5000**

## Déploiement de l'application

Dans le cas de ce projet, l'application a été déployée sur **Heroku**, nous pouvons la retrouver à l'adresse suivante : *https://radiant-citadel-84173.herokuapp.com/*.

Pour effectuer ce déploiement, il suffit de suivre, simplement, la documentation fournit à ce sujet. Elle est consultable à l'adresse suivante : *https://devcenter.heroku.com/articles/getting-started-with-python*.

A savoir que lors du déploiement, nous ne renseignons pas les variables contenus dans le <a href="https://github.com/Eidocode/OC_Project7/blob/main/config.py">*config.py*</a> directement dans celui-ci. En effet, **Heroku** utilise pour ce genre d'information des variables d'environnement, nommées ici **Config Vars**. C'est ce que l'on utilisera pour déclarer les variables **SECRET_KEY** et **GMAP_APP_ID**.
Il suffit alors de déclarer les variables (dans l'environnement **Heroku**) de la façon suivante : 
***A savoir qu'il est également possible de le faire depuis le dashboard du projet***

		heroku config:set SEC_KEY=(valeur de la variable)
		heroku config:set GMAP_TOKEN=(valeur de la variable)

Reste ensuite à appeler ces variables d'environnement dans le fichier <a href="https://github.com/Eidocode/OC_Project7/blob/main/config.py">*config.py*</a> de l'application destinée à être déployé sur **Heroku**.

		import os
		
		SECRET_KEY = os.environ.get('SEC_KEY')
		GMAPS_APP_ID = os.environ.get('GMAP_TOKEN')


## Utilisation de l'application

L'application **GrandPy** est un simple BOT qui ne peut fonctionner uniquement lorsqu'elle est capable d'isoler un lieu existant du reste de la phrase. De façon à soumettre le reste de la phrase aux **API Wikipedia** et **Googlemaps**. Cela veut dire que si on lui demande autre chose que des renseignements sur un lieu, il y a de fortes chances qu'il nous demande de reposer la question différemment. Une tournure de phrase change beaucoup de chose, donc il ne faut pas hésiter à reformuler. 
		
Voici des phrases qui fonctionnent : 

 - *Bonjour GrandPy, peux-tu me donner des informations sur la tour eiffel ?*
 - *Hey GrandPy, comment vas-tu ? Connais-tu la cathédrale d'Amiens ?*
 - *GrandPy, parle moi de la muraille de Chine*

Une fonctionnalité (externe) à l'application, dans le répertoire nommé <a href="https://github.com/Eidocode/OC_Project7/tree/main/stop_words">*stop_words*</a> à la racine du projet, est disponible. Elle permet d'ajouter, par le biais d'un menu, des nouveaux mots qui seront directement ajoutés au fichier <a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/bot/final_stop_words.fic">*final_stop_words.fic*</a> (en vérifiant préalablement la présence du mot dans le fichier). Il est également possible de vérifier uniquement qu'un mot existe déjà ou pas dans le fichier. Cela permettra de filtrer, à l'avenir, plus de mots par notre Bot, et donc, d'améliorer sa compréhension des questions posées par les utilisateurs. 

## Tests unitaires et fonctionnels

Des tests unitaires et fonctionnels sont disponibles dans le répertoire <a href="https://github.com/Eidocode/OC_Project7/tree/main/grandpy/tests">*tests*</a> de l'application. Les tests unitaires se trouvent dans le répertoire enfant <a href="https://github.com/Eidocode/OC_Project7/tree/main/grandpy/tests/unit">*unit*</a>, voici le détail des fichiers :
	
 - <a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/tests/unit/test_gmapapi.py">*test_gmapapi.py*</a> :  *Test unitaire de la classe **GmapsAPI***
 - <a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/tests/unit/test_parser.py">*test_parser.py*</a> : *Test unitaire de la classe **Parser** utilisée dans l'application*
 - <a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/tests/unit/test_stopwords.py">*test_stopwords.py*</a> : *Test unitaire de la fonction **get_stop_words***
 - <a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/tests/unit/test_wikiapi.py">*test_wikiapi.py*</a> : *Test unitaire de la classe **WikiAPI***

Un test fonctionnel nommé <a href="https://github.com/Eidocode/OC_Project7/blob/main/grandpy/tests/test_views.py">*test_views.py*</a> est également disponible à la racine du répertoire <a href="https://github.com/Eidocode/OC_Project7/tree/main/grandpy/tests">*tests*</a>. Il permet notamment de tester le processus qui se déroule lors de la soumission de l'input par un utilisateur. De façon à vérifier que toutes les fonctionnalités s'échangent correctement les informations.

## Bugs connus

Voici la liste des bugs connus aujourd'hui et qui ne sont pas résolus à ce jour. La liste évoluera selon la découverte de nouveaux bugs ou des remontées faites par les utilisateurs.

 - **Mozilla Firefox** : Ce navigateur est aujourd'hui inutilisable avec l'application. Si la page d'accueil et le chat s'affichent correctement au départ, une erreur se produit lors de la soumission de l'input par l'utilisateur. En effet, le navigateur semble doubler les requêtes et donc ici la requête **POST**... Ce qui a pour effet de retourner une seconde requête vide. Une erreur se produit alors puisque l'application demande le retour de l'entrée "**message**" qui n'existe plus dans cette seconde requête.
	Après quelques recherches, ce bug semble connu. Notamment lorsqu'il s'agit d'une application **Flask**.
	Je n'ai pas noté, à ce jour, un phénomène équivalent dans les autres navigateurs. Voici ceux qui ont été testés et qui fonctionnent : 
	
	 - [X] *Google Chrome*
	 - [X] *Chromium*
	 - [X] *Safari (**iOS**)*
	 - [X] *Safari (**MacOS, etc...**)*
	 - [X] *Edge*
	 - [X] *Opera*
