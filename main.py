from flask import Flask
from flask import make_response
import yesserver
import requests

if __name__ == "__main__":

    app = yesserver.YesServer()
    app.start()

    r = requests.get('http://localhost:5000/check')
    print "check:"
    print r.text

    r = requests.post('http://localhost:5000/bla')
    print "bla:"
    print r.status_code
    print r.text

    app.stop()
