import flask
import time
import multiprocessing

class StubServer:
    def __init__(self, debug=False, port=5000):
        self.server = None
        self.port = port;
        self.manager = multiprocessing.Manager()

    def server_thread(self):
        app = flask.Flask(__name__)

        @app.errorhandler(404)
        def page_not_found(error):
            print self.port
            return "OK", 200
        
        app.run(host="0.0.0.0", port=self.port)

    def start(self):
        """
        Start the server (async)
        """
        self.server = multiprocessing.Process(target=self.server_thread)
        self.server.start()
        time.sleep(0.5) # Let the server start, just in case...

    def stop(self):
        """
        Stop the server
        """
        self.manager.shutdown()
        self.server.terminate()
        self.server.join()
