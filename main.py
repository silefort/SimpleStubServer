from flask import Flask
from flask import make_response

def build_response(body, statusCode, headers,responseTime):
    resp = make_response(body, statusCode)
    resp.headers = headers
    return resp

if __name__ == "__main__":
    app = Flask(__name__)

    # make a "check" route to test the web server
    @app.route('/check')
    def check():
        return "OK", 200

    # All other routes should end up in a 404
    # We catch it to provide custom responses
    @app.errorhandler(404)
    def page_not_found(error):
        headers = {}
        headers['X-entete'] = 'entete'
        headers['X-entete2'] = 'entete3'
        return build_response("ma rep",304, headers)
    
    app.run(host="0.0.0.0")
