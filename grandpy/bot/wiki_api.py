import wikipedia


class WikiAPI:
    def __init__(self):
        wikipedia.set_lang("fr")

    def get_search_result(self, string):
        print('[WIKIAPI] : ' + string)
        try:
            search = wikipedia.search(string)

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
