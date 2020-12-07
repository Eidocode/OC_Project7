import urllib.request

from grandpy.bot.parser import Parser
from grandpy.bot.wiki_api import WikiAPI
from grandpy.bot.gmaps_api import GmapsAPI
from config import GMAPS_APP_ID
from grandpy.bot.stop_words import get_stop_words

# - View :
#   - accéder à la route /, /index
def test_route1():
    url = "http://127.0.0.1:5000/"
    status_code = urllib.request.urlopen(url).getcode()
    assert status_code == 200


def test_route2():
    url = "http://127.0.0.1:5000/index/"
    status_code = urllib.request.urlopen(url).getcode()
    assert status_code == 200

# - Stop words:
#   - Vérifier l'existance de mots dans la liste stop words
def test_stopwords():
    stop_words = get_stop_words('./grandpy/bot/final_stop_words.fic')
    test_list = ('auxquelles', 'bravo', 'desquelles', 'particulièrement', 'souhait')
    for word in test_list:
        assert word in stop_words


# - Parsing :
class TestParser:
    #   - Instancier Parser()
    parser = Parser()
    assert isinstance(parser, Parser)

    #   - Envoyer une phrase au parser et récupérer le résultat
    def test_parser(self):
        test_input = "Bonjour, je avoir des informations sur la tour eiffel ?"
        test_result = self.parser.get_keywords(test_input)
        assert test_result == ['tour', 'eiffel']


# - Wikipedia
class TestWikipedia:
    #   - Instancier WikiAPI()
    wiki = WikiAPI()
    assert isinstance(wiki, WikiAPI)

    #   - Envoyer une chaine de caractère à traiter et récupérer l'URL de la page
    def test_wiki_url(self):
        self.wiki.get_search_result('tour eiffel')
        assert self.wiki.page.url == 'https://fr.wikipedia.org/wiki/Tour_Eiffel'

    #   - Récupérer le titre de la page Wikipedia
    def test_wiki_api(self):
        self.wiki.get_search_result('tour eiffel')
        assert self.wiki.page.title == 'Tour Eiffel'

    #   - Envoyer une chaine intraitable (doit retourner une erreur)
    def test_wiki_error(self):
        test = self.wiki.get_search_result('fdsfs')
        assert test == 'error'


# - API GoogleMaps
class TestGmaps:
    #   - Instancier GmapsAPI()
    gmap = GmapsAPI(GMAPS_APP_ID)
    assert isinstance(gmap, GmapsAPI)

    #   - Envoyer une chaine de caractère à traiter et récupérer l'adresse du lieu
    def test_gmaps_address(self):
        addr = self.gmap.get_address('tour eiffel')
        assert addr == 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France'

    #   - Récupérer la latitude et longitude
    def test_gmaps_coord(self):
        coord = self.gmap.get_coordinates('tour eiffel')
        assert coord == {'lat': 48.85837009999999, 'lng': 2.2944813}

    #   - Envoyer une chaine intraitable (doit retourner une erreur)
    def test_gmaps_error(self):
        coord = self.gmap.get_coordinates('fdslmfdsm')
        assert coord == 'error'
