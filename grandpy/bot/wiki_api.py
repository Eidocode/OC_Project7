import wikipedia
import requests

class WikiAPI:
    def __init__(self):
        wikipedia.set_lang("fr")
        self.page = None
    
    def get_search_result(self, string):
        print('[WIKIAPI] : ' + string)
        search = wikipedia.search(string)
        self.page = wikipedia.page(search[0])
        result = wikipedia.summary(search[0])
        return result
    
    def get_coordinates(self):
        URL = "https://fr.wikipedia.org/w/api.php?action=query&prop=coordinates&titles=" + self.page.title + "&format=json"

        json_result = requests.get(URL).json()
        json_page = json_result.get('query').get('pages')
        page_id = None

        for id in json_page:
            page_id = id
        
        coordinates = json_page.get(page_id).get('coordinates')
        latitude = coordinates[0]['lat']
        longitude = coordinates[0]['lon']

        return latitude, longitude