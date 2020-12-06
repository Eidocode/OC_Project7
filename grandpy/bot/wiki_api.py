import wikipedia
import requests


class WikiAPI:
    def __init__(self):
        wikipedia.set_lang("fr")
        self.page = None

    def get_search_result(self, string):
        print('[WIKIAPI] : ' + string)
        try:
            search = wikipedia.search(string)
            self.page = wikipedia.page(search[0])
            result = wikipedia.summary(search[0])
        except wikipedia.exceptions.WikipediaException:
            print('Une erreur est survenue')
            result = 'error'
        except IndexError:
            print('Index introuvable')
            result = 'error'

        return result
