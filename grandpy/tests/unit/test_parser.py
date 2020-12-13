from grandpy.bot.parser import Parser


# - Parsing :
class TestParser:
    # Instancier Parser()
    parser = Parser()

    # Test de l'instance parser
    def test_instance(self):
        assert isinstance(self.parser, Parser)

    # Envoyer une phrase au parser et récupérer le résultat
    def test_parser_valid(self):
        test_input = "Bonjour, je veux avoir des informations sur la tour Eiffel ?"
        test_result = self.parser.get_keywords(test_input)
        assert test_result == ['tour', 'eiffel']

    def test_parser_empty(self):
        test_input = "Bonjour, comment vas-tu Papy Bot ?"
        test_result = self.parser.get_keywords(test_input)
        assert test_result == []
