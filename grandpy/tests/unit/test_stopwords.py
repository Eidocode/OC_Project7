from grandpy.bot.stop_words import get_stop_words


def test_stopwords():
    # Call get_stop_words function
    stop_words = get_stop_words('./grandpy/bot/final_stop_words.fic')

    # Checks the existence of words in the stop words list
    test_list = (
        'auxquelles', 'bravo', 'desquelles', 'particulièrement', 'souhait'
    )
    for word in test_list:
        assert word in stop_words
