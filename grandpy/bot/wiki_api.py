import wikipedia

class WikiAPI:
    def __init__(self):
        wikipedia.set_lang("fr")
    
    def get_search_result(self, string):
        print('[WIKIAPI] : ' + string)
        result = wikipedia.summary(string, sentences=2)
        return result