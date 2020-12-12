from grandpy.bot.gmaps_api import GmapsAPI
from config import GMAPS_APP_ID


# API GoogleMaps
class TestGmaps:
    # Instancier GmapsAPI()
    gmap = GmapsAPI(GMAPS_APP_ID)

    # Test instance gmaps
    def test_instance(self):
        assert isinstance(self.gmap, GmapsAPI)

    # Envoyer une chaine de caractère à traiter et récupérer l'adresse du lieu
    def test_address(self):
        addr = self.gmap.get_address('tour eiffel')
        assert addr == 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France'

    # Récupérer la latitude et longitude
    def test_coord(self):
        coord = self.gmap.get_coordinates('tour eiffel')
        assert coord == {'lat': 48.85837009999999, 'lng': 2.2944813}

    # Envoyer une chaine intraitable (doit retourner une erreur)
    def test_error(self):
        coord = self.gmap.get_coordinates('fdslmfdsm')
        assert coord == 'error'
