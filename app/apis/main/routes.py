from googlemaps import convert
import time
import requests
from requests.auth import HTTPBasicAuth
from flask import request, current_app, jsonify
from app.apis.components.decorators import require_appkey
from app.apis.components.utils import get_reviews
from app.apis.main import main

#test data
# lat = "40.686779099999995"
# longitude = "-73.9548217"
# search_type = "beauty_salon"
# keyword = "salon"
# open_now=True
# rank_by = "distance"

@main.route('/get_nearby_places')
@require_appkey
def get_nearby_places():
    nearby_places_results = {"results":[]}
    key = current_app.config.get("API_KEY")   
    url = current_app.config.get('GMAPS_PLACES_NEARBY_SEARCH_BASE_URL')
    search_type = request.args.get('search_type', type = str)
    keyword = request.args.get("keyword", type = str)
    lat = request.args.get('lat', type = str)
    longitude = request.args.get('longitude', type = str)
    location = convert.latlng({"lat":lat, "lng":longitude})    
    open_now = request.args.get('open_now', default=True, type=bool)
    rank_by = request.args.get('rank_by', default = None, type=str)
    radius = request.args.get('radius', type=str, default=None)
    language = request.args.get('language', type=str, default='en')

    params = {
        'location':location,
        'keyword':keyword,
        'language':language,
        'min_price':0,  #most affordable 
        'max_price':4,  #most expensive
        'open_now':open_now,
        'rankby':rank_by,
        'type':search_type,
        'radius':radius,
        'key':key         
    }
    nearby_places = requests.get(url=url, params=params).json()
    nearby_places_results["results"] = nearby_places["results"]
    if nearby_places.get('next_page_token'):
        nearby_places_results.update({"next_page_token":nearby_places.get('next_page_token')})
    for place in nearby_places_results["results"]:
        placeid = place.get("place_id")
        place["reviews"] = get_reviews(placeid=placeid)
    if request.args.get('paginate'):
        if not 'next_page_token' in request.args:
            return jsonify({"error":"Missing next page token"}), 401
        else:
            if 'next_page_token' in nearby_places.keys() and request.args.get('next_page_token') == nearby_places.get('next_page_token'): 
                while 'next_page_token' in nearby_places.keys():
                    # print(nearby_places['next_page_token'])
                    params.update({"pagetoken": nearby_places["next_page_token"]})
                    time.sleep(2)
                    nearby_places = requests.get(url=url, params=params).json()
                    nearby_places_results_contd = nearby_places["results"]
                    for place in nearby_places_results_contd:
                        placeid = place.get("place_id")
                        place["reviews"] = get_reviews(placeid=placeid)                    
                    nearby_places_results["results"].extend(nearby_places_results_contd)
                nearby_places_results.pop('next_page_token')                    
            else:
                return jsonify({"error":"Bad request"}), 500
    return nearby_places_results


