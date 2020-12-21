from grandpy.bot.parser import Parser


# - Parsing :
class TestParser:
    # Instance Parser()
    parser = Parser()

    # Testing the parser instance
    def test_instance(self):
        assert isinstance(self.parser, Parser)

    # Send a sentence to the parser and get a words list result
    def test_parser_valid(self):
        test_input = "Bonjour, je veux avoir des informations sur la tour Eiffel ?"
        test_result = self.parser.get_keywords(test_input)
        assert test_result == ['tour', 'eiffel']

    # Send a sentence to the parser and get an empty list result
    def test_parser_empty(self):
        test_input = "Bonjour, comment vas-tu Papy Bot ?"
        test_result = self.parser.get_keywords(test_input)
        assert test_result == []
