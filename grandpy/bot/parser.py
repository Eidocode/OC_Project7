import re

from .stop_words import get_stop_words


class Parser:
    """
    Class used to parse the question asked by the user to GrandPy.

    ...

    Methods
    -------
    get_keywords(input)
        Returns a list with the remaining words after comparing with
        "Stop_Words" list stored in "final_stop_words.fic"
    """

    def __init__(self):
        # File where "stop_words" are stored
        self.stop_words = get_stop_words('./grandpy/bot/final_stop_words.fic')

    def get_keywords(self, input):
        # Removes punctuation and lowercase characters
        user_input = re.sub(r"\W+", " ", input).lower()
        user_input = user_input.split(' ')

        keywords = []
        for word in user_input:
            # Compare users's words with the stop_words list
            if word not in self.stop_words and word != '':
                keywords.append(word)

        return keywords
