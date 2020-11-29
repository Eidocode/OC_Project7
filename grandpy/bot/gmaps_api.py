import googlemaps


class GmapsAPI:
    def __init__(self, api_id):
        self.KEY = api_id
        self.gmaps = googlemaps.Client(key=self.KEY)

    def get_informations(self, string):
        print("[GMAPS API] : " + string)
        result = self.gmaps.geocode(string)

        return result


