import pytest
import requests

from flask import current_app

from grandpy.views import app

from grandpy.bot.parser import Parser
from grandpy.bot.wiki_api import WikiAPI
from grandpy.bot.gmaps_api import GmapsAPI
from config import GMAPS_APP_ID


parser = Parser()
wiki = WikiAPI()
gmap = GmapsAPI(GMAPS_APP_ID)

get_message = None


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"
        yield client


def test_index(client):
    res = client.get('/')
    res2 = client.get('/index/')
    assert res.status_code == 200
    assert res2.status_code == 200


def test_set_post(client):
    global get_message
    url = 'http://127.0.0.1:5000/process'
    question = { 'message': 'Bonjour, je veux des informations sur la tour Eiffel ?' }
    res = requests.post(url, data=question)
    get_message = question['message']
    assert res.status_code == 200


def test_process(client, monkeypatch):
    valid_answer = "Ah oui, je vois tout à fait ce dont tu veux parler. L'adresse est "
    error_answer = "Désolé mon grand, mais je ne comprends pas ta demande... "

    wiki_response = {
        'summary': 'Tour de fer puddlé de 324 mètres de hauteur',
        'url': 'https://fr.wikipedia.org/wiki/Tour_Eiffel',
        'title': 'Tour Eiffel'
    }

    gmap_response = [
        {
            "formatted_address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
            "geometry": {
                "location": {
                    "lat": 48.85837009999999,
                    "lng": 2.2944813
                }
            }
        }
    ]

    def mock_wiki(string):
        return wiki_response

    def mock_gmap(string):
        return gmap_response

    monkeypatch.setattr(wiki, 'get_search_result', mock_wiki)
    monkeypatch.setattr(gmap, 'get_informations', mock_gmap)

    parsed_message = ' '.join(parser.get_keywords(get_message))
    assert parsed_message == 'tour eiffel'

    wiki_result = wiki.get_search_result(parsed_message)
    assert not wiki_result == 'error'

    gmap_result = gmap.get_coordinates(parsed_message)
    assert not gmap_result == 'error'

    if wiki_result == 'error':
        first_message = error_answer
        second_message = None
        coord = None
        url = None
        title = None
    else:
        coord = gmap_result['coord']
        addr = gmap_result['addr']
        first_message = valid_answer + addr
        second_message = wiki_result['summary']
        url = wiki_result['url']
        title = wiki_result['title']

    res = {
        "first_message": first_message,
        "second_message": second_message,
        "gmap_coord": coord,
        "url": url,
        "title": title
    }

    assert res["first_message"] == valid_answer + gmap_response[0]["formatted_address"]
    assert res["second_message"] == wiki_response["summary"]
    assert res["gmap_coord"] == gmap_response[0]["geometry"]["location"]
    assert res["url"] == wiki_response["url"]
    assert res["title"] == wiki_response["title"]
