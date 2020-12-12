import urllib.request

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


def test_stopwords():
    # Call get_stop_words function
    stop_words = get_stop_words('./grandpy/bot/final_stop_words.fic')

    # Vérifier l'existance de mots dans la liste stop words
    test_list = ('auxquelles', 'bravo', 'desquelles', 'particulièrement', 'souhait')
    for word in test_list:
        assert word in stop_words
