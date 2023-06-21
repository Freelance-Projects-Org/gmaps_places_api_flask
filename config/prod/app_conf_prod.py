DEBUG = False
SERVER_NAME = '127.0.0.1:8888'
GMAPS_PLACES_NEARBY_SEARCH_BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
with open(r'config\dev\api.key', 'r') as apikey:
    api_key = apikey.read().replace('\n', '')
    API_KEY = api_key