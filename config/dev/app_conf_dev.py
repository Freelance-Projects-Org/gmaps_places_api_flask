DEBUG = True
SERVER_NAME = '127.0.0.1:3000'
GMAPS_PLACES_NEARBY_SEARCH_BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
GMAPS_PLACES_API_BASE_URL = "https://maps.googleapis.com/maps/api/place/details/json"
with open(r'config\dev\api.key', 'r') as apikey:
    api_key = apikey.read().replace('\n', '')
    API_KEY = api_key