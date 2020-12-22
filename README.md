# Créez GrandPy Bot, le papy-robot 🤖 👴

### Sujet du projet

Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴

Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?

## Structure du projet

Pour la mise en place de ce projet, il était demandé de créer une page HTML permettant à l'utilisateur d'interagir avec le bot, ainsi qu'une application Flask (Framework Python) chargée de toute la partie "traitement". Pour faire la jonction entre l'application et la page HTML, nous utilisons un script JavaScript composé de JQuery ainsi que de requêtes Ajax.

### Déroulement de l'application
Lors de l'ouverture de l'application, l'utilisateur se retrouve face à une fenêtre de "chat", dans laquelle GrandPy Bot nous accueille. L'utilisateur est alors invité à poser une question par le biais d'un champ de saisie.
Lorsque l'utilisateur a posé sa question, celle-ci est envoyée par le biais d'une requête POST. La vue de notre application (views.py) se charge alors de récupérer le contenu de cette requête (en l'occurrence la chaine de caractères envoyée par l'utilisateur).
A ce moment, l'application Flask prend le relai, et se charge de traiter les informations reçues. 

- **Parser (parser.py)**
Le parser, qui est la première fonctionnalité de notre application, se charge de traiter la chaîne de caractères puis de retourner uniquement les mots qu'elle juge important. Pour cela, elle s'appuie sur une liste de "Stop words" (final_stop_words.fic) contenant des mots jugés inutiles dans une phrase et permettant d'aider notre GrandPy Bot à la compréhension de celle-ci.
Une fois la ponctuation et les mots jugés superflus supprimés, le Parser retourne à la vue une liste de mots restants.

- **WikiAPI**
La deuxième fonctionnalité qui consiste à communiquer avec l'API Wikipedia (wiki_api.py) est ensuite utilisée. Les informations renvoyées par le Parser sont alors envoyées à l'API Wikipedia.
Wikipedia renvoi alors une liste de résultat à notre recherche. Un élément de la liste est sélectionné puis nous renvoyons à la vue les informations Wikipedia composées du "Sommaire" de la page, de son URL ainsi que son titre.

- **GmapsAPI**
La fonctionnalité suivante permet de communiquer directement avec l'API Googlemaps (gmaps_api.py).
