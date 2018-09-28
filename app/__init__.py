from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
sqlite_db = SQLAlchemy(app)
app.url_map.strict_slashes = False

from app.views.example_view import ExampleView
ExampleView.register(app, route_base='/')
