import googlemaps


class GmapsAPI:
    def __init__(self, api_id):
        self.KEY = api_id
        self.gmaps = googlemaps.Client(key=self.KEY)

    def get_informations(self, string):
        print("[GMAPS API] : " + string)
        result = self.gmaps.geocode(string)

        return result

    def get_coordinates(self, string):
        res = self.get_informations(string)
        lat = res[0]["geometry"]["location"]["lat"]
        lng = res[0]["geometry"]["location"]["lng"]
        print("[GMAPS API] Latitude : " + str(lat))
        print("[GMAPS API] Longitude : " + str(lng))

        result = {
            "lat": lat,
            "lng": lng
        }

        return result
