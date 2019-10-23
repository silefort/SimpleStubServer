from flask import Flask
import stubserver
import requests

if __name__ == "__main__":

    app = stubserver.StubServer()
    app.start()

    r = requests.get('http://localhost:5000/check')
    print "check:"
    print r.text

    r = requests.post('http://localhost:5000/bla')
    print "bla:"
    print r.status_code
    print r.text

    app.stop()
