from functools import wraps

from flask import request, Response

from app import app


# Put custom authentication methods in this file so that all Views can import them
def _check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == app.config['AUTH_USERNAME'] and password == app.config['AUTH_PASSWORD']


def _failed_authentication():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def uses_basic_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not _check_auth(auth.username, auth.password):
            return _failed_authentication()
        return f(*args, **kwargs)

    return decorated
