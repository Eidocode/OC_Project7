import re

from .stop_words import get_stop_words


class Parser:
    """docstring for Parser"""

    def __init__(self):
        self.stop_words = get_stop_words('./grandpy/bot/final_stop_words.fic')

    def get_keywords(self, input):

        user_input = None
        user_input = re.sub(r"\W+", " ", input).lower()
        user_input = user_input.split(' ')

        keywords = []
        for word in user_input:
            if word not in self.stop_words and word != '':
                keywords.append(word)

        return keywords


# parser = Parser()

# test = parser.get_keywords("Bonjour, comment allez-vous ? J'espère que tout va bien.")
# test = parser.get_keywords("Bonjour, je recherche la tour eiffel !")
# print(test)
