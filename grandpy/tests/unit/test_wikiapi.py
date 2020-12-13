from grandpy.bot.wiki_api import WikiAPI


# - Wikipedia
class TestWikipedia:
    # Instancier WikiAPI()
    wiki = WikiAPI()

    # Test instance wiki
    def test_instance(self):
        assert isinstance(self.wiki, WikiAPI)

    def test_view_result(self, monkeypatch):
        view_result = {
            'summary': 'Tour de fer puddlé de 324 mètres de hauteur',
            'url': 'https://fr.wikipedia.org/wiki/Tour_Eiffel',
            'title': 'Tour Eiffel'
        }

        def mockreturn(self, string):
            return view_result

        search = 'tour eiffel'
        monkeypatch.setattr(self.wiki, 'get_search_result', mockreturn)
        wiki_res = self.wiki.get_search_result(self, search)

        # Test le sommaire de la page
        assert wiki_res['summary'] == view_result['summary']
        # Test l'URL de la page
        assert wiki_res['url'] == view_result['url']
        # Test le titre de la page Wikipedia
        assert wiki_res['title'] == view_result['title']

    # Envoyer une chaine intraitable (doit retourner une erreur)
    def test_index_error(self, monkeypatch):
        result = []

        def mockreturn(string):
            return result

        search = 'heyedfds'
        monkeypatch.setattr(self.wiki, 'search', mockreturn)
        wiki_res = self.wiki.get_search_result(search)

        assert wiki_res == 'error'
