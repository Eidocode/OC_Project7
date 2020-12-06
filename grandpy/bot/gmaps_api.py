import googlemaps


class GmapsAPI:
    def __init__(self, api_id):
        self.KEY = api_id
        self.gmaps = googlemaps.Client(key=self.KEY)
        self.result = None

    def __get_informations(self, string):
        self.result = self.gmaps.geocode(string)

    def get_coordinates(self, string):
        try:
            self.__get_informations(string)
            lat = self.result[0]["geometry"]["location"]["lat"]
            lng = self.result[0]["geometry"]["location"]["lng"]
            print("[GMAPS API] Latitude : " + str(lat))
            print("[GMAPS API] Longitude : " + str(lng))
            result = {
                "lat": lat,
                "lng": lng
            }
        except googlemaps.exceptions.HTTPError:
            print('Gmaps error')
            result = 'error'
        except IndexError:
            print('Index introuvable')
            result = 'error'

        return result

    def get_address(self, string):
        self.__get_informations(string)
        addr = self.result[0]["formatted_address"]
        return addr
