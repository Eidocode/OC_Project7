import wikipedia


class WikiAPI:
    def __init__(self):
        wikipedia.set_lang("fr")

    def search(self, string):
        return wikipedia.search(string)

    def get_search_result(self, string):
        print('[WIKIAPI] : ' + string)
        try:
            search = self.search(string)
            page = wikipedia.page(search[0])

            result = {
                'summary': page.summary,
                'url': page.url,
                'title': page.title
            }
        except wikipedia.exceptions.WikipediaException:
            print('Une erreur est survenue')
            result = 'error'
        except IndexError:
            print('Index introuvable')
            result = 'error'

        return result
