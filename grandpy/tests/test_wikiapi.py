from grandpy.bot.wiki_api import WikiAPI


# - Wikipedia
class TestWikipedia:
    # Instancier WikiAPI()
    wiki = WikiAPI()

    # Test instance wiki
    def test_instance(self):
        assert isinstance(self.wiki, WikiAPI)

    # # Envoyer une chaine de caractère à traiter et récupérer l'URL de la page
    # def test_url(self):
    #     self.wiki.get_search_result('tour eiffel')
    #     assert self.wiki.page.url == 'https://fr.wikipedia.org/wiki/Tour_Eiffel'

    # # Récupérer le titre de la page Wikipedia
    # def test_api(self):
    #     self.wiki.get_search_result('tour eiffel')
    #     assert self.wiki.page.title == 'Tour Eiffel'

    def test_view_result(self, monkeypatch):
        view_result = {
            'summary': 'Tour de fer puddlé de 324 mètres de hauteur',
            'url': 'https://fr.wikipedia.org/wiki/Tour_Eiffel',
            'title': 'Tour Eiffel'
        }

        def mockreturn(self, string):
            return view_result

        search = 'tour eiffel'
        monkeypatch.setattr(WikiAPI, 'get_search_result', mockreturn)
        wiki_res = self.wiki.get_search_result(search)

        # Test le sommaire de la page
        assert wiki_res['summary'] == 'Tour de fer puddlé de 324 mètres de hauteur'
        # Test l'URL de la page
        assert wiki_res['url'] == 'https://fr.wikipedia.org/wiki/Tour_Eiffel'
        # Test le titre de la page Wikipedia
        assert wiki_res['title'] == 'Tour Eiffel'

    # Envoyer une chaine intraitable (doit retourner une erreur)
    def test_error(self):
        test = self.wiki.get_search_result('fdsfs')
        assert test == 'error'
