#Use this file to add utility functions

def get_config_file_name(*, environment:str):
    if environment == 'dev':
        name = 'app_conf_dev'
    if environment == 'prod':
        name = 'app_conf_prod'
    return name

def get_reviews(placeid):
    from flask import current_app
    import requests
    places_api_url = current_app.config.get('GMAPS_PLACES_API_BASE_URL')
    params = {
        "placeid": placeid,
        "key":current_app.config.get("API_KEY")
    }
    resp = requests.get(url=places_api_url, params=params).json()
    return resp.get('result').get('reviews') if resp.get('result').get('reviews') else None


