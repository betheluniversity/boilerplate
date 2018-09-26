from flask import render_template
from flask.wrappers import Response as FlaskResponse
from flask_classy import FlaskView


class ExampleView(FlaskView):
    def __init__(self):
        pass

    def before_request(self, name, **kwargs):
        pass

    def after_request(self, name, response):
        if isinstance(response, FlaskResponse):
            pass

        return response

    def index(self):
        return render_template('index.html', python_variable='How to pass a variable from Python to HTML')

    # def get(self):
    #     pass

    def post(self):
        pass

    def decorated_get_route(self):
        pass

    def decorated_get_route_with_args(self, arg1, arg2):
        pass

    def decorated_post_route(self):
        pass