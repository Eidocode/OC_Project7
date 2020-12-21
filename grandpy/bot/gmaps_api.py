import googlemaps


class GmapsAPI:
    """
    Class used to communicate with GoogleMaps API

    ...

    Methods
    -------
    get_informations(string)
        Returns geocode according to the location (string)

    get_coordinates(string)
        Returns the coordinates (Latitude, Longitude and address) of the
        desired location (string).
        If GoogleMaps encounters an error, return the string 'error'
    """
    def __init__(self, api_id):
        self.KEY = api_id
        self.gmaps = googlemaps.Client(key=self.KEY)
        self.result = None

    def get_informations(self, string):
        return self.gmaps.geocode(string)

    def get_coordinates(self, string):
        try:
            self.result = self.get_informations(string)
            lat = self.result[0]['geometry']['location']['lat']
            lng = self.result[0]['geometry']['location']['lng']
            addr = self.result[0]['formatted_address']
            print("[GMAPS API] Latitude : " + str(lat))
            print("[GMAPS API] Longitude : " + str(lng))
            result = {
                'coord': {
                    'lat': lat,
                    'lng': lng
                },
                'addr': addr
            }
        except googlemaps.exceptions.HTTPError:
            print('Gmaps error')
            result = 'error'
        except IndexError:
            print('Index introuvable')
            result = 'error'

        return result
