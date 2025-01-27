from flask_pymongo import PyMongo

class Database:
    def __init__(self, app):
        self.app = app
        self.mongo = PyMongo(app)

    def get_db(self):
        return self.mongo.db
