from app import sqlite_db as db


# This class will automatically create a table in the SQLite database if it doesn't exist, insert a row into that table
# when a new instance of it gets made with new values, or edit an existing row under the right conditions.
class Users(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, new_username, new_first_name, new_last_name, new_email):
        self.username = new_username
        self.first_name = new_first_name
        self.last_name = new_last_name
        self.email = new_email

    def __repr__(self):
        return "<User '%(0)s %(1)s'>" % {'0': self.first_name, '1': self.last_name}