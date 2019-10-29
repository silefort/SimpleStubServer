from flask import Flask
import stubserver
import requests

if __name__ == "__main__":

    app = stubserver.StubServer(port=5000, status=404, body='body')
    app.start()

    r = requests.get('http://localhost:5000/check')
    print "check:" + str(r.text)

    r = requests.post('http://localhost:5000/bla')
    print "bla:" + str(r.text)

    app.stop()
