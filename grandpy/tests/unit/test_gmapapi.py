"""
Unit test for GoogleMaps API
"""
from grandpy.bot.gmaps_api import GmapsAPI
from config import GMAPS_APP_ID


# API GoogleMaps
class TestGmaps:
    # Instance GmapsAPI()
    gmap = GmapsAPI(GMAPS_APP_ID)

    # Test instance gmaps
    def test_instance(self):
        assert isinstance(self.gmap, GmapsAPI)

    def test_view_result(self, monkeypatch):
        view_result = [
            {
                "formatted_address": (
                        "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, "
                        "France"
                    ),
                "geometry": {
                    "location": {
                        "lat": 48.85837009999999,
                        "lng": 2.2944813
                    }
                }
            }
        ]

        def mockreturn(string):
            return view_result

        search = 'tour eiffel'
        monkeypatch.setattr(self.gmap, 'get_informations', mockreturn)
        gmap_res = self.gmap.get_coordinates(search)

        assert gmap_res['coord'] == view_result[0]["geometry"]["location"]
        assert gmap_res['addr'] == view_result[0]["formatted_address"]

    # sends an incomprehensible string (must return an error)
    def test_index_error(self, monkeypatch):
        result = []

        def mockreturn(string):
            return result

        search = 'heyedfds'
        monkeypatch.setattr(self.gmap, 'get_informations', mockreturn)
        gmap_res = self.gmap.get_coordinates(search)

        assert gmap_res == 'error'
