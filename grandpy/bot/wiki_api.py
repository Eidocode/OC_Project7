import wikipedia


class WikiAPI:
    """
    Class used to communicate with Wikipedia API

    ...

    Methods
    -------
    search(string)
        Returns wikipedia search titles (string)

    get_search_result(string)
        Returns the summary, url and title of the wikipedia search based on
        "search" method result.
        If Wikipedia encounters en error, the string 'error' is returned.
    """

    def __init__(self):
        # Sets Wikipedia language
        wikipedia.set_lang("fr")

    def search(self, string):
        return wikipedia.search(string)

    def get_search_result(self, string):
        print('[WIKIAPI] : ' + string)
        try:
            search = self.search(string)
            # Select the first search result
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
