from functools import wraps
from flask import request, jsonify, current_app

def require_appkey(view_function, **kwargs):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):        
        key=current_app.config['API_KEY'].replace('\n', '')
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            return jsonify({"error":"Unauthorized access"}), 401
    return decorated_function