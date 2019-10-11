class TFlask():
    def request_context(self, environ):
        print("SELF - {0}".format(self))
        return RequestContext(self, environ)

    def wsgi_app(self, environ, start_response):
        with self.request_context(environ):
            return environ

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

class RequestContext(object):
    def __init__(self, app, environ):
        print("APP - {0}".format(app))
        print("ENV - {0}".format(environ))
        self.app = app

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, tb):
        pass

environ = {"query_string": "/healthcheck", "method":"GET"}
start_response = {}

flask = TFlask()
flask(environ, start_response)


