from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
app.url_map.strict_slashes = False

from app.views.example_view import ExampleView
ExampleView.register(app, route_base='/')
