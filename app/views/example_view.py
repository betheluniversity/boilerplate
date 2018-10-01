# Imports from Python global packages

# Imports from packages installed from requirements.txt
from flask import make_response, redirect, render_template, request, session
from flask.wrappers import Response as FlaskResponse
from flask_classy import FlaskView, route
from werkzeug.datastructures import ImmutableMultiDict

# Imports from elsewhere in this project
from app import app
from app.controllers.auth import uses_basic_auth
from app.controllers.example_controller import large_computational_function


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

    @route('/custom-name')
    def decorated_get_route(self):
        custom_content = '<p>Hello. This content was generated in the Python code</p>'
        return render_template('pass_through.html', raw_content=custom_content)

    @route('/args/<arg1>/<arg2>')
    def decorated_get_route_with_args(self, arg1, arg2):
        custom_content = '<p>The arguments sent to /args are %s and %s<p>' % (arg1, arg2)
        return render_template('pass_through.html', raw_content=custom_content)

    @route('/post-submission', methods=['POST'])
    def decorated_post_route(self):
        form = request.form
        if isinstance(form, ImmutableMultiDict):
            raw_data = form.to_dict()
        else:
            raw_data = {}
        parsed_data = """
        <div>
            The data sent to POST /form-submission is:<br/>
            %s
        </div>
        """ % raw_data
        return render_template('pass_through.html', raw_content=parsed_data)

    @uses_basic_auth
    def cronjob(self):
        content = "<p>The sum of all numbers from 1 to 10 is %s" % large_computational_function(10)
        return render_template('pass_through.html', raw_content=content)

    @route('/favicon.ico')
    def favicon(self):
        return redirect('/static/images/favicon.ico')

    def logout(self):
        session.clear()
        resp = make_response(redirect(app.config['LOGOUT_URL']))
        resp.set_cookie('MOD_AUTH_CAS_S', '', expires=0)
        resp.set_cookie('MOD_AUTH_CAS', '', expires=0)
        return resp
