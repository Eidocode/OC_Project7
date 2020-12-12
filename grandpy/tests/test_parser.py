from grandpy.bot.parser import Parser


# - Parsing :
class TestParser:
    # Instancier Parser()
    parser = Parser()

    # Test de l'instance parser
    def test_instance(self):
        assert isinstance(self.parser, Parser)

    # Envoyer une phrase au parser et récupérer le résultat
    def test_parser(self):
        test_input = "Bonjour, je veux avoir des informations sur la tour eiffel ?"
        test_result = self.parser.get_keywords(test_input)
        assert test_result == ['tour', 'eiffel']
